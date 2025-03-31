from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.
from main import scraping
from craft_mail import auto_email

class HomeView(TemplateView):
    template_name = "core/home.html"

    def post(self, *args, **kwargs):
        # scraping()
        auto_email()
        return render(self.request, self.template_name)