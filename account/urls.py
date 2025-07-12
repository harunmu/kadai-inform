from django.urls import path
from .views import SignupView, SignupDoneView, LoginView, UserSettingView, LogoutView

app_name = 'account'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signup/done/', SignupDoneView.as_view(), name='signup_done'),
    path('login/', LoginView.as_view(), name="login"),
    path('setting/', UserSettingView.as_view(), name='setting'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
