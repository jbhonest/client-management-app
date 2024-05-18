from django.urls import path
from . import views

app_name = "clients_app"
urlpatterns = [
    path("list/", views.ClientListView.as_view(), name="list"),
    path("create/", views.clients_create, name="create"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
