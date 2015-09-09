from django.forms import ModelForm
from app.models import Pledge
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class PledgeForm(ModelForm):
    class Meta:
        model = Pledge
        #Duplicate the fields from the model that will be used in the form
        fields = ('email', 'pledge', 'name')#, 'completed'

    def __init__(self, *args, **kwargs):
        super(PledgeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Anonymous'})
        self.helper = FormHelper(self)
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Fieldset(
                ' ',
                'email',
                'pledge',
                'name',
                'completed',
            ),
            # ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-default')
            # )
        )