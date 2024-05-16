from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Наслов на книгата',
            'image': 'Слика',
            'isbn': 'ИСБН',
            'year': 'Година на издавање',
            'publisher': 'Издавачка куќа',
            'pages': 'Број на страни',
            'dimensions': 'Димензии',
            'cover_type': 'Корица',
            'category': 'Категорија',
            'price': 'Цена',
        }
