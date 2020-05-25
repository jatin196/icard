from django import forms
from .models import IdInfo
from bootstrap_datepicker_plus import DatePickerInput


class IcardForm(forms.ModelForm):
    # Name = forms.CharField(max_length=45)
    DateOfBirth = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y')
    )
    # Address = forms.Textarea()
    # Job = forms.CharField(max_length=45)


    class Meta:
        model = IdInfo
        fields = '__all__'