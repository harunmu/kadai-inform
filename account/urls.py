from django.urls import path
from .views import * 

app_name = 'account'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signup/done/', SignupDoneView.as_view(), name='signup_done'),
]
