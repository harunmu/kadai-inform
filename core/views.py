from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.
from main import scraping
from craft_mail import auto_email
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import requests,time

def wakeup(request):
    return JsonResponse({"message": "I'm awake!"})

@csrf_exempt
def cron_run(request):
    requests.get("https://kadai-inform.onrender.com/wakeup/")
    time.sleep(5)  # レンダーが目を覚ます時間を確保
    if request.method == 'GET':
        inform_date_data = scraping()
        auto_email(inform_date_data)
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'invalid method'},status=405)

class HomeView(TemplateView):
    template_name = "core/home.html"

    def post(self, *args, **kwargs):
        inform_date_data = scraping()
        # day = inform_date_data[2]
        # auto_email(day)
        # day = '123'
        auto_email(inform_date_data)
        return render(self.request, self.template_name)
    
