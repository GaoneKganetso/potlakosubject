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
from potlakosubject.forms.community_engagement_form import CommunityEnagementForm
from ..models import Community_Engagement


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


@admin.register(Community_Engagement, site=potlako_subject_admin)
class EnrollmentAdmin(ModelAdminMixin, admin.ModelAdmin):
    form = CommunityEnagementForm

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'activeness',
                'voting',
                'problems',
                'neighborhood'
            )}),
        audit_fieldset_tuple)

    search_fields = ('subject_identifier', 'activeness',)

    radio_fields = {
        'activeness': admin.VERTICAL,
        'voting': admin.VERTICAL,
        'problems': admin.VERTICAL,
        'neighborhood': admin.VERTICAL, }

    # def get_readonly_fields(self, request, obj=None):
    #  return (super().get_readonly_fields(request, obj=obj) + audit_fields +
    # ('citizenship',))
