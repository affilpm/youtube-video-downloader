from django.shortcuts import render, redirect
from .forms import RegisterForm
from .utils.otp import store_otp, get_otp_data, delete_otp, update_otp
from django.contrib import messages 
from .models import CustomUser

def registerview(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            otp = store_otp(email, form.cleaned_data)
            
            print(f'{email}:{otp}')
            
            return redirect('verify_otp', email=email)
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})        
            
def verify_otp_view(request, email):
    if request.method == 'POST':
        input_otp = request.POST.get('otp')
        otp_data = get_otp_data(email)
        
        if otp_data and otp_data['otp'] == input_otp:
            data = otp_data['form_data']
            CustomUser.object.create_user(
                email = email,
                username = data['username'],
                first_name = data['first_name'],
                last_name = data['last_name'],
                password = data['password1']
            )
            delete_otp(email)
            messages.success(request, 'Account created successfully.')
            # return redirect('login')
        else:
            messages.error(request, 'Invalide otp or expired otp.')
    return render(request, 'users/verify_otp.html', {'email': email})  
    
def resend_otp_view(request, email):
    new_otp = update_otp(email)
    if new_otp:
        print(f'{email}:{new_otp}')    
        messages.info(request, 'A new otp has been sent to your email.')
    else:
        messages.error(request, 'Could not resend OTP. Try regestering again')
    return redirect('verify_otp', email=email)        
                    