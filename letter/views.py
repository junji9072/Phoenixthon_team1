from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.core.paginator import Paginator
from .models import Letter
from users.models import Civil_User, Users, Soldier_User
from .forms import LetterForm,UpdateLetterForm
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def letter(request):
    """
    letter 조회 함수
    """
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/signin/')
    # letters = Letter.objects.filter(user_id=request.user.pk).order_by('created_at')
    letters = Letter.objects.all().order_by('created_at')
    context = {
        'letters': letters,
    }
    return render(request, 'letter.html', context)


#request.POST['user'] = request.user
#request.POST._mutable = True

def letter_create(request):
    """
    letter 생성
    """
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['civil_user'] = request.user
        # suser = request.user.Civil_User.my_soldier.all()
        # request.POST['soldier_user'] = suser[0]
        form = LetterForm(request.POST, request.FILES )
        if form.is_valid():
            # form.initial['soldier_user'] = form.civil_user.my_soldier[0]
            new_item = form.save()

        return HttpResponseRedirect("/letter")
    form = LetterForm(request.FILES)
    return render(request, 'letter_create.html', {'form': form})


def letter_update(request):
    """
    letter 수정
    """
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Letter, pk=request.POST.get('id'))
        form = UpdateLetterForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
    elif 'id' in request.GET:
        item = get_object_or_404(Letter, pk=request.GET.get('id'))
        form = LetterForm(instance=item)
        return render(request, 'letter_update.html', {'form': form})
    return HttpResponseRedirect("/letter")


def letter_delete(request, id):
    """
    letter 삭제
    """
    item = get_object_or_404(Letter, pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('letter')  # 리스트 화면으로 이동합니다.
    return render(request, 'letter_delete.html', {'item': item})