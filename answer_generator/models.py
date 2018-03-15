from django.db import models
# Create your models here.

class PdfFile(models.Model):
	file = models.FileField(upload_to='answer_generator_files_pdf/')