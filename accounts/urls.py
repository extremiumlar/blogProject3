from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)
from .views import (
    user_login,
    dashboard_view,
    user_register,
    SignupView,
    edit_user,
    EditUserView,
)

urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', dashboard_view, name='profile'),

    # foydalanuvchi parolini o'zgartirish
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # foydalanuvchi parolini qayta tiklash
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Forma va view qo'lda yozilgan url :
    path('signup/', user_register, name = 'signup'),

    # tayyor createviewdan foydalangan url
    # path('signup/', SignupView.as_view(), name='signup'),

    # view funksiyada yozilgan url
    # path('profile/edit/', edit_user, name = 'edit_user'),

    # view classda yozilgan url
    path('profile/edit', EditUserView.as_view(), name = 'edit_user'),

]