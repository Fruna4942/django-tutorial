from django.contrib import admin
from .models import Choice, Question

# Register your models here.

# django의 default form
"""
admin.site.register(Question)
"""

"""
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
"""

"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
"""


# admin.StackedInline : 한줄에 한 필드씩 표시
# admin.TabularInline : 테이블 형식
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 적절한 필터 옵션 제공
    list_filter = ['pub_date']
    # 검색 기능 추가
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)