from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Props
from .forms import PropsForm
from django.views.generic import DetailView, DeleteView


# Create your views here.

@staff_member_required(login_url="profile")
def props_home(request):
    props = Props.objects.order_by('date')
    return render(request, 'proposal/prop_home.html', {'props': props})


class PropsDeleteView(DeleteView):
    model = Props
    template_name = 'proposal/details_view.html'
    success_url = '/props/'
    context_object_name = 'props'

def create(request):
    error = ''
    if request.method == 'POST':
        form = PropsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = PropsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'proposal/create.html', data)
