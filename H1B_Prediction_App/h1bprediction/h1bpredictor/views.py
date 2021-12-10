from django.shortcuts import render
from .forms import *
import numpy as np

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.conf import settings
import pickle

# ['CASE_STATUS', 'EMPLOYER_NAME', 'EMPLOYER_STATE', 'SOC_CODE',
#        'NAICS_CODE', 'NEW_EMPLOYMENT', 'CONTINUED_EMPLOYMENT',
#        'CHANGE_PREVIOUS_EMPLOYMENT', 'NEW_CONCURRENT_EMPLOYMENT',
#        'CHANGE_EMPLOYER', 'AMENDED_PETITION', 'FULL_TIME_POSITION',
#        'H1B_DEPENDENT', 'WORKSITE_STATE', 'WILLFUL_VIOLATOR', 'SUPPORT_H1B',
#        'Total_Wage']


def getPrediction(AMENDED_PETITION, CHANGE_EMPLOYER, CHANGE_PREVIOUS_EMPLOYMENT,
                  CONTINUED_EMPLOYMENT,EMPLOYER_NAME, EMPLOYER_STATE,
       FULL_TIME_POSITION, H1B_DEPENDENT, NAICS_CODE,
       NEW_CONCURRENT_EMPLOYMENT, NEW_EMPLOYMENT, SOC_CODE,
       SUPPORT_H1B, Total_Wage, WILLFUL_VIOLATOR, WORKSITE_STATE):

    transformed_EmpName = settings.EMP_NAME_LE.transform([EMPLOYER_NAME])
    transformed_EmpState = settings.EMP_STATE_LE.transform([EMPLOYER_STATE])
    transformed_NaicsCode = settings.NAICS_CODE_LE.transform([NAICS_CODE])
    transformed_SocCode = settings.SOC_CODE_LE.transform([SOC_CODE])
    transformed_WorkState = settings.WORKSTATE_LE.transform([WORKSITE_STATE])

    EMPLOYER_NAME = transformed_EmpName
    EMPLOYER_STATE = transformed_EmpState
    SOC_CODE = transformed_SocCode
    NAICS_CODE = transformed_NaicsCode
    WORKSITE_STATE = transformed_WorkState

    single=np.array([[AMENDED_PETITION, CHANGE_EMPLOYER, CHANGE_PREVIOUS_EMPLOYMENT, CONTINUED_EMPLOYMENT, EMPLOYER_NAME,
      EMPLOYER_STATE, FULL_TIME_POSITION, H1B_DEPENDENT, NAICS_CODE, NEW_CONCURRENT_EMPLOYMENT, NEW_EMPLOYMENT,
      SOC_CODE, SUPPORT_H1B, Total_Wage, WILLFUL_VIOLATOR, WORKSITE_STATE]])

    prediction = settings.NN_MODEL.predict(single)
    return prediction


def index(request):
    if request.method == 'POST':
        form = PredictionsForm(request.POST)
        print(form.is_valid(),form.errors)
        if form.is_valid():
            EMPLOYER_NAME=form.cleaned_data.get('EMPLOYER_NAME')
            EMPLOYER_STATE = form.cleaned_data.get('EMPLOYER_STATE')
            SOC_CODE = form.cleaned_data.get('SOC_CODE')
            NAICS_CODE = form.cleaned_data.get('NAICS_CODE')
            NEW_EMPLOYMENT = form.cleaned_data.get('NEW_EMPLOYMENT')
            CONTINUED_EMPLOYMENT = form.cleaned_data.get('CONTINUED_EMPLOYMENT')
            CHANGE_PREVIOUS_EMPLOYMENT = form.cleaned_data.get('CHANGE_PREVIOUS_EMPLOYMENT')
            NEW_CONCURRENT_EMPLOYMENT = form.cleaned_data.get('NEW_CONCURRENT_EMPLOYMENT')
            CHANGE_EMPLOYER = form.cleaned_data.get('CHANGE_EMPLOYER')
            AMENDED_PETITION = form.cleaned_data.get('AMENDED_PETITION')
            FULL_TIME_POSITION = form.cleaned_data.get('FULL_TIME_POSITION')
            H1B_DEPENDENT = form.cleaned_data.get('H1B_DEPENDENT')
            WORKSITE_STATE = form.cleaned_data.get('WORKSITE_STATE')
            WILLFUL_VIOLATOR = form.cleaned_data.get('WILLFUL_VIOLATOR')
            SUPPORT_H1B = form.cleaned_data.get('SUPPORT_H1B')
            Total_Wage = form.cleaned_data.get('Total_Wage')
            # model.predit()
            print([EMPLOYER_NAME, EMPLOYER_STATE, SOC_CODE, NAICS_CODE, NEW_EMPLOYMENT, CONTINUED_EMPLOYMENT,CHANGE_PREVIOUS_EMPLOYMENT, NEW_CONCURRENT_EMPLOYMENT,CHANGE_EMPLOYER, AMENDED_PETITION, FULL_TIME_POSITION, H1B_DEPENDENT, WORKSITE_STATE, WILLFUL_VIOLATOR, SUPPORT_H1B,Total_Wage])

            prediction = getPrediction(AMENDED_PETITION=AMENDED_PETITION,
                                       CHANGE_EMPLOYER=CHANGE_EMPLOYER,
                                       CHANGE_PREVIOUS_EMPLOYMENT=CHANGE_PREVIOUS_EMPLOYMENT,
                                       CONTINUED_EMPLOYMENT=CONTINUED_EMPLOYMENT,
                                       EMPLOYER_NAME=EMPLOYER_NAME,
                                       EMPLOYER_STATE=EMPLOYER_STATE,
                                       FULL_TIME_POSITION=FULL_TIME_POSITION,
                                       H1B_DEPENDENT=H1B_DEPENDENT,
                                       NAICS_CODE=NAICS_CODE,
                                       NEW_CONCURRENT_EMPLOYMENT=NEW_CONCURRENT_EMPLOYMENT,
                                       NEW_EMPLOYMENT=NEW_EMPLOYMENT,
                                       SOC_CODE=SOC_CODE,
                                       SUPPORT_H1B=SUPPORT_H1B,
                                       Total_Wage=Total_Wage,
                                       WILLFUL_VIOLATOR=WILLFUL_VIOLATOR,
                                       WORKSITE_STATE=WORKSITE_STATE)
            print('Predictionnnnnnnnnn', prediction)
        # return JsonResponse({'success': True})
            if prediction[0]==0:
                text='Possibility of H1b getting denied'
            else:
                text = 'Possibility of H1b getting Approved'
            response={'prediction': str(prediction[0]),'text':text}
            return render(request, 'prediction.html', response)
    else:
        form = PredictionsForm()
        context = {'form': form }
        print(context)
        return render(request, 'index.html', context)
