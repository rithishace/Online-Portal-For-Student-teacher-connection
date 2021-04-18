from django.db import models

# Create your models here.
class Student(models.Model):
    CHOICELIST=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'))
    Class= models.CharField(max_length=100,choices=CHOICELIST)
    SUBLIST=(('English','English'),('Hindi','Hindi'),('Mathematics','Mathematics'),('Physics','Physcis'),('Chemistry','Chemistry'),('Computer Science','Computer Science'),('Biology','Biology'),('History','History'),('Geography','Geography'),('Civics','Civics'),('Economics','Economics'),('Political Science','Political Science'),('Business Studies','Business Studies'),('Accountancy', 'Accountancy'),('Sanskrit','Sanskrit'),('Social Studies', 'Social Studies'),('EVS',' EVS'))
    Subject_Name= models.CharField(max_length=100,choices=SUBLIST)
    
    def __str__(self):
        return self.Class
