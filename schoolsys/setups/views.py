from django.shortcuts import render

# Create your views here.
def academics(request):
    return render(request, 'setups/academics/academic_setup.html')

def system(request):
    return render(request, 'setups/system/system_setup.html')