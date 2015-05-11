from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)  #blog title
    category = models.CharField(max_length = 50, blank = True)  #blog tag
    date_time = models.DateTimeField(auto_now_add = True)  #blog date
    content = models.TextField(blank = True, null = True)  #bnlog article

    def __unicode__(self) :
        return self.title

    class Meta:  #sort by created date
        ordering = ['-date_time']