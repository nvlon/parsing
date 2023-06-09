from django import forms
from . import models, parser

class ParserForm(forms.Form):
    MEDIA_CHOICES =(
        ('toyboss.kg', 'toyboss.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)


class Meta:
    fields =[
        'media_type',
    ]

def parser_data(self):
        if self.data['media_type']== 'toyboss.kg':
            sausage_parser= parser.parser()
            for i in sausage_parser:
                models.ToybossKg.objects.create(**i)