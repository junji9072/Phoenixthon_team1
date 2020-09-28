from django.shortcuts import render,get_object_or_404
from users import models as usermodels
from post import models as postmodels

def home(request):
    notices = postmodels.Post_notice.objects.all()
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'home.html')
        current_user = get_object_or_404(usermodels.Civil_User,pk = request.user.id)
        soldiers = current_user.my_soldier.all()
        return render(request, 'home.html',{'soldiers':soldiers,'notices':notices})
    return render(request, 'home.html',{'notices':notices})

def mypage(request):
    soldiers = usermodels.Soldier_User.objects.all()
    civils = usermodels.Civil_User.objects.all()
    return render(request, 'mypage.html',{'soldiers':soldiers,'civils':civils})

def add_soldier(request):
    current_user = get_object_or_404(usermodels.Civil_User,pk = request.user.id)
    all_soldiers = usermodels.Soldier_User.objects.all()
    in_soldiers = current_user.my_soldier.all()
    
    soldiers = list(set(all_soldiers) - set(in_soldiers))

    civils = usermodels.Civil_User.objects.all()
    return render(request, 'add_soldier.html',{'soldiers':soldiers,'civils':civils})