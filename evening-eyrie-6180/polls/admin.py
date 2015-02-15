from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,{'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date']}),
        ]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]
        

            

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('AAAAAAAAAAAAAAAAA', {'fields': ['question','choice_text','votes']}),
    ('BBBBBB', {'fields': ['question']})]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)

# Register your models here.
