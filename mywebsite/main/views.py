from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DeleteView, DetailView, UpdateView


from .forms import RegisterForm, ServicesForm, FeedbackForm
from .models import Services, Feedback


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def services(request):
    service = Services.objects.all()
    return render(request, 'main/services.html', {'services' : service})


def contacts(request):
    return render(request, 'main/contacts.html')

def secondMainPage(request):
    return render(request, 'main/secondMainPage.html')


@login_required
def profile_view(request):
    return render(request, 'main/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("profile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ServicesDetailView(DeleteView):
    model = Services
    template_name = 'main/servicesDetailView.html'
    success_url = '/settings'
    context_object_name = 'services'

class ServicesUpdateView(UpdateView):
        model = Services
        template_name = 'main/changeServices.html'
        form_class = ServicesForm
        success_url = '/settings'
        context_object_name = 'services'


def servicesSettings(request):
    service = Services.objects.order_by('category')
    return render(request, 'main/settingsServices.html', {'services' : service})

def createSettingsServices(request):
    error = ''
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ServicesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/createServices.html', data)



def createFeedback(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'

    form = FeedbackForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/secondMainPage.html', data)

def feedbackSettings(request):
    orderbyList = ['status', 'date', 'time']
    feedback = Feedback.objects.order_by(*orderbyList)
    return render(request, 'main/feedbackDetails.html', {'feedback' : feedback})

def feedbackArchive(request):
    orderbyList = ['status', 'date', 'time']
    feedback = Feedback.objects.order_by(*orderbyList)
    return render(request, 'main/feedbackArchive.html', {'feedback': feedback})

def change_feedback_status(request):
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        new_status = request.POST.get('new_status')
        feedback = Feedback.objects.get(id=feedback_id)
        feedback.status = new_status
        feedback.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def delete_feedback(request, feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    feedback.delete()
    return redirect('feedbackArchive')

def servicesDetails(request):
    orderbyList = ['category', 'title', 'price']
    selected_category = request.GET.get('category', 'all')
    search_query = request.GET.get('query', '')

    if selected_category == 'all':
        services = Services.objects.order_by(*orderbyList)
    else:
        services = Services.objects.filter(category=selected_category).order_by(*orderbyList)

    if search_query:
        services = services.filter(title__icontains=search_query)

    return render(request, 'main/servicesDetails.html', {'services' : services})

def edit_service(request):
    if request.method == 'POST':
        service_id = request.POST.get('service_id')
        title = request.POST.get('title')
        price = request.POST.get('price')
        full_text = request.POST.get('full_text')
        category = request.POST.get('category')

        if title and price and full_text and category:  # Проверяем, что все поля заполнены
            try:
                service = Services.objects.get(id=service_id)
                service.title = title
                service.price = price
                service.full_text = full_text
                service.category = category
                service.save()
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        else:
            return JsonResponse({'success': False, 'message': 'Не все поля заполнены'})


def add_service(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        full_text = request.POST.get('full_text')
        category = request.POST.get('category')

        if title and price and full_text and category:  # Проверяем, что все поля заполнены
            try:
                service = Services.objects.create(title=title, price=price, full_text=full_text, category=category)
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        else:
            return JsonResponse({'success': False, 'message': 'Не все поля заполнены'})