from django.shortcuts import render
from collection.models import Cat 

def index(request):
    cats = Cat.objects.all()
    return render(request, 'index.html', {
        'cats': cats,
    })

# Right now it’s essentially saying: “When the index page is viewed, display this template and pass along these two variables.”

# def index(request):
#     number = 6
#     critter = "Yoshi bean"
#     return render(request, 'index.html',{
#         'number': number, 
#         'critter': critter,
#     })