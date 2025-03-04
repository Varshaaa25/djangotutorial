from django import forms
  
# creating a form 
class ResultForm(forms.Form):
  
    USN = forms.CharField(max_length = 200)
    SEMESTER=forms.IntegerField()
   