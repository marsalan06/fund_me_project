from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
    
def mutual_funds(request):
    return render(request, 'mutual_funds.html')

def calculator(request):
    return render(request, 'calculator.html')