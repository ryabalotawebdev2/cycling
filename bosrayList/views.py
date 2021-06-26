from django.shortcuts import render, redirect
from django.http import HttpResponse
from bosrayList.models import Participant, Profile, Program, Schedule, Feedback

'''
def homepage(request):
   participants = Participant.objects.all()
   return render(request, 'homepage.html',{'participants': participants})

def homepage(request):
   participants = Participant.objects.all()
   return render(request, 'homepage.html',{'participants': participants})


def new_profile(request):
   newparticipant_ = Participant.objects.create(user=request.POST['_name_'],email=request.POST['_email_'])
   return redirect(f'/{newparticipant_.id}/view_profile')
    
def addpart_id(request, participant_id):
   participant_ = Participant.objects.get(id=participant_id)    
   Profile.objects.create(name=request.POST['name'],address=request.POST['address'],email=request.POST['email'],phonenumber=request.POST['number'], employee=employee_)
   return redirect(f'/{participant_.id}/view_profile') 
   
def view_profile(request, participant_id):
   participant_ = Participant.objects.get(id=participant_id)
   return render(request, 'registration.html', {'participant': participants_})'''


def home_page(request):
  #  profile = Profile.objects.all()
  participant = Participant.objects.all()
  return render(request, 'homepage.html',{'home_page':home_page})
def registrate(request):
  #  profile = Profile.objects.all(
  participant = Participant.objects.all()
  return render(request, 'registration.html',{'registrate':registrate})
def modelsss(request):
  #  profile = Profile.objects.all()
  participant = Participant.objects.all()
  return render(request, 'model3.html', {'modelsss' :modelsss})
def modelssss(request):
  #  profile = Profile.objects.all()
  participant = Participant.objects.all()
  return render(request, 'models4.html', {'modelssss' :modelssss})
def modelsssss(request):
  #  profile = Profile.objects.all()
  participant = Participant.objects.all()
  return render(request, 'models5.html',{'modelsssss' :modelsssss})
def contacts(request):
  #  profile = Profile.objects.all()
  participant = Participant.objects.all()
  return render(request, 'Contact.html', {'contacts' :contacts}) 
def abouts(request):
  #  profile = Profile.objects.all()
  participant = Participant.objects.all()
  return render(request, 'About.html', {'abouts' :abouts})      






'''
from django.shortcuts import redirect, render
from bosrayList.models import Participant, Profile, Program, Schedule, Feedback
from django.views.decorators.csrf import csrf_exempt


def home_page(request):  #1st model
      participant = Participant.objects.all()
      return render(request, 'homepage.html',{'home_page':home_page})
     #ibrgy ko foreign key ng 1st model ko sa 2nd model
     #IBrgy – 1st model
#BSMS.html – 1st html ko
def fullname(request):   :  #1st model
    
    fullname = Participant.objects.create(mncplty=request.POST['Municipality'],name=request.POST['Brgy'],bID=request.POST['BrgyID'])
    return redirect(f'/{newibrgy_.id}/')
#newibrgy – kahit ano
#IBrgy = 1st model , mncplty – attributes ng 1st model ko , Municipality – id ng 1st html 

def view_ibrgy(request, ibrgy_id):    2nd model
   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)
   return render(request, 'SInfo.html', {'ibrgy': ibrgy_})
#SInfo.html – 2nd html ko
   def add_info(request, ibrgy_id):    2nd model

   ibrgy_ = IBrgy.objects.get(id=ibrgy_id)    
   BResidents.objects.create(rlname=request.POST['addLN'],rfname=request.POST['addFN'],rmname=request.POST['addMN'],rrelation=request.POST['addRelation'],rjob=request.POST['addJob'],rnumber=request.POST['cnumber'],radd=request.POST['addadd'], ibrgy=ibrgy_)
  
   return redirect(f'{ibrgy_.id}/')    
#BResidents – 2nd model , rlname – attributes ng 2nd model ko , addln – id sa html  


def view_list(request, membership_id):
    participant_ =Participant.objects.get(id=participant_id)
    return render(request, 'registration.html', {'participant': participant_})


def new_list(request):
    participant_ = Participant.objects.create()
    #Membership.objects.create(
     #   name =request.POST['name'],
      #  address =request.POST['address'], 
      #  email =request.POST['email'], )
    return redirect(f'/bosrayList/{participant_.id}/')


def add_item(request, list_id):
    participantist_ = Participant.objects.get(id=participant_id)
    #Membership.objects.create(name=request.POST['name'],kilometer =request.POST['kilometer'],list=participant_)
    return redirect(f'/bosrayList/{participant_.id}/')




 def dataManipulation(request):
    vparticipant = Participant (name ="fullname", address ="brgy.", email="@gmail") 
    vparticipant.save()
    
    vvparticipant = Participant.objects.all()
    result ='Result of all entries in Participant model : <br>'
    for x in vvparticipant:
        res += x.name+'<br>'

    vvvparticipant = Participant.objects.get(id='1')
    res += 'Only one entry <br>'
    res += vvvparticipant.email
    
    res += '<br> Delete entry <br>'
    vvvparticipant.delete()
    
    vparticipant = Participant.objects.get(name = 'fullname' , address = 'brgy.', email = '@gmail')
    vparticipant.team="cnc"
    vparticipant.save()    
    res =""

    qs = Membership.objects.filter(name = 'fullname')
    res += "Found : %s results <br>" %len(qs)

    qs = Participant.objects.order_by('name')
    for x in qs:
        res += x.name + x.address +x.email'<br> 

'''
