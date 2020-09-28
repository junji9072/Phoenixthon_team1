from django.shortcuts import render, redirect
from .models import Items

# Create your views here.
def tips(request):
    items = Items.objects.all()
    return render(request, 'tips.html', {'items' : items})

def cosmetics(request, id):
    return render(request, 'cosmetics.html')

def create(request):
    if request.method == 'POST':
        post = Items()

        if 'image' in request.FILES:
            post.image = request.FILES['image']
            post.name = request.FILES['name']
            post.description = request.FILES['description']

        post.save()

        return redirect('cosmetics', post.id)