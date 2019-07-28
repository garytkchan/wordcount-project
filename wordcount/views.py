from django.http import HttpResponse # for just string
from django.shortcuts import render # redirect to html page
import operator


def home(request):
    #return HttpResponse("Hello world!!")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    # get and save input into fulltext
    fulltext = request.GET['fulltext']

    # split all input string into list separting by space
    wordlist = fulltext.split()

    # dictionary to record the recurrence of all words
    word_dictionary = {}

    # count each word and save count into word_dictionary
    for word in wordlist:
        if word in word_dictionary:
            #increase
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    # convert dictionary into a list. To print
    wordCountList = word_dictionary.items()

    # sort the wordCountList
    sortedWordList = sorted(wordCountList, key=operator.itemgetter(1), reverse=True)

    # use dictionary to pass input data
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedWordList': sortedWordList})
