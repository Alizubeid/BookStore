from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import Customer,Auther

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = "__all__"

class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = "__all__"

class AutherCreationForm(UserCreationForm):
    class Meta:
        model = Auther
        fields = "__all__"

class AutherChangeForm(UserChangeForm):
    class Meta:
        model = Auther
        fields = "__all__"