from django import forms
from .models import Category,Description

class SearchForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects,label="カテゴリ名",required=False)


class TextCreateForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = '__all__'
