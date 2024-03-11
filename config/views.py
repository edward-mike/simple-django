from django.template.response import TemplateResponse
from django.http import HttpResponse


def welcome(request: HttpResponse, 
            template:str = "index.html",
            *args,
            **kwargs) -> HttpResponse:
    
    template_data = {
        "message": "simple Django project on AWS EC2"
    }
    
    return TemplateResponse(request,template,template_data)