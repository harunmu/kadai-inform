from django.shortcuts import render
from django.views.generic import TemplateView, View

# Create your views here.
from main import scraping
from craft_mail import auto_email
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import requests,time
from datetime import datetime,timedelta

# def wakeup(request):
#     return JsonResponse({"message": "I'm awake!"})

@csrf_exempt
def cron_run(request):
    if request.method == 'GET':
        kadai_deadline_list,class_name_list= scraping()
        current_day = datetime.now().date()
        # execute_day = current_day + timedelta(days=3)
        # execute_day_date = execute_day.date()

        for i, kadai_deadline in enumerate(kadai_deadline_list):
            deadline = datetime.strptime(kadai_deadline,'%Y/%m/%d')
            deadline_date = deadline.date()

            deadline_limit = deadline_date - current_day
            deadline_limit_date = deadline_limit.days
            class_name = class_name_list[i]

            # if deadline_limit_date <= 3:
            auto_email(deadline_limit_date,class_name)
        
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'invalid method'},status=405)

class HomeView(TemplateView):
    template_name = "core/home.html"

    def post(self, *args, **kwargs):
        kadai_deadline_list,class_name_list= scraping()
        current_day = datetime.now().date()
        # execute_day = current_day + timedelta(days=3)
        # execute_day_date = execute_day.date()

        for i, kadai_deadline in enumerate(kadai_deadline_list):
            deadline = datetime.strptime(kadai_deadline,'%Y/%m/%d')
            deadline_date = deadline.date()

            deadline_limit = deadline_date - current_day
            deadline_limit_date = deadline_limit.days
            class_name = class_name_list[i]

            # if deadline_limit_date <= 3:
            auto_email(deadline_limit_date,class_name)
        return render(self.request, self.template_name)
    
