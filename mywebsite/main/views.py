from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    return render(request, 'main/services.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def secondMainPage(request):
    return render(request, 'main/secondMainPage.html')


@login_required(login_url="main/login.html")
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
    return render(request, 'main/settingsServices.html', {'services': service})


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

@login_required(login_url="login")
def feedbackSettings(request):
    orderbyList = ['status', 'date', 'time']
    feedback = Feedback.objects.order_by(*orderbyList)
    return render(request, 'main/feedbackDetails.html', {'feedback': feedback})

@login_required(login_url="login")
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

def delete_services(request, services_id):
    services = Services.objects.get(id=services_id)
    services.delete()
    return redirect('servicesDetails')

@login_required(login_url="login")
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

    return render(request, 'main/servicesDetails.html', {'services': services})


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


def add_user(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_staff = request.POST.get('is_staff')

        if login and name and surname and email and password:
            try:
                user = User.objects.create_user(username=login, email=email, password=password, first_name=name,
                                                last_name=surname, is_staff=is_staff)
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        else:
            return JsonResponse({'success': False, 'message': 'Не все поля заполнены'})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password"
    else:
        error_message = None
    return render(request, 'main/login.html', {'error_message': error_message})


def aboutFeedback(request):
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

    return render(request, 'main/about.html', data)


def send_feedback(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronymic = request.POST.get('patronymic')
        phone_number = request.POST.get('phone_number')
        full_text = request.POST.get('full_text')
        date = request.POST.get('date')
        time = request.POST.get('time')

        if surname != '' and name != '' and phone_number != '':
            try:
                feedback = Feedback.objects.create(surname=surname, name=name, patronymic=patronymic,
                                                   phone_number=phone_number, feedback_text=full_text,
                                                   date=date, time=time)
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        else:
            return JsonResponse({'success': False,
                                 'message': 'Ошибка. Фамилия: {}, Имя: {}, Номер телефона: {}, Дата: {}, Время: {}'.format(
                                     surname, name, phone_number, date, time)})

def servicesSanteh(request):
    service = Services.objects.all()
    return render(request, 'main/santeh.html', {'services': service})

def servicesElectric(request):
    service = Services.objects.all()
    return render(request, 'main/electric.html', {'services': service})

def servicesBrick(request):
    service = Services.objects.all()
    return render(request, 'main/brick.html', {'services': service})

def servicesDecorative(request):
    service = Services.objects.all()
    return render(request, 'main/decorative.html', {'services': service})

def servicesCosmetic(request):
    service = Services.objects.all()
    return render(request, 'main/cosmetic.html', {'services': service})

def servicesAnother(request):
    service = Services.objects.all()
    return render(request, 'main/another.html', {'services': service})