from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
import json
from urllib.parse import urlencode  # python 3
# from urllib import urlencode      # python 2
import requests

def index(request):
    form = NameForm(request.POST)
    if request.method == 'POST':
        labels_raw = ""
        data_raw = ""
        data = ""
        labels = ""
        types = ""
        formats = ""
        form = NameForm(request.POST)
        if form.is_valid():
            print(request.POST)
            labels_raw = (request.POST)['labels']
            labels = list(map(str,labels_raw.split(",")))
            data_raw = (request.POST)['data']
            data = list(map(int,data_raw.split(",")))
            types = (request.POST)['types']
            formats = (request.POST)['formats']
            print(labels)
            print(data)
            config = {
                "type": types,
                "data": {
                    "labels": labels,   #Set X-axis labels
                    "datasets": [{
                        "label": 'Users',                         # Create the 'Users' dataset
                        "data": data           # Add data to the chart
                    }]
                }
            }
            postdata = {
                'chart': json.dumps(config),
                'width': 500,
                'height': 300,
                'format' : formats,
                'backgroundColor': 'transparent',
            }
            
            resp = requests.post('https://quickchart.io/chart/create', json=postdata)
            parsed = json.loads(resp.text)
            my_url = parsed['url']
            print(my_url)
            context = {'my_url' : my_url, 'format' : formats}
            return render(request, 'chartapp/output.html',context)
        form = NameForm()

    return render(request, 'chartapp/index.html', {'form': form})