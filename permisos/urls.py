from django.urls import path
from . import views

app_name = 'permisos'

urlpatterns = [
    path('', views.permiso_list, name='permiso-list'),
    path('<int:pk>/', views.permiso_detail, name='permiso-detail'),
    path('create/', views.permiso_create, name='permiso-create'),
    path('<int:pk>/update/', views.permiso_update, name='permiso-update'),
    path('<int:pk>/delete/', views.permiso_delete, name='permiso-delete'),
]
