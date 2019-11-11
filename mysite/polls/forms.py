from django import forms
from .models import Question,Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {'question_text': 'Tên câu hỏi '}


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        labels = {'choice_text': 'Your choice'}
        widgets = {'choice_text': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Your choice'})}
    def __init__(self, *args, **kwargs):
        self.questions =  kwargs.pop('questions',None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        choice = super().save(commit=False)
        choice.question = self.questions
        choice.save()
        
