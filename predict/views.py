
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Client
from django.urls import reverse

# Create your views here.
def index(request):
    Client_list = Client.objects.order_by('client_name')[:5]
    context = {
        'Client_list': Client_list
    }
    return render(request, 'index.html', context)

def detail(request, Client_id):
    client = get_object_or_404(Client, pk=Client_id)
    context = {
        'client': client
    }
    return render(request, 'detail.html', context)

def result(request, Client_id):
    client = get_object_or_404(Client, pk=Client_id)
    return render(request, 'result.html', {'client': client})

def pred(request, Client_id):
    import numpy as np
    import pickle
    import pandas as pd

    client = get_object_or_404(Client, pk=Client_id)

 
    filePath2 = 'model.pkl'
    post_list = ['연간소득', '직업유형', '가족수', '나이', '연차', '카드발급년수']
    values = []

    model = pickle.load(open(filePath2, 'rb'))

    for post in post_list:
        values.append(float(request.POST[post]))

    power = (values[4]/((values[-3]*365)+(values[-2]*365)))/130

    f_income = np.log((values[4]/ values[-4])/130)

    values.append(power)
    values.append(f_income)
    values[2]= np.log(values[2])

    input_features = pd.Series(values,index=['연간소득', '직업유형', '가족수', '나이', '연차', '카드발급년수']) 
    input_features_df = pd.DataFrame(input_features)
    input_features_df_T = input_features_df.T
    client.grade =  model.predict(input_features_df_T)
    client.save()

    return HttpResponseRedirect(reverse('predict:result', args=(client.id,)))