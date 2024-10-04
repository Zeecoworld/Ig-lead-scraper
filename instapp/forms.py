from django import forms

class SearchForm(forms.Form):
    searchTerms = forms.CharField(label='Search Terms', required=True,widget=forms.TextInput(attrs={
            'placeholder': 'Enter search terms here',
            'class': 'form-control',
            'id':'searchTerms'  #type="text" class="form-control" id="searchTerms"
        }))
    profileType = forms.ChoiceField(choices=[
        ('', 'Any'),
        ('personal', 'Personal'),
        ('business', 'Business')  #class="form-select" id="profileType"
    ], label='Profile Type', widget=forms.Select(attrs={'class': 'form-select','id':'profileType'}))
    includeTerms = forms.CharField(label='Include Terms', required=False,widget=forms.TextInput(attrs={
            'placeholder': 'Comma-separated terms',
            'class': 'form-control', #type="text" class="form-control" id="includeTerms" placeholder="Comma-separated terms"
            'id': 'includeTerms'
        }))
    excludeTerms = forms.CharField(label='Exclude Terms', required=False, widget=forms.TextInput(attrs={
            'placeholder': 'Comma-separated terms',
            'class': 'form-control', #type="text" class="form-control" id="excludeTerms" placeholder="Comma-separated terms"
            'id':'excludeTerms'
        }))