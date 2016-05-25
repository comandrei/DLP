from django.contrib import admin
from . import models


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'votes')
    fields = ('choice_text', 'votes', 'question')
    readonly_fields = ('votes', )


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_recently_published')
    fields = ('question_text', 'pub_date', )


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice, ChoiceAdmin)
