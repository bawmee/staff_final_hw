from django import forms
from .models import post


class post_fo(forms.Form):
    site = forms.ChoiceField(choices=[('Netfilx', 'Netfilx'), ('Watcha', 'Watcha'),('Qoop', 'Qoop'), ('Tving', 'Tving'), ('Etc', 'Etc')])
    contry = forms.CharField(required = True)
    genre = forms.CharField(required = True)
    rate = forms.ChoiceField(choices=[('1', '1'), ('2', '2'),('3', '3'), ('4', '4'), ('5', '5')])
    title = forms.CharField(required = True)
    review = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(post_fo, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        new_post = post(**self.cleaned_data)
        if commit:
            new_post.save()
        
        return new_post