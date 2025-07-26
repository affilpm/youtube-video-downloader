import random
from django.core.cache import cache
from django.core.mail import send_mail 

OTP_EXPIRY_SECONDS = 300

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_mail(email, otp):
    subject = 'your otp for registration'
    message = f'your otp for registraion is {otp}'
    send_mail(subject, message, None, [email], fail_silently=False)
    
def store_otp(email, data):
    otp = generate_otp()
    cache.set(f'otp_{email}', {
        'otp': otp,
        'form_data': data,
    }, timeout=OTP_EXPIRY_SECONDS)
    send_otp_mail(email, otp)
    return otp

def get_otp_data(email):
    return cache.get(f'otp_{email}')

def delete_otp(email):
    cache.delete(f'otp_{email}')
    
def update_otp(email):
    data = get_otp_data(email)
    if data:
        new_otp = generate_otp()
        data['otp'] = new_otp
        cache.set(f'otp_{email}', data, timeout=OTP_EXPIRY_SECONDS)
        send_otp_mail(email, new_otp)
        return new_otp
    return None   
      
