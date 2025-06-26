from django import forms  # import forms

from .models import Reservation  # model we going to use


class ReservationForm(forms.ModelForm):  # inherit from the form class
    class Meta:                          # define meta properties/data
        model = Reservation              # our model is reservation
        # we want to use all the fields in our model.
        fields = '__all__'
