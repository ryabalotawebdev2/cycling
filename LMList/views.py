from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request,'homepage.html',{'new_item_text':request.POST.get('owner',''),})






#def homepage(request):
	#if request.method == 'POST':
		#Item.objects.create(text=request.POST['	peronEntry'])
		#return redirect('/')
	#items = Item.objects.all()
	#return render(request, 'homepage.html', {'newPerson': items})

