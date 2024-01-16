from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    
    
    def save(self, *args, **kwargs):
        #do something before the data is saved to the database
        if self.name == "Yoko Onos's Blog":
            return
        else:
            super().save(*args, **kwargs)
