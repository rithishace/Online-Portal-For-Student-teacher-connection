from django import forms
from .models import Assignment,vsoln

class AssignmentForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('Grade','Subject_Name','Description','Content')

class view_assignment_form(forms.ModelForm):
    class Meta:
        model=vsoln
        fields=('Assignment_Code',)
        
