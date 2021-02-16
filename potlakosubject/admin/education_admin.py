from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.sites.admin import ModelAdminSiteMixin
from edc_metadata import NextFormGetter
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fields, audit_fieldset_tuple)

from .. import admin
# from ..admin_site import potlako_subject_admin
from potlakosubject.tests.admin_site import potlako_subject_admin
from potlakosubject.forms.education_form import EducationForm
from ..models import Education


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):
    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter


@admin.register(Education, site=potlako_subject_admin)
class EnrollmentAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = EducationForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'work',
                'type_of_work',
                'recent_job',
                'salary'
            )}),
        audit_fieldset_tuple)

    search_fields = ('subject_identifier', 'salary',)

    radio_fields = {
        'work': admin.VERTICAL,
        'type_of_work': admin.VERTICAL,
        'recent_job': admin.VERTICAL,
        'salary': admin.VERTICAL, }

    # def get_readonly_fields(self, request, obj=None):
    #  return (super().get_readonly_fields(request, obj=obj) + audit_fields +
    # ('citizenship',))
