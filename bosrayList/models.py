from django.db import models



class Participant(models.Model):
	name = models.CharField(max_length=50, default='')
	address = models.CharField(max_length=50, default='')
	email= models.EmailField(default='')
	
	def __str__(self):
		return self.name

class Profile(models.Model):
	participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
	age = models.CharField(max_length=50, default='')
	gender = models.CharField(max_length=50, default='')
	('M', 'Male'),('F', 'Female')
	numbers = models.CharField(max_length=64)
	team = models.CharField(max_length=64)
	kilometers = models.CharField(max_length=50, default='')

	def __str__(self):
		return self.name
	

class Program(models.Model):
    partcipant = models.ForeignKey(Participant, on_delete = models.CASCADE)
    eventtype = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=50, default='')
    details = models.CharField(max_length=50, default='')

    def __str__(self):
    	return self.name

class Location(models.Model):
	time_date = models.DateTimeField(null=True, blank=True)
	place = models.CharField(max_length=50, default='')

	def __str__(self):
		return self.name

class Feedback(models.Model):
    status_health = models.CharField(max_length=50,  default='')
    remarks = models.CharField(max_length=50, default='')



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
