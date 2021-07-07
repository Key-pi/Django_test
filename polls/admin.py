from django.contrib import admin

from .models import Choice, Log, Question, Board



@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['method', 'path', 'timestamp']
    date_hierarchy = 'timestamp'
    list_filter = ['method', 'timestamp']


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Board)