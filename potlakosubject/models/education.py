from django.db import models
from potlakosubject.models.choices import yes_no, job_type,jobs,money


class Education(models.Model):
    work = models.CharField(
        verbose_name='Are you currently working?',
        max_length=5,
        choices=yes_no,
        blank=True,
        null=True, )

    type_of_work = models.CharField(
        verbose_name='In your main job what type of work do you do?',
        max_length=50,
        choices=job_type,
        blank=True,
        null=True, )

    recent_job = models.CharField(
        verbose_name='Describe the work that you do or did in your most recent job. If you have more than one '
                     'profession, choose the one you spend the most time doing',
        max_length=100,
        choices=jobs,
        blank=True,
        null=False, )

    salary = models.CharField(
        verbose_name='n the past month, how much money did you earn from work you did or received in payment?',
        max_length=100,
        choices=money,
        blank=True,
        null=False,
    )

    class Meta:
        verbose_name_plural = 'Education'
