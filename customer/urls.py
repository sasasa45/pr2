from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns = [
    path('signup/', SignUpView.as_view(),name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html', success_url=reverse_lazy('/')),name='password_change'),
    path('profile/', customerupdate ,name='profile'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),
    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
     name="password_reset_confirm"),
    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
        name="password_reset_complete"),
]
