from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import FarmerData
import re

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, help_text='Enter your first name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Enter your last name')
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # Add error styling if form has errors
            if hasattr(self, 'errors') and field_name in self.errors:
                field.widget.attrs['class'] += ' is-invalid'
        
        # Add placeholders
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise ValidationError("Username must be at least 3 characters long.")
        return username

class FarmerDataForm(forms.ModelForm):
    class Meta:
        model = FarmerData
        exclude = ['user', 'is_approved', 'created_at', 'updated_at']
        fields = ['farmer_name', 'phone_number', 'village', 'district', 'state', 'farm_id', 'owner', 'water_source', 'irrigation_type', 'organic_type', 'aadhaar_number', 'aadhaar_image', 'crop_type', 'land_area']
        widgets = {
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Auto-populate farmer name if user is provided and form is new
        if user and not self.instance.pk:
            full_name = f"{user.first_name} {user.last_name}".strip()
            if full_name:
                self.fields['farmer_name'].initial = full_name
        
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
            # Add error styling if form has errors
            if hasattr(self, 'errors') and field_name in self.errors:
                field.widget.attrs['class'] += ' is-invalid'
        
        # Add placeholders
        self.fields['farm_id'].widget.attrs['placeholder'] = 'Enter unique farm ID'
        self.fields['owner'].widget.attrs['placeholder'] = 'Enter owner name'
        self.fields['water_source'].widget.attrs['placeholder'] = 'Select water source'
        self.fields['irrigation_type'].widget.attrs['placeholder'] = 'Enter irrigation type'
        self.fields['farmer_name'].widget.attrs['placeholder'] = 'Enter farmer name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'
        self.fields['village'].widget.attrs['placeholder'] = 'Enter village name'
        self.fields['district'].widget.attrs['placeholder'] = 'Enter district name'
        self.fields['state'].widget.attrs['placeholder'] = 'Enter state name'
        self.fields['aadhaar_number'].widget.attrs['placeholder'] = 'Enter 12-digit Aadhaar number'
        self.fields['crop_type'].widget.attrs['placeholder'] = 'Enter crop type'
        self.fields['land_area'].widget.attrs['placeholder'] = 'Enter land area in acres'
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone and not re.match(r'^[0-9]{10}$', phone):
            raise ValidationError("Phone number must be exactly 10 digits.")
        return phone
    
    def clean_aadhaar_number(self):
        aadhaar = self.cleaned_data.get('aadhaar_number')
        if aadhaar and not re.match(r'^[0-9]{12}$', aadhaar):
            raise ValidationError("Aadhaar number must be exactly 12 digits.")
        return aadhaar
    
    def clean_land_area(self):
        land_area = self.cleaned_data.get('land_area')
        if land_area and land_area <= 0:
            raise ValidationError("Land area must be greater than 0.")
        return land_area
    


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if hasattr(self, 'errors') and field_name in self.errors:
                field.widget.attrs['class'] += ' is-invalid'
        
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter your password'
    
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_active:
            raise ValidationError("This account is inactive.")
    
    error_messages = {
        'invalid_login': "Please enter a correct username and password. Note that both fields may be case-sensitive.",
        'inactive': "This account is inactive.",
    }