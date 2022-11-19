from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Creamos modelo para tabla de posts en la BD
class Post(models.Model):
    # Creamos los campos 
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255) #Lugar donde las URL's válidas se generan y se almacenan para las webpages
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

# Definimos funcionalidad de la URL y funcion Save para guardar el post. La idea con esto es crear un único link que matchee con un único post
def get_absolute_url(self):
    return reverse('blog_post_detail', args=[self.slug])

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)

#ordenamos los posts for fecha de creacion
class Meta:
    ordering = ['created_on']

    def __unicode__(self):
        return self.title

# Creamos modelo para tabla que almacenará los coments en la BD
class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #El post al cual se está haciendo el comentario
    created_on = models.DateTimeField(auto_now_add=True)
