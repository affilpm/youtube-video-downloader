from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser 

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']
        
class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)
    
    
    
    