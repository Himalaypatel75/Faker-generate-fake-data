from django import forms

class FakerForm(forms.Form):
    CHOICES = [
        ('name', 'Name'),
        ('address', 'Address'),
        ('phone', 'Phone Number'),
        ('email', 'Email'),
        ('job_title', 'Job Title'),
        ('company_name', 'Company Name'),
        ('text', 'Text'),
        ('date_of_birth', 'Date of Birth'),
        ('city', 'City'),
        ('country', 'Country'),
        ('credit_card_number', 'Credit Card Number'),
        ('ssn', 'SSN'),
        ('license_plate', 'License Plate'),
        ('ipv4_address', 'IPv4 Address'),
        ('mac_address', 'MAC Address'),
        ('url', 'URL'),
        ('username', 'Username'),
        ('password', 'Password'),
        ('currency', 'Currency'),
        ('uuid', 'UUID'),
    ]
    options = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    count = forms.IntegerField(min_value=1, max_value=100)
