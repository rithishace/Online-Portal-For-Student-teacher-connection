from django.db import models
import os

# Create your models here.
def get_form_path(instance,filename):
    upload_dir=os.path.join('Uploaded_Assignments/',instance.Grade)
    return os.path.join(upload_dir,filename)

class view_assignment(models.Model):
    Assignment_Code=models.CharField(max_length=10)
    

class Solution(models.Model):
    Name=models.CharField(max_length=100)
    CHOICELIST=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'))
    Grade= models.CharField(max_length=100,choices=CHOICELIST)
    CHOICE=(('A','A'),('B','B'),('C','C'),('D','D'),('E','E'))
    Section=models.CharField(max_length=100,choices=CHOICE)
    Admission_Number=models.CharField(max_length=100)
    Content=models.FileField(upload_to=get_form_path)
    Assignment_Code=models.CharField(max_length=100,null=True)
    
    def delete(self, *args, **kwargs):
        self.Content.delete()
        super().delete(*args, **kwargs)

