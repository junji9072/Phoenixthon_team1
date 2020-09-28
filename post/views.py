from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from. import models as post_models

# Create your views here.


#공지사항 관련

#공지사항 목록
def notice_list(request):
    posts = post_models.Post_notice.objects.all()
    return render(request, 'notice_list.html', {"posts":posts})

#공지사항 디테일
def notice_detail(request, post_id):
    post = post_models.Post_notice.objects.get(pk=post_id)
    return render(request, 'notice_detail.html', {"post":post})

#공지사항 생성
def notice_create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        notice = post_models.Post_notice()
        notice.title = request.POST['title']
        notice.content = request.POST['content']
        notice.user = request.user

        notice.save()
        return redirect('notice_list')
    else:
        return render(request, 'notice_create.html')

#공지사항 업데이트
def notice_update(request, post_id):
    myPost = post_models.Post_notice.objects.get(pk=post_id)
    if myPost.user != request.user:
        return redirect('login')
        
    if request.method == "POST":
        myPost.title = request.POST['title']
        myPost.content = request.POST['content']

        myPost.save()
        return redirect('notice_detail', post_id)
    else:
        return render(request, 'notice_update.html', {"myPost":myPost})

#공지사항 삭제
def notice_delete(request, post_id):
    myPost = post_models.Post_notice.objects.get(pk=post_id)
    myPost.delete()
    return redirect('notice_list')



#질문 관련

#질문 목록
def question_list(request):
    questions = post_models.Post_Question.objects.all()
    return render(request, 'question_list.html', {"questions":questions})

#질문 디테일
def question_detail(request, post_id):
    post = post_models.Post_Question.objects.get(pk=post_id)
    answers = post.post_answer_set.all()
    return render(request, 'question_detail.html', {"post":post, "answers":answers})

#질문 생성
def question_create(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        question = post_models.Post_Question()
        question.title = request.POST['title']
        question.content = request.POST['content']
        question.user = request.user

        question.save()
        return redirect('question_list')
    else:
        return render(request, 'question_create.html')

#질문 업데이트
def question_update(request, post_id):
    myPost = post_models.Post_Question.objects.get(pk=post_id)
    if myPost.user != request.user:
        return redirect('login')

    if request.method == "POST":
        myPost.title = request.POST['title']
        myPost.content = request.POST['content']

        myPost.save()
        return redirect('question_detail', post_id)
    else:
        return render(request, 'question_update.html', {"myPost":myPost})

#질문 삭제
def question_delete(request, post_id):
    myPost = post_models.Post_Question.objects.get(pk=post_id)
    myPost.delete()
    return redirect('question_list')



#답변 관련

#답변 생성
def answer_create(request, question_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        questionPost = post_models.Post_Question.objects.get(pk=question_id)

        answer = post_models.Post_Answer()
        answer.title = request.POST['title']
        answer.content = request.POST['content']
        answer.user = request.user
        answer.question = questionPost

        answer.save()
        return redirect('question_detail', question_id)
    else:
        return render(request, 'answer_create.html', {"question_id":question_id})

#답변 업데이트
def answer_update(request, question_id, answer_id):
    myPost = post_models.Post_Answer.objects.get(pk=answer_id)
    if myPost.user != request.user:
        return redirect('login')

    if request.method == "POST":
        myPost.title = request.POST['title']
        myPost.content = request.POST['content']

        myPost.save()
        return redirect('question_detail', question_id)
    else:
        return render(request, 'answer_update.html', {"myPost":myPost})

#답변 삭제
def answer_delete(request, question_id, answer_id):
    myPost = post_models.Post_Answer.objects.get(pk=answer_id)
    myPost.delete()
    return redirect('question_detail', question_id)
