from django.shortcuts import render, redirect
from django.http import HttpResponse
from bosrayList.models import Participant, Membership, Event, Location, Status


def home_page(request):
    membership = Membership.objects.all()
    return render(request, 'homepage.html',{'membership' : membership})
    


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


'''def dataManipulation(request):
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
        res += x.name + x.address +x.email'<br>'''


