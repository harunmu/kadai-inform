from django.shortcuts import render
from django.views.generic import TemplateView

from main import scraping
from craft_mail import auto_email
from check_deadline import check_deadline
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account.models import CustomUser

from datetime import datetime

@csrf_exempt
def cron_run(request):
    if request.method == 'GET':
            
        class_name_list,kadai_deadline_list= scraping()
        email_contents = check_deadline(class_name_list,kadai_deadline_list)
        
        if email_contents:
            auto_email(email_contents)
        
        return JsonResponse({'status':'success'})
    
    return JsonResponse({'status':'invalid method'},status=405)


class HomeView(TemplateView):
    template_name = "core/home.html"

    def post(self, *args, **kwargs):

        # class_name_list,kadai_deadline_list,= scraping()
        # email_contents = check_deadline(class_name_list,kadai_deadline_list,)
        
        login_info = list(
            CustomUser.objects.exclude(login_id__isnull=True).exclude(login_password__isnull=True).values_list('login_id','login_password')
        )
        login_id = login_info[0][0]
        login_password = login_info[0][1]
        scraping(login_id, login_password)
        print('success')

        
        
        
        # if email_contents:
        #     auto_email(email_contents)
        
        return render(self.request, self.template_name)
    
