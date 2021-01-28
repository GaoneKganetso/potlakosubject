from django import forms
from potlakosubject.models.enrollment import Enrollment


# Create the form class
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'
