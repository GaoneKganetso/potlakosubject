from django import forms
from potlakosubject.models.education import Education


# Create the form class
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
