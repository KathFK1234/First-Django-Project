from django import forms
from .models import Reservation

# Creating this form to gather the required input
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation # This imports from the model we are referencing for the fields we shall gather in the form
        fields = '__all__' # This gathers all fields in the model we're referencing
        