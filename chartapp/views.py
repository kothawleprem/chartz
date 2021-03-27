from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
import json
from urllib.parse import urlencode  # python 3
# from urllib import urlencode      # python 2
import requests
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


my_url =""
def index(request):
    form = NameForm(request.POST)
    if request.method == 'POST':
        labels_raw = ""
        data_raw = ""
        data = ""
        labels = ""
        types = ""
        formats = ""
        text = ""
        toemail = "" 
        name = ""
        form = NameForm(request.POST)
        if form.is_valid():
            try:
                text = (request.POST)['qrcode']
                if len(text)>1:
                    context = {'text' : text}
                    return render(request, 'chartapp/output.html',context)
            except:
                print("")
            else:
                # try:
                labels_raw = (request.POST)['labels']
                labels = list(map(str,labels_raw.split(",")))
                data_raw = (request.POST)['data']
                data = list(map(int,data_raw.split(",")))
                formats = (request.POST)['formats']
                types = (request.POST)['types']
                toemail = request.POST.get('toemail')
                name = request.POST.get('name')
                config = {
                    "type": types,
                    "data": {
                        "labels": labels,   #Set X-axis labels
                        "datasets": [{
                            "label": name,                         # Create the 'Users' dataset
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

                context = {'my_url' : my_url, 'format' : formats, 'text' : text}

                subject, from_email, to = 'Your Chart From ChartBay has Arrived!!!', settings.EMAIL_HOST_USER,toemail
                text_content = 'Chart Sent Successfully'
                if formats == "png":
                    html_content = f"<h3> Your Chart is Ready!! </h3> <img src='{my_url}'/><h4>Here's the url:<a href='{my_url}'>{my_url}</a></h4><h4> Do Share with your Friends: <a href='https://chartbay.herokuapp.com/'><em>ChartBay</em></a></h4><h4><i>~Team Ternalt's</i></h4>"
                else:
                    html_content = f"<h1> PDF Available !</h1><a href='{my_url}'>Click Here</a><h4>Here's the url:<a href='{my_url}'>{my_url}</a></h4><h4> Do Share with your Friends: <a href='https://chartbay.herokuapp.com/'><em>ChartBay</em></a></h4><h4><i>~Team Ternalt's</i></h4>"
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                return render(request, 'chartapp/output.html',context)    
    return render(request, 'chartapp/index.html', {'form': form})

def charts(request):
    return render (request,'chartapp/charts.html')
def about(request):
    return render (request,'chartapp/about.html')


