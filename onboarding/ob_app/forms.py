from django import forms
from .models import AllKeys
from .models import NewEmployee


class AllKeysForm(forms.ModelForm):
    class Meta:
        model = AllKeys
        fields = ['newEmployeeID', 'employeeID', 'licenseIDS', 'materialIDS', 'accountIDS', 'otherIDS',
                  'installationIDS']
        widgets = {
            'newEmployeeID': forms.Select(attrs={'class': 'form-control'}),
            'employeeID': forms.Select(attrs={'class': 'form-control'}),
            'licenseIDS': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'materialIDS': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'accountIDS': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'otherIDS': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'installationIDS': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = NewEmployee
        fields = ['firstname', 'lastname', 'role']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }
