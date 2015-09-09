from django.forms import ModelForm
from app.models import Pledge

class PledgeForm(ModelForm):
    class Meta:
        model = Pledge
        #Duplicate the fields from the model that will be used in the form
        fields = ('email', 'pledge', 'name', 'completed')