from django.shortcuts import render
# Create your views here.
def hello(request):
    tag=['rainy','sunny','cloudy']
    rate=4
    return render(request, 'index.html',
    {
        'name':'weather',
        'tag':tag,
        'rate':rate
    })

def p1(request):
    return render(request, 'p1.html')

def form(request):
    return render(request, 'form.html')

def addBlog(request):
    return render(request, 'result.html')