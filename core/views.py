from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.
from main import scraping
from craft_mail import auto_email

class HomeView(TemplateView):
    template_name = "core/home.html"

    def post(self, *args, **kwargs):
        # inform_date_data = scraping()
        # day = inform_date_data[2]
        # auto_email(day)
        day = '123'
        auto_email(day)
        return render(self.request, self.template_name)