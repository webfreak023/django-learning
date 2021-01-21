from random import choice
from string import ascii_lowercase, ascii_letters, digits, punctuation
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'generator/index.html')

def generate_password(request):
    length = int(request.GET.get('length', 10))
    choice_of_characters = ascii_lowercase
    if request.GET.get('uppercase'):
        choice_of_characters = ascii_letters
    if request.GET.get('numbers'):
        choice_of_characters = choice_of_characters+digits
    if request.GET.get('specialchar'):
        choice_of_characters = choice_of_characters+punctuation
    generated_password = ''.join([choice(choice_of_characters) for letter in range(length)])
    return render(request, 'generator/generator.html',{'password':generated_password, 'params': ''.join([i for i in request.GET.values()])})

def about(request):
    return render(request, 'generator/about.html')