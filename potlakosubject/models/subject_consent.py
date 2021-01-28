from django.db import models
from potlakosubject.models.choices import status, stay


class SubjectConsent(models.Model):

    marital_status = models.CharField(
        verbose_name='Are you single, married or divorced?',
        max_length=15,
        choices=status,
        blank=True,
        null=True, )

    stay_with = models.CharField(
        verbose_name='Who do you currently stay with?',
        max_length=15,
        choices=stay,
        blank=True,
        null=True,)

    wives = models.IntegerField(
        verbose_name='If wife, how many wives does your husband have (including traditional marriage), including '
                     'yourself??',
        blank=True,
        null=True, )

    husbands = models.IntegerField(
        verbose_name='How many wives do you have, including traditional marriage?',
        blank=True,
        null=True, )

    class Meta:
        verbose_name_plural = 'Subject Consent'




