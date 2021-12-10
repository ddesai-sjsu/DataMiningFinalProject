from django.db import models
from django.conf import settings

# ['CASE_STATUS', 'EMPLOYER_NAME', 'EMPLOYER_STATE', 'SOC_CODE',
#        'NAICS_CODE', 'NEW_EMPLOYMENT', 'CONTINUED_EMPLOYMENT',
#        'CHANGE_PREVIOUS_EMPLOYMENT', 'NEW_CONCURRENT_EMPLOYMENT',
#        'CHANGE_EMPLOYER', 'AMENDED_PETITION', 'FULL_TIME_POSITION',
#        'H1B_DEPENDENT', 'WORKSITE_STATE', 'WILLFUL_VIOLATOR', 'SUPPORT_H1B',
#        'Total_Wage']
# Create your models here.
# x=[]
# for i in whatevr:
#     x.append((i,i))


class Predictions(models.Model):
    EMPLOYER_NAME  = models.CharField(max_length=200, choices=settings.EMP_NAMES_CHOICES[:1500])
    EMPLOYER_STATE = models.CharField(max_length=200, choices=settings.EMP_STATE_CHOICES)
    SOC_CODE  = models.CharField(max_length=200, choices=settings.SOC_CODE_CHOICES)
    NAICS_CODE  = models.CharField(max_length=200, choices=settings.NAICS_CODE_CHOICES)
    NEW_EMPLOYMENT  = models.BooleanField(default=0,)
    CONTINUED_EMPLOYMENT  = models.BooleanField(default=0)
    CHANGE_PREVIOUS_EMPLOYMENT  = models.BooleanField(default=0)
    NEW_CONCURRENT_EMPLOYMENT  = models.BooleanField(default=0)
    CHANGE_EMPLOYER  = models.BooleanField(default=0)
    AMENDED_PETITION  = models.BooleanField(default=0)
    FULL_TIME_POSITION  = models.BooleanField(default=0)
    H1B_DEPENDENT  = models.BooleanField(default=0)
    WORKSITE_STATE  =  models.CharField(max_length=200, choices=settings.WORKSITE_STATE_CHOICES)
    WILLFUL_VIOLATOR  = models.BooleanField(default=0)
    SUPPORT_H1B  = models.BooleanField(default=0)
    Total_Wage = models.IntegerField(default=100000)
