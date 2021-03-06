from django.db import models
# Create your models here.
class Student(models.Model):
    father_choice = (("Teacher", "Teacher"), ("Professor", "Professor"),
                     ("Businessman", "Businessman"), ("Sciencist", "Sciencist"), ("Farmer", "Farmer"), ("NGO", "NGO"), ("Banker", "Banker"), ('Others', 'Others'),)

    mother_choice = (("Teacher", "Teacher"), ("Professor", "Professor"),
                     ("Businessman", "Businessman"), ("Sciencist", "Sciencist"), ("Housewife", "Housewife"), ("NGO", "NGO"), ("Banker", "Banker"), ('Others', 'Others'),)

    blood_group = (('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+',
                   'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'), ('Others', 'Others'),)

    religion_group = (('Islam', 'Islam'), ('Christan', 'Chirstan'),
                      ('Hindu', 'Hindu'), ('Buddho', 'Buddho'), ('Others', 'Others'),)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100, choices=father_choice)
    mother_occupation = models.CharField(max_length=100, choices=mother_choice)
    date_of_birth = models.DateField(max_length=10)
    gernder = models.CharField(max_length=20, choices=(
        ("male", "male"), ("female", "female")))
    course = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    blood_group = models.CharField(max_length=10, choices=blood_group)
    religion = models.CharField(max_length=50, choices=religion_group)
    profile_img = models.ImageField(upload_to='assets/images')
    def __str__(self):
        return self.first_name+' '+self.last_name
