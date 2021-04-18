from django.db import models
from django.conf import settings
import os

# Create your models here.
def get_form_path(instance,filename):
    upload_dir=os.path.join('Assignments/',instance.user.username)
    return os.path.join(upload_dir,filename)

class Assignment(models.Model):
    
    Assignment_Code=models.CharField(max_length=10)
    CHOICELIST=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'))
    Grade= models.CharField(max_length=100,choices=CHOICELIST)
    SUBLIST=(('English','English'),('Hindi','Hindi'),('Mathematics','Mathematics'),('Physics','Physcis'),('Chemistry','Chemistry'),('Computer Science','Computer Science'),('Biology','Biology'),('History','History'),('Geography','Geography'),('Civics','Civics'),('Economics','Economics'),('Political Science','Political Science'),('Business Studies','Business Studies'),('Accountancy', 'Accountancy'),('Sanskrit','Sanskrit'),('Social Studies', 'Social Studies'),('EVS',' EVS'))
    Subject_Name= models.CharField(max_length=100,choices=SUBLIST)
    Description= models.CharField(max_length=100)
    Content =models.FileField(upload_to=get_form_path)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.Assignment_Code

    def delete(self, *args, **kwargs):
        self.Content.delete()
        super().delete(*args, **kwargs)


class vsoln(models.Model):
    Assignment_Code=models.CharField(max_length=100)
