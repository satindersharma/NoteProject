from .models import Note
from django import forms


class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class': 'form-control'})
        self.fields['is_favourite'].widget.attrs.update(
            {'class': 'custom-control-input'})

    content = forms.CharField(label="",
                                   required=False,
                                   widget=forms.Textarea(
                                       attrs={"class": "form-control", "rows": "1", "autocomplete": "off"})
                                   )


    class Meta:
        model = Note
        fields = '__all__'
