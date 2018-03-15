from django.urls import path

from . import views
from question_generator.views import PdfFileView

app_name = 'question_generator'

urlpatterns = [
    path('', views.index, name='index'),
    path('question_paper', views.question_paper,  name='question_paper'),
    path('upload', PdfFileView.as_view(), name='pdf_file_upload_question'),
]