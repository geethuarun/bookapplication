from django.shortcuts import render,redirect
from django.views.generic import View
from task.forms import BooksCreateForm,BookChangeForm
from task.models import Books

# Create your views here.

class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BooksCreateForm()
        return render(request,"books_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BooksCreateForm(request.POST)
        if form.is_valid():
            # Books.objects.create(**form.cleaned_data)
            form.save()
            print("book created")
            return redirect("book-list")
        else:
            return render(request,"books_add.html",{"form":form})
        
class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        return render(request,"books_list.html",{"books":qs})


class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render(request,"book_detail.html",{"book":qs})
    
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.filter(id=id).delete()
        return redirect("book-list")
    

class BookChangeView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookChangeForm(instance=obj)
        return render(request,"book_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookChangeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("book-list")
        else:
            return render(request,"book_edit.html",{"form":form})
    

