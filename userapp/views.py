from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST' and request.POST['username'] != '' and request.POST['password'] != '':
        if request.POST['password'] == request.POST['con_password']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error':'해당 아이디가 이미 존재합니다'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'signup.html', {'error':'비밀번호와 비밀번호 확인이 일치하지 않습니다'})
    return render(request, 'signup.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(request, username=name, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'이름 또는 비밀번호를 확인해주세요'})

def logout(request):

    auth.logout(request)

    return redirect('/')

