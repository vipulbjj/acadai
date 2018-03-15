from django import forms

class FileForm(forms.Form):
	file = forms.FileField(label='Select a pdf file')

class QuestionForm(forms.Form):
    question = forms.CharField(label='Please enter question: ', max_length=100)