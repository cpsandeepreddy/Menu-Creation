from django.forms import ModelForm
from card.models import Data
class TestForm(ModelForm):
    class Meta:
        model=Data

