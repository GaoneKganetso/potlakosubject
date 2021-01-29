# -*- coding: utf-8 -*-

from django.contrib import admin
from potlakosubject.models.enrollment import Enrollment
from potlakosubject.models.subject_consent import SubjectConsent
from potlakosubject.models.education import Education
from potlakosubject.models.community_engagement import CommunityEngagementQuestionnare


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('gender', 'citizenship', 'legally_married', 'marriage_certificate', 'literacy', 'minor')
    list_filter = ('gender', 'citizenship', 'legally_married', 'marriage_certificate', 'literacy', 'minor')

    fieldsets = (
        (None, {
            'fields': (
                'screening_identifier',
                'gender',
                'citizenship',
                'legally_married',
                'marriage_certificate',
                'minor',
                'literacy',)}
         ),)

    radio_fields = {
        'gender': admin.VERTICAL,
        'citizenship': admin.VERTICAL,
        'legally_married': admin.VERTICAL,
        'marriage_certificate': admin.VERTICAL,
        'minor': admin.VERTICAL,
        'literacy': admin.VERTICAL,
    }


@admin.register(SubjectConsent)
class SubjectConsentAdmin(admin.ModelAdmin):
    list_display = ('marital_status', 'stay_with', 'wives', 'husbands')
    list_filter = ('marital_status', 'stay_with')

    fieldsets = (
        (None, {
            'fields': (
                'marital_status',
                'stay_with',
                'wives',
                'husbands',)}
         ),)

    radio_fields = {
        'marital_status': admin.VERTICAL,
        'stay_with': admin.VERTICAL,

    }


@admin.register(CommunityEngagementQuestionnare)
class CommunityEngagementQuestionnareAdmin(admin.ModelAdmin):
    list_display = ('activeness', 'voting', 'problems', 'neighborhood')
    list_filter = ('activeness', 'voting', 'problems', 'neighborhood')

    fieldsets = (
        (None, {
            'fields': (
                'activeness',
                'voting',
                'problems',
                'neighborhood',)}
         ),)

    radio_fields = {
        'activeness': admin.VERTICAL,
        'voting': admin.VERTICAL,
        'problems': admin.VERTICAL,
        'neighborhood': admin.VERTICAL,

    }


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('work', 'type_of_work', 'recent_job', 'salary')
    list_filter = ('work', 'type_of_work', 'recent_job', 'salary')

    fieldsets = (
        (None, {
            'fields': (
                'work',
                'type_of_work',
                'recent_job',
                'salary',)}
         ),)

    radio_fields = {
        'work': admin.VERTICAL,
        'type_of_work': admin.VERTICAL,
        'recent_job': admin.VERTICAL,
        'salary': admin.VERTICAL,

    }
