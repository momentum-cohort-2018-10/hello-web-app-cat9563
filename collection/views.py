from django.shortcuts import render, redirect
from collection.forms import CatForm
from collection.models import Cat 

def index(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', {
        'cats': cats,
    })

def cat_detail(request, slug):
    cat = Cat.objects.get(slug=slug)
    return render(request, 'cats/cat_detail.html', {
        'cat': cat,
    })

def edit_cat(request, slug):
    cat = Cat.objects.get(slug=slug)
    form_class = CatForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_detail', slug=cat.slug)
    else:
        form = form_class(instance=cat)
    return render(request, 'cats/edit_cat.html', {
        'cat': cat,
        'form': form,
        })