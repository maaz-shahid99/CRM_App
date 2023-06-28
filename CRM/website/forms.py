from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="", widget= forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="",widget= forms.TextInput( max_length=30,attrs={'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="",widget= forms.TextInput(max_length= 30, attrs={'class':'form-control', 'placeholder': 'Last Name'}))
    ph_number = forms.CharField(label="",widget= forms.TextInput(max_length= 10, attrs={'class':'form-control', 'placeholder': 'Phone Mumber'}))


    class Meta:
        model = User
        fields = ('username', 
                'first_name',
                'last_name',
                'email', 
                'ph_number', 
                'password_1', 
                'password_2'
                ) 
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['ph_number'].widget.attrs['class'] = 'form-control'
        self.fields['ph_number'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['ph_number'].label = ''
        self.fields['ph_number'].help_text = '<span class="form-text text-muted small"><small>Your number can\'t be more than 10 digits.</small><small>Your phone number is too short</small></span>'

        self.fields['password_1'].widget.attrs['class'] = 'form-control'
        self.fields['password_1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password_1'].label = ''
        self.fields['password_1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password_2'].widget.attrs['class'] = 'form-control'
        self.fields['password_2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password_2'].label = ''
        self.fields['password_2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'