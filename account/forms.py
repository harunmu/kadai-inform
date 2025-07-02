from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

# from core.models import Cart

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','login_id','login_password') #パスワード以外の表示したい項目を記述

class UserUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'login_id', 'login_password', 'is_notification')