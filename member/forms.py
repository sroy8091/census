from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    # states = (('West Bengal', 'West Bengsl'),)
    # state = forms.CharField(label="Your Name:", max_length=30, choice=states)
    class Meta:
        model = Member
        fields = ('first_name', 'middle_name', 'last_name', 'dob', 'sex', 'employment_satus', 'adhaar_no')
