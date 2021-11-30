from django.db import models

class Score(models.Model):

    allsubject=(('math','คณิตศาสตร์'),
                ('science','วิทยาศาสตร์'),
                ('art','ศิลปะ'),
                ('eng','ภาษาอังกฤษ'))

    subject = models.CharField(max_length=50,choices=allsubject,default='NULL')
    std_name = models.CharField(max_length=100)
    score= models.IntegerField(default=0)

    def __str__(self):
        return self.std_name + " " + self.subject + " " + str(self.score)

user=models.CharField(max_length=250,null=False,default='unknown user')
