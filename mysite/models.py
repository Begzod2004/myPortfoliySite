from django.db import models


# Create your models here.


class Comments(models.Model):
    name        = models.CharField(max_length=255,null=False,blank=False)
    comment     = models.TextField(blank=False)
    image       = models.ImageField(null=True,upload_to='profile', default='profile/default.jpeg')
    published   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self): 
        """This function for to fix images url"""
        try:
            url = self.image.url
        except:
            url = ""
        return url


class MyResume(models.Model):
    file = models.FileField(upload_to='files/',default='resume.pdf')
    
    def __str__(self):
        return str(self.file)


class MyProjects(models.Model):

    SIDE_CHOICES = (
        ("left","left"),
        ("right","right"),
    )
    
    category    = models.CharField(max_length=123)
    side        = models.CharField(blank=False,null=True,choices=SIDE_CHOICES,max_length=5)
    image       = models.ImageField(null=True,blank=False)
    title       = models.CharField(max_length=27,null=True,blank=False)
    body        = models.CharField(max_length=500,null=True,blank=False)
    link        = models.CharField(max_length=255,null=True,blank=False)
    published   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published']


class MySkills(models.Model):
    name        = models.CharField(max_length=30,null=True,blank=False)
    image       = models.ImageField(null=True,blank=False)
    published   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



class MyWorkExprea(models.Model):
    name        = models.CharField(max_length=30,null=True,blank=False)
    image       = models.ImageField(null=True,blank=False)
    start_date  = models.DateTimeField()
    finish_date = models.DateTimeField()
    published   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['published']
    

class GetInTouch(models.Model):
    fullname    = models.CharField(max_length=255,null=True,blank=False)
    email       = models.EmailField(max_length=255,null=True,blank=False)
    body        = models.TextField(blank=False)
    published   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname