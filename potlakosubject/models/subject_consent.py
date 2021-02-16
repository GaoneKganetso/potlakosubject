from django.db import models
from potlakosubject.models.choices import status, stay

from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_identifier.subject_identifier import SubjectIdentifier
from edc_registration.model_mixins import (
    UpdatesOrCreatesRegistrationModelMixin)

from edc_consent.field_mixins import CitizenFieldsMixin
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.managers import ConsentManager as SubjectConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_consent.validators import eligible_if_yes
from edc_search.model_mixins import SearchSlugManager
from edc_sms.models import SubjectRecipientModelMixin

from ..choices import IDENTITY_TYPE
from .clinician_call_enrollment import ClinicianCallEnrollment
from .model_mixins import SearchSlugModelMixin


class ConsentManager(SubjectConsentManager, SearchSlugManager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)

    class Meta:
        abstract = True


class SubjectConsent(ConsentModelMixin, SiteModelMixin, SubjectRecipientModelMixin,
                     UpdatesOrCreatesRegistrationModelMixin,
                     NonUniqueSubjectIdentifierModelMixin,
                     IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
                     CitizenFieldsMixin, SearchSlugModelMixin, BaseUuidModel, models.Model):

    subject_screening_model = 'potlako_subject.subjectscreening'

    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        null=True,
        blank=True,
        max_length=50)

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
        null=True, )

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

    consent = SubjectConsentManager()

    objects = ConsentManager()

    on_site = CurrentSiteManager()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.subject_type = 'subject'
        self.version = '1'

    def natural_key(self):
        return (self.subject_identifier, self.version,)

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend(['identity', 'screening_identifier',
                       'first_name', 'last_name'])
        return fields

    def make_new_identifier(self):
        """Returns a new and unique identifier.
        Override this if needed.
        """
        subject_identifier = SubjectIdentifier(
            identifier_type='subject',
            requesting_model=self._meta.label_lower,
            site=self.site)
        return subject_identifier.identifier

    @property
    def consent_version(self):
        return self.version

    class Meta(ConsentModelMixin.Meta):
        app_label = 'potlakosubject'
        get_latest_by = 'consent_datetime'
        unique_together = (('subject_identifier', 'version'),
                           ('first_name', 'dob', 'initials', 'version'))
        ordering = ('-created',)
