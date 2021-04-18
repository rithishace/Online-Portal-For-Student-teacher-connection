from django import forms
from .models import view_assignment,Solution


class view_assignment_form(forms.ModelForm):
    class Meta:
        model=view_assignment
        fields=('Assignment_Code',)


class SolutionForm(forms.ModelForm):
    class Meta:
        model=Solution
        fields=('Assignment_Code','Name','Grade','Section','Admission_Number','Content')
