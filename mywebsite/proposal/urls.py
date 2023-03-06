
from django.urls import path
from . import views

urlpatterns = [
    path('', views.props_home, name='props'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PropsDeleteView.as_view(), name='props-delete')
]