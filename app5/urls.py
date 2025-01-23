from django.urls import path
from .views import userCreating, UserRUD

urlpatterns = [
    path('users/', userCreating.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRUD.as_view(), name='user-detail'),
]