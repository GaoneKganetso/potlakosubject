# -*- coding: utf-8 -*-
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugModelMixin

from potlakosubject.eligibility import Eligibility
from potlakosubject.models.choices import yes_no, gender, literacy


# create your models here
# class Enrollment(models.Model):

class Enrollment(NonUniqueSubjectIdentifierFieldMixin,
                 SiteModelMixin, SearchSlugModelMixin, BaseUuidModel):
    eligibility_checklist = Eligibility

    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        max_length=36,
        unique=True,
        # default=None
    )

    gender = models.CharField(
        verbose_name='Gender ',
        choices=gender,
        blank=False,
        null=False,
        max_length=10)

    citizenship = models.CharField(
        verbose_name='Citizen of Botswana?',
        choices=yes_no,
        null=True,
        blank=True,
        max_length=5)

    legally_married = models.CharField(
        verbose_name='Legally married to a Botswana Citizen?',
        choices=yes_no,
        null=True,
        blank=True,
        max_length=5)

    marriage_certificate = models.CharField(
        verbose_name='Has the participant produced marriage certificate as proof?',
        choices=yes_no,
        null=True,
        blank=True,
        max_length=5)

    literacy = models.CharField(
        verbose_name='Is the participant literate or illiterate ?If illiterate is there a witness available?',
        choices=literacy,
        null=True,
        blank=True,
        max_length=50)

    minor = models.CharField(
        verbose_name='If minor, is there a guardian available?',
        choices=yes_no,
        null=True,
        blank=True,
        max_length=5)

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Enrollment'
