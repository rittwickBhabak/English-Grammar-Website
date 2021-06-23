from django.shortcuts import redirect, render
from book.models import Book, Question
import random 

# Create your views here.
def home(request):
    books = Book.objects.all()
    mylist= []
    total_questions = 0
    for book in books:
        no_of_questions = Question.objects.filter(book=book).count()
        total_questions = total_questions + no_of_questions
        obj = { 'book': book, 'no_of_questions': no_of_questions }
        mylist.append(obj)
        
    context = {
        'chapters': mylist ,
        'total_questions': total_questions
    }
    return render(request, 'practice/home.html', context=context)

def start_exam(request):
    if request.method=='POST':
        chapters = request.POST.getlist('chapter') 
        total_question = request.POST.get('total-question')
        chapters = list(map(int, chapters))
        questions = []
        chapters_list = []
        for book_id in chapters:
            questions = questions + list(Question.objects.filter(book=Book.objects.filter(id=book_id).first()))
            chapters_list.append(Book.objects.filter(id=book_id).first())

        new_questions = random.sample(questions, int(total_question))
        
        context = {
            'questions': new_questions,
            'chapters': chapters_list
        }
        return render(request, 'practice/test.html', context=context)
    
    return redirect('/practice/')

def evaluate_exam(request):
    if request.method == 'POST':
        question_ids = request.POST.get('quesiton_ids')
        answers = []
        for id in question_ids.split(','):
            ans = request.POST.get(f'answer-{id}')
            question = Question.objects.filter(id=id).first()
            answers.append({ 'question': question, 'answer': ans})
        context = {
            'answers': answers 
        }
        return render(request, 'practice/result.html', context=context)


    return redirect('/practice')