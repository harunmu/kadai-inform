from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LogoutView as DjangoLogoutView

from create_email import send_test_email
from .forms import SignupForm, UserUpdateForm

User = get_user_model()

class SignupView(CreateView):
    template_name = "registration/signup.html"
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('account:signup_done')

    def form_valid(self,form):
        user = form.save()
        send_test_email(user.email)
        return super().form_valid(form)

class SignupDoneView(TemplateView):
    template_name = "registration/signup_done.html"
    
class LoginView(TemplateView):
    template_name = "registration/login.html"

class UserSettingView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "registration/setting.html"
    success_url = reverse_lazy('account:setting')

    def get_object(self, queryset=None):
        return self.request.user

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('core:home')