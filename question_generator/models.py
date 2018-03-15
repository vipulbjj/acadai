from django.db import models
# Create your models here.

class PdfFile(models.Model):
	file = models.FileField(upload_to='question_paper_files_pdf/')