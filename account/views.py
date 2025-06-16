from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from django.views.generic.base import TemplateView

from create_message import auto_email
from .forms import SignupForm

User = get_user_model()

class SignupView(CreateView):
    template_name = "registration/signup.html"
    model = User
    form_class = SignupForm
    success_url = reverse_lazy('account:signup_done')

    def form_valid(self,form):
        response = super().form_valid(form)
        user = self.object

        title = "Thank You for Registering with service"
        email_address = user.email
        message = "登録が完了しました。"
        auto_email(title,email_address,message)

        return response

class SignupDoneView(TemplateView):
    template_name = "registration/signup_done.html"