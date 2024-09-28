import secrets

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm, UserPasswordResetForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        token = secrets.token_hex(16)
        user.token = token
        user.save()

        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'

        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения почты необходимо перейти по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserPasswordResetView(PasswordResetView):
    template_name = "users/password_reset_form.html"
    form_class = UserPasswordResetForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        try:
            user = get_object_or_404(User, email=email)
            if user:
                password = User.objects.make_random_password(length=10)
                user.set_password(password)
                user.save()
                send_mail(
                    subject="Сброс пароля",
                    message=f"Ваш новый пароль: {password}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email]
                )
                return redirect(reverse("users:login"))
        except:
            return redirect(reverse("users:invalid-email"))


class UserInvalidEmail(TemplateView):
    template_name = "users/invalid_email.html"
