from django.urls import path

from django.contrib.auth import views as auth_views


from . import views

# entries/urls.py

urlpatterns = [

    path('', views.home, name='home'),
    path(
        "entry/",
        views.EntryListView.as_view(),
        name="entry-list"
    ),
    path(
        "entry/<int:pk>",
        views.EntryDetailView.as_view(),
        name="entry-detail"
    ),
    path(
        "create",
        views.EntryCreateView.as_view(),
        name="entry-create"
    ),
    path(
        "entry/<int:pk>/update",
        views.EntryUpdateView.as_view(),
        name="entry-update",
    ),
    path(
        "entry/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete",
    ),

    path('remedios/', views.RemedioListView.as_view(), name='remedio-list'),
    path('remedio/<int:pk>/',views.RemedioDetailView.as_view(), name='remedio-detail'),
    path('remedio/new/', views.RemedioCreateView.as_view(), name='remedio-create'),
    path('remedio/<int:pk>/edit/', views.RemedioUpdateView.as_view(), name='remedio-update'),
    path('remedio/<int:pk>/delete/', views.RemedioDeleteView.as_view(), name='remedio-delete'),
    
    path('sono/', views.SonoRegistroListView.as_view(), name='sono-registro-list'),

    path('sono/<int:pk>/', views.SonoDetailView.as_view(), name='sono-detail'),

    path('calendar/', views.CalendarView.as_view(), name='calendario'),

    path('login/', auth_views.LoginView.as_view(template_name='entries/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('register/', views.register, name='register'),






]