from django.urls.conf import path
from django.views.generic.base import RedirectView

from potlakosubject.tests.admin_site import potlako_subject_admin


app_name = 'potlako_subject'

urlpatterns = patterns = [
    path('admin/', potlako_subject_admin.urls),
    path('', RedirectView.as_view(url='admin/'), name='home_url'),
]

# [ path('enroll/', views.enroll), ]
