
from dataclasses import fields
from django import forms


from core.models import Student
# Create your models here.


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        """ fields=['first_name']
        widget = {'first_name':forms.TextInput(attrs={'class':'profileInputBox'})} """