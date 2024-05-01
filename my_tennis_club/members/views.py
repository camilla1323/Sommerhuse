from django.http import HttpResponse
from django.template import loader
from .models import Member, Ejer, Sommerhus

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mydata = Member.objects.all()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


def ejer(request):
  myejer = Ejer.objects.all().values
  template = loader.get_template('ejer.html')
  context = {
    'myejer': myejer
  }
  return HttpResponse(template.render(context, request))

def detailsejer(request, id):
  myejer = Ejer.objects.get(id=id)
  template = loader.get_template('detailsejer.html')
  context = {
    'myejer': myejer,
  }
  # return HttpResponse("test asdfas")
  return HttpResponse(template.render(context, request))

def sommerhus(request):
    mysommerhus = Sommerhus.objects.all().values()
    template = loader.get_template('sommerhus.html')
    context = {
      'mysommerhus': mysommerhus,
    }
    return HttpResponse(template.render(context, request))

def detailssommerhus(request, id):
  mysommerhus = Sommerhus.objects.get(id=id)
  template = loader.get_template('detailssommerhus.html')
  context = {
    'mysommerhus': mysommerhus,
  }
  return HttpResponse(template.render(context, request))
