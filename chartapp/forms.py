from django import forms

type_of_charts = [('bar','Bar'),('line','Line'),('pie','Pie'),('radar','Radar'),('doughnut','Doughnut'),('polarArea','PolarArea'),('scatter','Scatter'),('bubble','Bubble'),('radialGauge','RadialGauge'),('violin','Violin'),('sparkline','Sparkline'),('progressBar','ProgressBar')]
type_of_formats = [('png','PNG'),('pdf','PDF')]

class NameForm(forms.Form):
    name  = forms.CharField(label='Title', max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter Title for the Chart','class': 'form-control'}),required=False)
    types = forms.CharField(label='Choose Your Chart', max_length=100,widget=forms.Select(choices=type_of_charts,attrs={'class':'form-select form-select-lg mb-3','aria-label':'form-select-lg example'}),required=False)
    labels = forms.CharField(label='Labels', max_length=100,widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Labels Seperated By Comma'}),required=False)
    data = forms.CharField(label='Data', max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter Data Values Seperated By Comma','class': 'form-control'}),required=False)
    formats = forms.CharField(label='Select Output Format', max_length=100,widget=forms.Select(choices=type_of_formats,attrs={'class':'form-select form-select-sm','aria-label':'.form-select-sm example'}),required=False)
    qrcode = forms.CharField(label='Text for QR Code',max_length=300,widget= forms.TextInput(attrs={'placeholder':'Enter Text','class': 'form-control'}),required=False)
    toemail = forms.CharField(label='Email', max_length=100,widget= forms.TextInput(attrs={'placeholder':'example@mail.com','class': 'form-control' }),required=False)
    
