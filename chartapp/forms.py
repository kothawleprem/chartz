from django import forms

type_of_charts = [('bar','Bar'),('line','Line'),('pie','Pie'),]
type_of_formats = [('png','PNG'),('pdf','PDF')]

class NameForm(forms.Form):
    types = forms.CharField(label='Type', max_length=100,widget=forms.Select(choices=type_of_charts))
    labels = forms.CharField(label='Labels', max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter Labels Sep. By Comma'}))
    data = forms.CharField(label='Data', max_length=100,widget= forms.TextInput(attrs={'placeholder':'Enter Data Sep. By Comma'}))
    formats = forms.CharField(label='Select Format', max_length=100,widget=forms.Select(choices=type_of_formats))