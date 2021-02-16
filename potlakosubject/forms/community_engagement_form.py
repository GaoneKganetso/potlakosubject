from django import forms
from potlakosubject.models.community_engagement import CommunityEngagement


# Create the form class
class CommunityEngagementForm(forms.ModelForm):
    class Meta:
        model = CommunityEngagement
        fields = '__all__'
