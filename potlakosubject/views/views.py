# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
# def enrollment_view(request, enrollment_id):
# get enrollment with enrollment ID
# enrollment = Enrollment.objects.get(gender= enrollment_id )

# return render_to_response("enrollment/enrollment.html" , {
# 'enrollment: enrollment',
# }, RequestContext(request))

from django.contrib.sitemaps.views import index
from django.shortcuts import redirect, render
from django.template import RequestContext
from potlakosubject.forms.enrollmentform import EnrollmentForm


def enroll(request):
    # get the context from the request
    """context = RequestContext(request)"""

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)

        # is the form valid
        if form.is_valid():

            # save  the new category to the database
            form.save(commit=True)

            # Now call the index() view.The user will be shown the homepage.
            return index(request)
        else:
            print('error form invalid')
    # If the request was not a POST, display the form to enter details.
    else:
        form = EnrollmentForm
    return render(request, 'enrollment.html', {'form': form})



