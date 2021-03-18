from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'MyApp/name.html')
def age_view(request):
    name=request.GET['name']
    response=render(request,'MyApp/age.html',{'name':name})
    response.set_cookie('name',name)
    return response
def gf_view(request):
    age=request.GET['age']
    name=request.COOKIES['name']
    response=render(request,'MyApp/gf.html',{'name':name})
    response.set_cookie('age',age)
    return response
def result_view(request):
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    gfname=request.GET['gfname']
    response=render(request,'MyApp/results.html',{'name':name,'age':age,'gfname':gfname})
    response.set_cookie('gfname',gfname)
    return response