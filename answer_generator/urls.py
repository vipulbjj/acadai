from django.urls import path

from . import views
from answer_generator.views import PdfFileView

app_name='answer_generator'

urlpatterns = [
    path('', views.index, name='index_answer_generator'),
    path('ask_question', views.ask_question,  name='ask_question'),
    path('upload', PdfFileView.as_view(), name='pdf_file_upload'),
]