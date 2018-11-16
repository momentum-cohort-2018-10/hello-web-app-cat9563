from django.forms import ModelForm
from collection.models import Cat

class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = ('name', 'description',)