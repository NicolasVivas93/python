# Connecting our blog to the admin interface will allow us to see links for both the Posts and Comments inside the admin dashboard
# To connect the two together, we need to register our Posts and Comments models inside of this admin file 

from django.contrib import admin
from .models import Post
from .models import Comment

admin.site.register(Post)
admin.site.register(Comment)

# You have now registered the Post and Comment models inside of the admin panel. This will enable the admin interface to pick these models up and show them to the user that is logged into and viewing the admin dashboard.