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
        
        email_contents = []
        
        kadai_deadline_list,class_name_list= scraping()
        current_day = datetime.now().date()

        for class_name, kadai_deadline in zip(class_name_list,kadai_deadline_list):
            deadline = datetime.strptime(kadai_deadline[0],'%Y/%m/%d')
            deadline_date = deadline.date()

            deadline_limit = deadline_date - current_day
            deadline_limit_date = deadline_limit.days
            if deadline_limit_date <= 7:
                contents_info = [deadline_limit_date,class_name,deadline_date]
                email_contents.append(contents_info)
                
        auto_email(deadline_limit_date,class_name)
        
        return JsonResponse({'status':'success'})
    
    return JsonResponse({'status':'invalid method'},status=405)


class HomeView(TemplateView):
    template_name = "core/home.html"

    def post(self, *args, **kwargs):
        
        email_contents = []
        
        kadai_deadline_list,class_name_list= scraping()
        current_day = datetime.now().date()
        
        for class_name, kadai_deadline in zip(class_name_list,kadai_deadline_list):
            deadline = datetime.strptime(kadai_deadline[0],'%Y/%m/%d')
            deadline_date = deadline.date()

            deadline_limit = deadline_date - current_day
            deadline_limit_date = deadline_limit.days
            if deadline_limit_date <= 7:
                contents_info = [deadline_limit_date,class_name,deadline_date]
                email_contents.append(contents_info)

        auto_email(deadline_limit_date,class_name)
        
        return render(self.request, self.template_name)
    
