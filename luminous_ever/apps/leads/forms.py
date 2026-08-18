from django import forms

from apps.services.models import Service

from .models import Lead


class LeadForm(forms.ModelForm):
    # Honeypot: real visitors never see or fill this (hidden off-screen via
    # CSS, not display:none — some bots skip fields that are display:none
    # but still fill plain hidden-looking ones). Any value here means spam.
    website_url = forms.CharField(required=False, widget=forms.TextInput(attrs={"autocomplete": "off", "tabindex": "-1"}))

    services_required = forms.ModelMultipleChoiceField(
        queryset=Service.objects.filter(is_published=True),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Lead
        fields = [
            "name", "business_name", "phone", "email", "website",
            "business_type", "services_required", "budget_range", "message",
        ]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_website_url(self):
        # Honeypot tripped — reject silently rather than telling a bot why.
        value = self.cleaned_data.get("website_url")
        if value:
            raise forms.ValidationError("Submission rejected.")
        return value
