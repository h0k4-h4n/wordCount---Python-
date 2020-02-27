from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')

def count(request):
    fullText = request.GET['fulltext']
    sorted = fullText.split()
    wordDict = {}
    for word in sorted:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    return render(request, 'count.html', {'fullText': fullText, 'count': len(sorted), 'wordDict': wordDict.items()})

def about(request):
    return render(request, 'about.html')