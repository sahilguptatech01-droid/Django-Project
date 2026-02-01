from .models import Course
from django import forms

class AddForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=["title","price","image","instructor_name","summary"]