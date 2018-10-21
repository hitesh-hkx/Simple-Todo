from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=100,widget=forms.TextInput(
    attrs={
        'placeholder':'Add a new Todo',
        'class':'form-control',
        'aria-label':'Todo',
        'aria-describedby':'add-btn'
    }))
