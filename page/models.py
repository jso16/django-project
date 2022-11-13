from django.db import models


class EmailNewsletter(models.Model):
    email = models.CharField(max_length=200, unique=True)
    registred_at = models.DateTimeField('date published')
    def __str__(self):
        return self.email + ' ' + str(self.registred_at)
      
