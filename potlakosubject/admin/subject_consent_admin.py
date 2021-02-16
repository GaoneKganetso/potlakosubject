from collections import OrderedDict

from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_consent.actions import (
    flag_as_verified_against_paper, unflag_as_verified_against_paper)
from edc_model_admin import (
    ModelAdminFormAutoNumberMixin, ModelAdminInstitutionMixin,
    audit_fieldset_tuple, audit_fields, ModelAdminNextUrlRedirectMixin,
    ModelAdminNextUrlRedirectError, ModelAdminReplaceLabelTextMixin)
from edc_model_admin import ModelAdminBasicMixin, ModelAdminReadOnlyMixin
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import potlako_subject_admin
from ..forms import SubjectConsentForm
from ..models import SubjectConsent


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminReplaceLabelTextMixin,
                      ModelAdminInstitutionMixin, ModelAdminReadOnlyMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

    def redirect_url(self, request, obj, post_url_continue=None):
        redirect_url = super().redirect_url(
            request, obj, post_url_continue=post_url_continue)
        if request.GET.dict().get('next'):
            url_name = request.GET.dict().get('next').split(',')[0]
            attrs = request.GET.dict().get('next').split(',')[1:]
            options = {k: request.GET.dict().get(k)
                       for k in attrs if request.GET.dict().get(k)}
            try:
                redirect_url = reverse(url_name, kwargs=options)
            except NoReverseMatch as e:
                raise ModelAdminNextUrlRedirectError(
                    f'{e}. Got url_name={url_name}, kwargs={options}.')
        return redirect_url


@admin.register(SubjectConsent, site=potlako_subject_admin)
class SubjectConsentAdmin(ModelAdminBasicMixin, ModelAdminMixin,
                          SimpleHistoryAdmin,
                          admin.ModelAdmin):

    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'subject_identifier',
                'marital_status',
                'stay_with',
                'wives',
                'husbands',
               )}),
        ('Review Questions', {
            'fields': (
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'verbal_script'),
            'description': (
                'The following questions are directed to the interviewer.')}),
        audit_fieldset_tuple)

    radio_fields = {
        'screening_identifier': admin.VERTICAL,
        'marital_status': admin.VERTICAL,
        'stay_with': admin.VERTICAL,
        'wives': admin.VERTICAL,
        'husbands': admin.VERTICAL}

    list_display = ('subject_identifier',
                    'marital_status',
                    'stay_with',
                    'wives',
                    'husbands')

    list_filter = ('marital_status',
                   'stay_with',
                   'wives')

    search_fields = ('subject_identifier', 'marital_status')







