from django.shortcuts import render

def calculatePage(request):
  context={}
  return render(request,'calculate/calcul.html',context)