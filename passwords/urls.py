from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<str:id>', views.view_secret, name='view_secret'),
    path('generated/<str:id>', views.generated, name='generated'),
    path('accounts/new', views.create_account, name='create_account'),
    path('sessions/new', views.Session.new, name='login'),
    path('sessions/create', views.Session.create, name='create_session'),
    path('sessions/delete', views.Session.delete, name='logout'),
    path('my_vault', views.MyVault.my_vault, name='my_vault'),
    path('my_vault/new', views.MyVault.add, name='new_vault'),
]