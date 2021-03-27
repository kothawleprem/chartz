from django.http import HttpResponseRedirect
from django.shortcuts import render

import json
from urllib.parse import urlencode  # python 3
# from urllib import urlencode      # python 2
import requests
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives



# Create your views here.
def filesHome(request):
    return render(request,'files/index.html')


def upload_csv(request):
    data = {}
    if "GET" == request.method:
        return render(request, "files/upload_csv.html", data)
# if not GET, then proceed with processing
    
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'File is not CSV type')
        return HttpResponseRedirect(reverse("myapp:upload_csv"))
            #if file is too large, return message
    if csv_file.multiple_chunks():
        messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
        return HttpResponseRedirect(reverse("myapp:upload_csv"))
    file_data = csv_file.read().decode("utf-8")          
    lines = file_data.split("\n")
    #loop over the lines and save them in db. If error shows up , store as string and then display
    label_list = []
    data_list = []
    # types = "" 
    # formats = ""
    # name = ""
    # toemail = ""
    for line in lines:                                   
        fields = line.split(",")
        data_dict = {}
        # if fields[0] == "label":
        #     print("ok")
        #     continue
        # if fields[1] == "value":
        #     print("ok")
        #     continue  
        # print(fields[0])
        # print(fields[1])
        # data_dict["label"] = fields[0]
        # label_list.append(data_dict["label"])
        # if "\r" in fields[1]:
        #     my_field = fields[1].replace("\r","")
        # data_dict["data"] = my_field
        # # data_list.append(int(data_dict["data"])) 
        # print(data_list)
        # print(label_list)
        try:
            if fields[0] == "types":
                types = fields[1].replace("\r","")
                continue
            if fields[0] == "formats":
                formats = fields[1].replace("\r","")
                continue
            if fields[0] == "name":
                name = fields[1].replace("\r","")
                continue
            if fields[0] == "toemail":
                toemail = fields[1].replace("\r","")
                continue
            if fields[0] == "label":
                continue
            if fields[1] == "value":
                continue   
            data_dict["label"] = fields[0]
            label_list.append(data_dict["label"])
            if "\r" in fields[1]:
                my_field = fields[1].replace("\r","")
            data_dict["data"] = my_field
            data_list.append(int(data_dict["data"])) 
            print(data_list)
            print(label_list)
        except:
            print("")
    try:
        form = EventsForm(data_dict)
        if form.is_valid():
            form.save()
    except:
        print("")
    config = {
        "type": types,
        "data": {
            "labels": label_list,   #Set X-axis labels
            "datasets": [{
                "label": name,                         # Create the 'Users' dataset
                "data": data_list           # Add data to the chart
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

    context = {'my_url' : my_url, 'format' : 'png',}
    if len(toemail)>1:
        subject, from_email, to = 'Your Chart Is Delivered!!!', settings.EMAIL_HOST_USER,toemail
        text_content = 'Chart Sent Successfully'
        # if formats == "png":
        html_content = f"<h1> Your Chart is Ready </h2> <img src='{my_url}'/><p> Team Ternalt's</p>"
        # else:
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()                                                                   
    return render(request, "files/upload_csv.html", context)

