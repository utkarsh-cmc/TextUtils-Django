# Author - Utkarsh Gumphekar
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def navigator(request):
    
    return HttpResponse('''<h1><centre>Personal Navigator</centre></h1>
    <ul>
        <li> <a href="https://github.com/utkarsh-cmc">Utkarsh github profile</a> </li>
        <li> <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django playlist YT</a> </li>
        <li> <a href="https://mail.google.com/mail/u/0/#inbox">Utkarsh Mail</a> </li>
    </ul>''')

def analyze(request):
    #getting the text
    djtext=request.POST.get('text','default')
    #checkbox value checker
    removepunc=request.POST.get('removepunc','off')        
    fullcaps=request.POST.get('fullcaps','off')
    newlineR=request.POST.get('newlineR','off')
    xspacerem=request.POST.get('xspacerem','off')
    charcount=request.POST.get('charcount','off')
    
#if we want to remove punctuations
    if removepunc=="on" and len(djtext)>0:                       
        analyzed=""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        parameter={'purpose':'Removed Punctuations','analyzed_text': analyzed}
        djtext=analyzed

#if we want to UPPERCASE
    if(fullcaps=='on'):                                    
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()  
        parameter={'purpose':'changed to UPPERCASE','analyzed_text': analyzed}   
        djtext=analyzed
        

#if we want to Newline remove
    if(newlineR=='on'):
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed=analyzed+char
        parameter={'purpose':'newline removed','analyzed_text':analyzed}  
        djtext=analyzed

#removes extra space          
    if(xspacerem=='on'):
        analyzed=""
        analyzed=djtext.strip
        parameter={'purpose':'extra space removed','analyzed_text':analyzed}  
        djtext=analyzed
        
#character counter
    if(charcount=='on'):
        count=0
        for i in djtext:
            count+=1
        
        parameter={'purpose':'character count','analyzed_text':count}  
        return render(request, 'analyze.html', parameter)
          

    if(removepunc != "on" and newlineR!="on" and xspacerem!="on" and fullcaps!="on" and charcount!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', parameter)


