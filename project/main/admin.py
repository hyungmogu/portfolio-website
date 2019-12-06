from django.contrib import admin

from . import models

# class TextInline(admin.StackedInline):
#     model = models.Text

# class QuizInline(admin.StackedInline):
#     model = models.Quiz

# class CourseAdmin(admin.ModelAdmin):
#     inlines = [TextInline, QuizInline]

admin.site.register(models.Project) #register by adding this line
