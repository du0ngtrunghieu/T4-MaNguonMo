from django.shortcuts import render,get_list_or_404,redirect,get_object_or_404
from django.views.generic import DetailView,ListView
from .models import Question,Choice
from .forms import QuestionForm,ChoiceForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

class HomeDetailView(ListView):
    model = Question
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Question.objects.order_by('-pub_date')[:5]
        test = Choice.objects.all()
        context['dataChoice'] = test
        context['data'] = data
        return context
@login_required(login_url='/users/login/')
def questions(request):
    """Show all questions"""
    # Query the database for all questions
    questions = Question.objects.all()

    
   
    # Context that will send to the template
    if request.method != 'POST':
        # No data submitted; create a blank form
        formQuestion = QuestionForm()
        formChoice = ChoiceForm()
    else:
        
        # POST data submitted; process data.
        formQuestion = QuestionForm(data=request.POST)
        formChoice = ChoiceForm()
        if formQuestion.is_valid():
            formQuestion.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

    # Display a blank or invalid form
    context = {'form': formQuestion,'questions' : questions,'formChoice':formChoice}
    
    return render(request, 'polls/questions.html', context)
@login_required(login_url='/users/login/')
def addChoice(request,question_id):
    if question_id is not None:
        if request.method == 'POST':
            questions = get_object_or_404(Question,id=question_id)
            if questions:
                choiceForm = ChoiceForm(data=request.POST,questions = questions)
                if choiceForm.is_valid():
                    
                    choiceForm.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))     
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))        


        

    

