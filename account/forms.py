from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

# from core.models import Cart

class SignupForm(UserCreationForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields["username"].widget.attrs.update({"class":"form-control"})
    #     self.fields["password1"].widget.attrs.update({"class":"form-control"})
    #     self.fields["password2"].widget.attrs.update({"class":"form-control"})
    #     #fieldは各フィールド情報を持っていて辞書型
    #     #widgetはInputタグに関する情報を
    #     #attrsはinputの属性に関する情報を持つ


    # def save(self):
    #     user = super().save(commit=False) #saveメソッドのオーバーライド
    #     user.cart = Cart.objects.create()
    #     user.save()
    #     return user

    class Meta:
        model = User
        fields = ('username',) #パスワード以外の表示したい項目を記述