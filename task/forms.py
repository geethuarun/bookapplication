from django import forms
from task.models import Books

# class BooksCreateForm(forms.Form):
#     name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     price=forms.IntegerField()
#     publisher=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     publish_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"date"}))

class BooksCreateForm(forms.ModelForm): 
    class Meta:
        model=Books
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "publisher":forms.TextInput(attrs={"class":"form-control"}),
            "publish_date":forms.DateTimeInput(attrs={"type":"date"})


        }  


class BookChangeForm(forms.ModelForm):
    
    class Meta:
        model=Books
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "publisher":forms.TextInput(attrs={"class":"form-control"}),
            "publish_date":forms.DateTimeInput(attrs={"type":"date"})


        }