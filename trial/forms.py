from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):

    # investor_type = forms.ChoiceField(choices=INVESTOR_TYPE, widget=forms.RadioSelect)
    class Meta:
        model = Document
        fields = ['InvestorType', 'asset', 'debt', 'foreignassets', 'foreigndebt',
                  'year_export', 'year_import', 'investment']
        widgets = {
            'InvestorType': forms.RadioSelect()
        }
