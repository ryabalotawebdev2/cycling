from django.db import models




class Participant(models.Model):
    name= models.CharField(max_length=50, default='')
    address = models.CharField(max_length=64)
    email = models.CharField(max_length=50, default='')
    number = models.CharField(max_length=50, default='')
   

    def __str__(self):
        return self.name

class Profile(models.Model):
    user01 = models.CharField(max_length=50, default='')
    email01 = models.EmailField(default='')
  

    def __str__(self):
        return self.name
	

class Program(models.Model):
    partcipant = models.ForeignKey(Participant, on_delete = models.CASCADE)
    your_kilometer = models.CharField(max_length=50, default='')
    catetype = models.CharField(max_length=50, default='')
    your_kilometer = models.CharField(max_length=50, default='')
    your_gender = models.CharField(max_length=50, default='')
    team = models.CharField(max_length=50, default='')
    yourage = models.CharField(max_length=50, default='')
    your_name = models.CharField(max_length=50, default='')
    
    def __str__(self):
    	return self.name

class Schedule(models.Model):
    partcipant = models.ForeignKey(Participant, on_delete = models.CASCADE)
    your_event = models.CharField(max_length=50, default='')
    your_place= models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

class Feedback(models.Model):
    feedback = models.CharField(max_length=50,  default='')
    
    def __str__(self):
    	return self.name

   

    









'''class join (models.Model):




class Last(models.Model):
    fullname = models.CharField(max_length=128)
    number  = models.ForeignKey(number, on_delete=models.CASCADE)
    place = models.OneToOneField( Place, on_delete=models.CASCADE, primary_key=True,)
    members = models.ManyToManyField(Person, through='Membership')

class accessories(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    height = models.CharField(choices=feet_cm,max_length=1)









class Male(models.Participants):
    def get_queryset(self):
        return super(Male, self).get_queryset().filter(sex='M')

class Female(models.Participants):
    def get_queryset(self):
        return super(Female, self).get_queryset().filter(sex='F')

class Person(models.Model):
    fullname = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=1,
                           choices=(
                                    ('M', 'Male'),  
                                    ('F', 'Female')
                           )
                           )
    people = models.Participants()
    men = Male()
    women = Female()'''
