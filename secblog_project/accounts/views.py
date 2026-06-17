from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from .models import User

def signup_page(request):
    return render(request, 'signup.html')

def signin_page(request):
    return render(request, 'login.html')

@csrf_exempt
def signup_api(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        User.objects.create(
            name=name,
            last_name=last_name,
            email=email,
            username=username,
            password=make_password(password)  
        )
        return JsonResponse({'success': True, 'message': 'Account created!'})
    
    return JsonResponse({'success': False, 'message': 'Error'})

@csrf_exempt
def signin_api(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')
        rememberMe = request.POST.get('rememberMe') == 'true'
        
        try:
            user = User.objects.get(email=identifier)
        except:
            try:
                user = User.objects.get(username=identifier)
            except:
                return JsonResponse({'success': False, 'message': 'User not found'})
        
        if check_password(password, user.password):
            request.session['user_id'] = user.id
            if rememberMe:
                request.session.set_expiry(1209600)  
            return JsonResponse({'success': True, 'message': 'Welcome back!'})
        else:
            return JsonResponse({'success': False, 'message': 'Wrong password'})
    
    return JsonResponse({'success': False, 'message': 'Error'})

@csrf_exempt
def logout_api(request):
    request.session.flush()
    return JsonResponse({'success': True, 'message': 'Logged out'})

@csrf_exempt 
def check_auth_api(request):
    if request.method == 'GET':
        if request.session.get('user_id'):
            return JsonResponse({
                'authenticated': True,
                'user': {
                    'id': request.session.get('user_id'),
                    'username': request.session.get('username'),
                    'fullname': request.session.get('fullname')
                }
            })
        return JsonResponse({'authenticated': False})
    return JsonResponse({'authenticated': False})