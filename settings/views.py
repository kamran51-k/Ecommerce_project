from django.shortcuts import render

from settings.models import CategoryModel, NavbarModel

# Create your views here.
def home_view(request):
    context ={}
    navbar_queryset = NavbarModel.objects.all()
    context['navbar_queryset'] = navbar_queryset
    category_queryset = CategoryModel.objects.all()
    context['category_queryset'] = category_queryset

    return render(request,'index.html',context)
