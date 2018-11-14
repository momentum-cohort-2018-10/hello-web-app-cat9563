from django.shortcuts import render

def index(request):
    number = 6
    critter = "Yoshi bean"
    return render(request, 'index.html',{
        'number': number, 
        'critter': critter,
    })