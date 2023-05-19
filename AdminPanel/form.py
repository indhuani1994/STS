from .models import Placement_Model
from django import forms 

class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement_Model
        fields = '__all__'
