

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.2.html')




def analyze(request):
    djtext=(request.GET.get('text','default'))
    removepunc = request.GET.get('removepunc','off')
    caps=request.GET.get('caps','off')
    newline=request.GET.get('newline','off')
    space=request.GET.get('space','off')
    if removepunc == "on":
    
       punctions = '''/[-[\]{}()*+?.',;\\^$|#\s]/g,"\\$&"'''
       analyzed=""
       for char in djtext:
         if char not in punctions:
           analyzed = analyzed+char
       params={'purpose':'removed punctions','analyzed_text': analyzed}
       djtext=analyzed

    if(caps=='on'):
        analyzed = ""
        for char in djtext:
          analyzed=analyzed+char.upper()
        params={'purpose':'change to upper case','analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(newline=='on'):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
              analyzed=analyzed+char
        params={'purpose':'remove new line','analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(space=='on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
              analyzed=analyzed+char
        params={'purpose':'extra space remover','analyzed_text': analyzed}
        
        # return render(request,'analyze.html',params)
    if(space!='on' and removepunc!='on' and space!='on' and newline!='on'):
         return HttpResponse('ERRORRRRR 404')

    
    return render(request,'analyze.html',params)
    