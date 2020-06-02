from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=False)


class ArticleImageForm(forms.Form):
    image = forms.ImageField(required=False)
