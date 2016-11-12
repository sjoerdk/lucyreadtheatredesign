from django.http import HttpResponse
from django.template.response import TemplateResponse

def test(request):
    
    return HttpResponse("You're looking at question letters")

def homepage(request,template=u"homepage.html"):
    
    
    return TemplateResponse(request, template, {"skanky":"yomama"})