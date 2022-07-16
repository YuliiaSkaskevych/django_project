from django import forms

from triangle.models import Person


class triangle_form(forms.Form):
    leg_1 = forms.FloatField(label='Leg 1', min_value=1, required=True)
    leg_2 = forms.FloatField(label='Leg 2', min_value=1, required=True)


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
