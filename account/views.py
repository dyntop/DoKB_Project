from django.shortcuts import render

# Create your views here.
def name(request):
    return render(request, 'name.html')

def result(request):
    name = request.POST.get('name')
    if name == "다연":
        return render(request, 'result.html')
    else:
        return render(request, 'name.html')
