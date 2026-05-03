from django.contrib import admin

from pybo.models import Question, Answer

# Register your models here.
#admin.site.register(Question)
#admin.site.register(Answer)

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Answer,AnswerAdmin)

