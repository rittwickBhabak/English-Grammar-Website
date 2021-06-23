from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Book, Question 
from django.http import JsonResponse 
import json 

# Create your views here.
def book_list(request):
    all_books = Book.objects.all().order_by('name')
    context = {
        'all_books': all_books
    }
    return render(request, 'book/book-list.html', context=context)

def book(request, book_id):
    pdf = Book.objects.filter(id=book_id).first() 
    page_arg = request.GET.get('page')
    question_id = request.GET.get('question')
    if page_arg:
        try:
            page_number = int(page_arg)
        except:
            page_number = pdf.last_read_page 
    else:
        page_number = pdf.last_read_page

    highlight_question = None 
    if question_id:
        try:
            highlight_question = int(question_id)
        except:
            pass

    questions = Question.objects.filter(book = pdf, page_number = page_number)
    if pdf:
        context = {
            'book': pdf ,
            'questions': questions,
            'highlight': highlight_question
        }
        return render(request, 'book/book.html', context=context)
    else:
        messages.warning(request, 'Book Not Found')
        return redirect('/book/')

def update_last_page(request):
    if request.method == 'POST':
        try:
            last_page = request.POST.get('last_page')
            book_id = request.POST.get('book_id')
            book = Book.objects.filter(id = book_id).first()
            if book:
                book.last_read_page = last_page
                book.save()
                return JsonResponse({"status": "success"})
        except:
            return JsonResponse({"status": "error"})
    
    return JsonResponse({"status": 'Method not allowed'})

def update_zoom_level(request):
    if request.method == 'POST':
        try:
            last_page = request.POST.get('zoom_level')
            book_id = request.POST.get('book_id')
            book = Book.objects.filter(id = book_id).first()
            if book:
                book.zoom_level = last_page
                book.save()
                return JsonResponse({"status": "success"})
        except:
            return JsonResponse({"status": "error"})
    
    return JsonResponse({"status": 'Method not allowed'})


def add_question(request):
    if request.method == 'POST':
        try:
            question = request.POST.get('question')
            answer = request.POST.get('answer')
            page_number = request.POST.get('page_number')
            book_id = request.POST.get('book_id')
            book = Book.objects.filter(id = book_id).first()
            if book:
                question_obj = Question.objects.create(question = question,answer = answer,book = book,page_number = page_number)
                question_obj.save()
                question_answer_obj = {
                    'question': question,
                    'answer': answer
                }
                return JsonResponse({"status": "success", "question": question, "answer": answer})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    
    return JsonResponse({"status": 'Method not allowed'})

def update_question(request):
    if request.method == 'POST':
        try:
            question_text = request.POST.get('question')
            answer = request.POST.get('answer')
            qid = request.POST.get('q_id')
            question = Question.objects.filter(id=qid).first()
            if question:
                question.question = question_text
                question.answer = answer 
                question.save()
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": 'error'})
        except Exception as e:
            return JsonResponse({"status": "error", "messasge": str(e)})
    return redirect('/book')