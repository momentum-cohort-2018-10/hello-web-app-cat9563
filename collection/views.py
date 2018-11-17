from django.shortcuts import render, redirect
from collection.forms import CatForm
from collection.models import Cat
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from django.http import Http404

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

@login_required
def edit_cat(request, slug):
    # grab the object...
    cat = Cat.objects.get(slug=slug)

    # grab the current logged in user and make sure they're the owner of the cat
    if cat.user != request.user:
        raise Http404

    # set the form we're using...
    form_class = CatForm

    # if we're coming to this view from a submitted form,
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=cat)

        if form.is_valid():
            # save the new data
            form.save()
            return redirect('cat_detail', slug=cat.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=cat)

    # and render the template
    return render(request, 'cats/edit_cat.html', {
        'cat': cat,
        'form': form,
    })

# @login_required
# def edit_cat(request, slug):
#     cat = Cat.objects.get(slug=slug)
#     if cat.user != request.user:
#         raise Http404
#     form_class = CatForm
#     if request.method == 'POST':
#         form = form_class(data=request.POST, instance=cat)
#         if form.is_valid():
#             form.save()
#             return redirect('cat_detail', slug=cat.slug)
#         else:
#             form = form_class(instance=cat)

#         return render(request, 'cats/edit_cat.html', {
#             'cat': cat,
#             'form': form,
#         })

def create_cat(request):
    form_class = CatForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.user = request.user
            cat.slug = slugify(cat.name)
            cat.save()
            return redirect('cat_detail', slug=cat.slug)
    else:
        form = form_class()
    return render(request, 'cats/create_cat.html', {
            'form': form,
    })