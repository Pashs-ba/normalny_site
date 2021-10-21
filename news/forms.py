from django import forms


class NewsForm(forms.Form):
    ru_title = forms.CharField(label='Заголовок на русском', widget=forms.TextInput(attrs={'class': "form-control"}))
    en_title = forms.CharField(label='Заголовок на английском', widget=forms.TextInput(attrs={'class': "form-control"}))
    ru_text = forms.CharField(label='Текст на русском', widget=forms.Textarea(attrs={'class': "form-control"}))
    en_text = forms.CharField(label='Текст на английском', widget=forms.Textarea(attrs={'class': "form-control"}))
    media = forms.FileField(label='Картинка', widget=forms.FileInput(attrs={'class': "form-control"}))

