from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Custom styling for each field
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email", 
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your text"})
    )
    
    def clean(self):
        username_or_email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username_or_email and password:
            # Check if the user entered an email or username
            user = authenticate(
                self.request, 
                username=username_or_email, 
                password=password
            )
            
            if user is None:
                # Try authenticating by email if username authentication failed
                try:
                    from django.contrib.auth.models import User
                    username = User.objects.get(email=username_or_email).username
                    user = authenticate(self.request, username=username, password=password)
                except User.DoesNotExist:
                    pass
            
            if user is None:
                raise forms.ValidationError("Invalid username or password.")
        
        return self.cleaned_data