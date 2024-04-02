from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    series=[
        {'name' : 'Game of Thrones', 'Ratings' : 9.2},
        {'name' : 'Attack On Titan', 'Ratings' : 10.0},
        {'name' : 'You', 'Ratings' : 8.1},
        {'name' : 'Jujutsu Kaisen', 'Ratings' : 8.4},
        {'name' : 'Demon Slayer', 'Ratings' : 5.3},
        {'name' : 'The Boys', 'Ratings' : 8.9},
        {'name' : 'Your Name', 'Ratings' : 10.0}
    ]
    text='''Since its debut in 2013, Attack on Titan has received universal critical acclaim, 
            numerous accolades and is considered as one of the greatest anime series of all time. 
            Critics and audiences have praised the show for its storytelling, animation, action sequences,
            characters, voice acting (original and dubbed), soundtrack and dark themes. The anime is noted 
            for its widespread appeal and enormous global popularity, being 
            cited as an important factor in introducing anime to a new generation.'''
    return render(request,'index.html',context= {"series":series,'text':text})

def about_page(request):
    return render(request,'about.html')

def contact_page(request):
    return render(request,'contact.html')


def success_page(request):
    print('*'*10)
    return HttpResponse('This is a success page')