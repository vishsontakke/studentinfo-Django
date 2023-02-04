
from django import forms
from .models import User

class studentinfo(forms.ModelForm):
    class Meta:
        model=User
        fields=["name","email","Course","div","rollno"]
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'Course': forms.TextInput(attrs={'class':'form-control'}),
            'div': forms.TextInput(attrs={'class':'form-control'}),
            'rollno': forms.TextInput(attrs={'class':'form-control'}),
        }