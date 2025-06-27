from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.event_form, name='event_form'),
    path('event/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event/register/', views.register_attend, name='register_attend'),
    path('event/details/<int:event_id>/', views.details, name='details'),
    path('event/ticket/<int:event_id>/', views.ticket_system, name='ticket_system'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/edit-ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('event/delete-ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    path('attendees/', views.all_attendees, name='all_attendees'),
    path('tickets/', views.event_tickets, name='event_tickets'),
    path('search/', views.search_results, name='search_results'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='event_form'), name='logout'),
    path('ticket/view/<int:ticket_id>/', views.view_ticket, name='view_ticket'),
    path('ticket/download/<int:ticket_id>/', views.download_ticket_pdf, name='download_ticket_pdf'),





]

