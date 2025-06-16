from django.shortcuts import render
from django.views.generic import TemplateView

from main import scraping
from create_email import send_kadai_email
from check_deadline import check_deadline
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account.models import CustomUser

from datetime import datetime

@csrf_exempt
def cron_run(request):
    if request.method == 'GET':

        login_info_list = list(
            CustomUser.objects.exclude(login_id__isnull=True)\
            .exclude(login_password__isnull=True)\
            .exclude(email__isnull=True)\
            .exclude(email__exact='')\
            .exclude(notification=False)\
            .values_list('login_id','login_password','email')
        )
        for login_info in login_info_list:
            login_id = login_info[0]
            login_password = login_info[1]
            email_address = login_info[2]
            class_name_list,kadai_deadline_list= scraping(login_id, login_password)
            email_contents = check_deadline(class_name_list,kadai_deadline_list)
            if email_contents:
                send_kadai_email(email_address,email_contents)
        
        return JsonResponse({'status':'success'})
    
    return JsonResponse({'status':'invalid method'},status=405)


class HomeView(TemplateView):
    template_name = "core/home.html"

    def post(self, *args, **kwargs):

        # class_name_list,kadai_deadline_list,= scraping()
        # email_contents = check_deadline(class_name_list,kadai_deadline_list,)
        
        login_info_list = list(
            CustomUser.objects.exclude(login_id__isnull=True).exclude(login_password__isnull=True).exclude(email__isnull=True).exclude(email__exact='').exclude(notification=False).values_list('login_id','login_password','email')
        )
        print(login_info_list)
        for login_info in login_info_list:
            login_id = login_info[0]
            login_password = login_info[1]
            email_address = login_info[2]
            class_name_list,kadai_deadline_list= scraping(login_id, login_password)
            email_contents = check_deadline(class_name_list,kadai_deadline_list)
            if email_contents:
                send_kadai_email(email_address,email_contents)

        
        
        
        # if email_contents:
        #     auto_email(email_contents)
        
        return render(self.request, self.template_name)
    
