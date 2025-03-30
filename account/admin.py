from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model() #CustomUserを呼び出す
admin.site.register(User)