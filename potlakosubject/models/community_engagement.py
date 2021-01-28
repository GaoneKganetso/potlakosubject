from django.db import models
from potlakosubject.models.choices import active, problem, neighbor, vote


class CommunityEngagementQuestionnare(models.Model):
    activeness = models.CharField(
        verbose_name='How active are you in community activities such as burial society, Motshelo, Syndicate, PTA, '
                     'VDC(Village Development Committee), Mophato and development of the community that surrounds '
                     'you?',
        max_length=50,
        choices=active,
        null=True,
        blank=True
    )

    voting = models.CharField(
        verbose_name='Did you vote in the last local government election?',
        max_length=25,
        choices=vote,
        null=True,
        blank=True,
    )

    problems =  models.CharField(
        verbose_name='What are the major problems in this neighborhood?',
        max_length=25,
        choices=problem,
        null=True,
        blank=True,
        #other specify
    )

    neighborhood = models.CharField(
        verbose_name='If there is a problem in this neighborhood, do the adults work together in solving it?',
        max_length=25,
        choices=neighbor,
        null=True,
        blank=True,

    )

