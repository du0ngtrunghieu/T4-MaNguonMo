from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',null=True, auto_now_add=True)
    
    #Add owner
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Câu hỏi"
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='questions')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    class Meta:
          
        verbose_name_plural = "Choice"
    def __str__(self):
        return self.choice_text
