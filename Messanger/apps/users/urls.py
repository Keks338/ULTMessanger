from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("sign-up/", views.signUp, name="signUp"),
    path("login/", views.loginPage, name="loginPage"),
    path("logout/", views.logoutUser, name="logoutUser"),
    # path("admin-panel/", views.adminPage, name="adminka"),
    path("editform/<int:user_id>/", views.edit_user, name="profileEdit"),
    path("profile/<int:user_id>/", views.profilePage, name="profile"),
]