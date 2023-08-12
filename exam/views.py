from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from django.http import JsonResponse
from datetime import datetime, timezone

# ...

from django.shortcuts import render
from .models import Question
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


  
from django.http import Http404
@login_required
def take_id(request, id):
    try:
        id_value= int(id)
        questions = Question.objects.filter(question_name_id=id_value)[:20]
        content = {'id': id, 'questions': questions}
        return render(request, 'quiz.html', content)
  # Lakukan pengolahan data lainnya
    except ValueError:
        # Jika tidak dapat mengubah id menjadi integer, kemungkinan ini adalah permintaan favicon.ico
        # Anggap saja tidak ada data yang ditemukan atau kirimkan pesan kesalahan
        raise Http404("No data found for the given ID")
@login_required
def home(request):
	course= courseName.objects.all()
	content= {'course': course}
	return render(request, 'home.html', content)
@login_required
def api_question(request, id):
    raw_questions= Question.object.filter(courseName= id)[:20]
    questions= []
    for raw_question in raw_questions:
        question= []
        question['question'] = raw_question.question
        question['answer'] = raw_question.answer
        question['marks'] = raw_question.marks
        options =[]
        options.append(raw_question.option_one)
        options.append(raw_question.option_two)
        options.append(raw_question.option_three)
        options.append(raw_question.option_four)
        options.append(raw_question.option_five)
        
        question['options']= options
        questions.append(question)
        
    return JsonResponse(questions, safe= False)
@login_required
def quiz_submit(request):
    if request.method == 'POST':
        user_answers = request.POST.dict()  # Mengambil semua jawaban yang dikirimkan
        user_score = 0

        # Loop melalui jawaban pengguna dan bandingkan dengan jawaban yang benar
        for question in Question.objects.all():
            user_answer = user_answers.get(f'question_{question.id}')
            if user_answer is not None and int(user_answer) == question.answer:
                user_score += 1

        return render(request, 'quiz_result.html', {'user_score': user_score})
    else:
        return HttpResponse('method not allowed')
