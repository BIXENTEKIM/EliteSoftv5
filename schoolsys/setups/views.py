from django.shortcuts import render

# Create your views here.
def academics(request):
    return render(request, 'setups/academics/academic_setup.html')