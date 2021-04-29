from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request,'homepage.html',{'pet':request.POST.get('pet',''),'breed':request.POST.get('breed',''),'birthday':request.POST.get('birthday','')})

	#return render(request,'homepage.html',{'validEntry':request.POST.get('validEntry',''),'validNumber':request.POST.get('validNumber',''),'validDate':request.POST.get('validDate',''),})






#def homepage(request):
	#if request.method == 'POST':
		#Item.objects.create(text=request.POST['	peronEntry'])
		#return redirect('/')
	#items = Item.objects.all()
	#return render(request, 'homepage.html', {'newPerson': items})

