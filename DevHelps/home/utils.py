from django.utils.text import slugify
import home.models
import random
import string

def randomstring(N):
    res= ''.join(random.choices(string.ascii_uppercase+string.digits,k = N))
    return res

def genrateslug(title):
    new_slug = slugify(title)
    if home.models.BlogModel.objects.filter(slug=new_slug).first():
        return genrateslug(new_slug+randomstring(5))
    return new_slug
