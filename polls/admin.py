from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['question_text', 'pub_date']
    # #pub_date가 q_t보다 앞으로 오게 한다

    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date information', {'fields' : ['pub_date']}),
        #첫번째 요소는 fieldset의 제목임
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #Question 목록 화면에 보이는 것들. 이것들은 기본적으로 메소드 이름임
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# Register your models here.
