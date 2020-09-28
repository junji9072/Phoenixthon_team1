from django.shortcuts import render,get_object_or_404,redirect
from .models import Civil_User, Soldier_User
from django.contrib import auth

# Create your views here

def add_my_soldier(request,civil_id,soldier_id):
  civil = get_object_or_404(Civil_User,pk=civil_id)
  civil.my_soldier.add(soldier_id)

  return redirect('home')


def delete_my_soldier(request,civil_id,soldier_id):
  civil = get_object_or_404(Civil_User,pk=civil_id)
  civil.my_soldier.remove(soldier_id)
  
  return redirect('home')

# 회원 가입
def soldier_signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = Soldier_User.objects.create_user(username=request.POST['username'], password=request.POST['password'],usertype=request.POST['usertype'],name=request.POST['name'],gender=request.POST['gender'],phone_number=request.POST['phone_number'],city=request.POST['city'],devision=request.POST['devision'],military_type=request.POST['military_type'],enter_date=request.POST['enter_date'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'sign_up_soldier.html')


def civil_signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = Civil_User.objects.create_user(username=request.POST['username'], password=request.POST['password'], usertype=request.POST['usertype'],name=request.POST['name'],gender=request.POST['gender'],phone_number=request.POST['phone_number'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'sign_up_ordinary.html')

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

# 로그 아웃
# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('home')
#     return render(request, 'home.html')

def signup_select(request):
  return render(request,'sign_up_select.html')