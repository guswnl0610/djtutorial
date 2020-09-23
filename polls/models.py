from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __Str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #cascade 얘랑 연결된 question이 사라지면 얘도 사라진다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __Str__(self):
        return self.choice_text