from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #cascade 얘랑 연결된 question이 사라지면 얘도 사라진다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
