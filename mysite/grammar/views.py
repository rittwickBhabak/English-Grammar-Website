from django.shortcuts import render

# Create your views here.
def books(request):
    return render(request, 'grammar/book-list.html')

def book(request):
    context = {
        'pdf': 'oxford_idioms.pdf'
    }
    return render(request, 'grammar/pdf-viewer.html', context=context)