from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone_number', 'company_name', 'category', 'product', 'inquiry_type', 'message', 'preferred_contact_time']
        widgets = {
            'preferred_contact_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
