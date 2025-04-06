from django.urls import path, include
from . import views
from .views import RegisterView

urlpatterns = [
    # path('', views.index, name='home'),
    path('services', views.services, name='services'),
    path('about-us', views.aboutFeedback, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('profile', views.profile_view, name="profile"),
    path('register', RegisterView.as_view(), name="register"),
    path('settings', views.servicesSettings, name="settings"),
    path('createServices', views.createSettingsServices, name="createServices"),
    path('settings/<int:pk>', views.ServicesDetailView.as_view(), name="services-detail"),
    path('settings/<int:pk>/update', views.ServicesUpdateView.as_view(), name="services-update"),
    path('', views.createFeedback, name='home'),
    path('feedbackDetails', views.feedbackSettings, name='feedbackSettings'),
    path('feedbackArchive', views.feedbackArchive, name='feedbackArchive'),
    path('change_feedback_status/', views.change_feedback_status, name='change_feedback_status'),
    path('feedback/delete/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
    path('services/delete/<int:services_id>/', views.delete_services, name='delete_services'),
    path('servicesDetails', views.servicesDetails, name='servicesDetails'),
    path('edit_service/', views.edit_service, name='edit_service'),
    path('add_service/', views.add_service, name='add_service'),
    path('add_user/', views.add_user, name='add_user'),
    path('login/', views.login_view, name='login'),
    path('send_feedback/', views.send_feedback, name='send_feedback'),
    path('plumbing/', views.servicesSanteh, name='santeh'),
    path('electric/', views.servicesElectric, name='electric'),
    path('tile/', views.servicesBrick, name='brick'),
    path('decorative/', views.servicesDecorative, name='decorative'),
    path('cosmetic/', views.servicesCosmetic, name='cosmetic'),
    path('another/', views.servicesAnother, name='another')

]
