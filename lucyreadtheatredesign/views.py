from django.http import HttpResponse
from django.template.response import TemplateResponse
from mezzanine.galleries.models import Gallery
from mezzanine.pages.models import Page

def test(request):
    
    return HttpResponse("You're looking at question letters")

def homepage(request,template=u"homepage.html"):
    
    g = Gallery.objects.all()
    p = Page.objects.all()
    return TemplateResponse(request, template, {"skanky":"yomama","all_galleries":g})