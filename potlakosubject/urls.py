from .views import views
from django.urls import path


urlpatterns = patterns = [

    path('enroll/', views.enroll),

]
