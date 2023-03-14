from django.urls import path, include
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.index, name='home'),
    path('services', views.services, name='services'),
    path('about-us', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('profile', views.profile_view, name="profile"),
    path('register', RegisterView.as_view(), name="register"),
    path('settings', views.servicesSettings, name="settings"),
    path('createServices', views.createSettingsServices, name="createServices"),
    path('settings/<int:pk>', views.ServicesDetailView.as_view(), name="services-detail"),
    path('settings/<int:pk>/update', views.ServicesUpdateView.as_view(), name="services-update"),
    path('secondMainPage', views.createFeedback, name='secondMainPage'),
    path('feedbackDetails', views.feedbackSettings, name='feedbackSettings'),
    path('feedbackArchive', views.feedbackArchive, name='feedbackArchive'),
    path('change_feedback_status/', views.change_feedback_status, name='change_feedback_status'),
    path('feedback/delete/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),

]
