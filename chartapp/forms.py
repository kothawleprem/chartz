from django import forms

type_of_charts = [('bar','Bar'),('line','Line'),('pie','Pie'),('radar','Radar'),('doughnut','Doughnut'),('polarArea','PolarArea'),('scatter','Scatter'),('bubble','Bubble'),('radialGauge','RadialGauge'),('violin','Violin'),('sparkline','Sparkline'),('progressBar','ProgressBar')]
type_of_formats = [('png','PNG'),('pdf','PDF')]

class NameForm(forms.Form):
    types = forms.CharField(label='Type', max_length=100,widget=forms.Select(choices=type_of_charts,attrs={'class':'form-select form-select-lg mb-3','aria-label':'.form-select-lg example'}),required=False)
    labels = forms.CharField(label='Labels', max_length=100,widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Labels Sep. By Comma'}),required=False)
    data = forms.CharField(label='Data', max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter Data Sep. By Comma','class': 'form-control'}),required=False)
    formats = forms.CharField(label='Select Format', max_length=100,widget=forms.Select(choices=type_of_formats,attrs={'class':'form-select form-select-sm','aria-label':'.form-select-sm example'}),required=False)
    qrcode = forms.CharField(label='Text for QR Code',max_length=300,widget= forms.TextInput(attrs={'placeholder':'Enter Text','class': 'form-control'}),required=False)
    toemail = forms.CharField(label='Email', max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter Email','class': 'form-control' }),required=False)
    name  = forms.CharField(label='Name', max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter Name for the Chart','class': 'form-control'}),required=False)
