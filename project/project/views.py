from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render



def hello(request):
    return HttpResponse('''
                  
        <h1 style="background-color: gray; color: white; border: 3px red solid; text-align: center;">Hello from Django</h1>      
                        
    ''')
    
@csrf_exempt   
def addxy(request):
        if(request.method == 'POST'):
            x = int(request.POST.get('first'))
            y = int(request.POST.get('second'))
            
            f = x+y
            
            return HttpResponse('result = '+ str(f))
        else:
            return HttpResponse(
                '''
                
                    <form action="add" method="post">
                        <p>
                            <label for="first">first value</label>
                            <input type="text" name="first">
                        </p>
                        
                        <p>
                            <label for="second">second value</label>
                            <input type="text" name="second">
                        </p>
                        <button type="submit">add</button>
                    </form>
                    
                
                '''
            )
            


from .forms import InputForm
def add(request):
    z=0
    form = InputForm()
    if request.method =='POST':
        form = InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x =cd['x']
            y =cd['y']
            z =x + y
            
    return render(request, 'pages/addition.html',{'form':form, 'output':z})



def performArithmetic(request):
    x=1
    y=1
    form = InputForm()
    if request.method =='POST':
        form = InputForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            x =cd['x']
            y =cd['y']
            z =x + y
            
    return render(request, 'pages/arithmetic.html',{'form':form,
                                                                               
               'x':x,
               'y':y,
               'r1':x+y,
               'r2':x-y,
               'r3':x*y,
               'r4':x//y,
               'r5':x%y,
            }
    )