from django.urls import path
from .views import RegisterView, ProfileView, CreateUserView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", ProfileView.as_view(), name="profile"),
    path("create-user/", CreateUserView.as_view(), name="create_user"),
]
