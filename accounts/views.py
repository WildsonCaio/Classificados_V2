from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        check = auth.authenticate(request, username=user, password=password)
        if check is not None:
            auth.login(request, check)
            return redirect('home')
        else:
            messages.info(request, 'Usuário ou Senha incorretos.')
            return redirect('login')    
    else:
        return render(request, 'pages/login.html')

def user_logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        contact_1 = request.POST.get('contact_1')
        contact_2 = request.POST.get('contact_2')
        password = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        create_user = User.objects.create_user(username=username, first_name=contact_1, last_name=contact_2,
                                               password=password)
        messages.success(request, 'Cadastro realizado com sucesso.')
        return redirect('login')
    else:
        return render(request, 'pages/register.html')