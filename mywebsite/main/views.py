from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DeleteView, DetailView, UpdateView


from .forms import RegisterForm, ServicesForm
from .models import Services


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
