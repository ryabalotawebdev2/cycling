from django.shortcuts import render, redirect
from django.http import HttpResponse
from bosrayList.models import Item, List


def home_page(request):
    items = Item.objects.all()
    return render(request, 'homepage.html',{'items' : items})
    


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'registration.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(email =request.POST['email'],fullname =request.POST['fullname'], list=list_)
    return redirect(f'/bosrayList/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    #para sa 1st item ng 2nd html
    Item.objects.create(name=request.POST['name'],kilometer =request.POST['kilometer'],list=list_)
    return redirect(f'/bosrayList/{list_.id}/')




