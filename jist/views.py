from django.shortcuts import render,redirect, HttpResponse
from . models import users, Feedback, StuDetails
from django.views.decorators.cache import cache_control


#Load Home page
def index(request):
    return render(request,'index.html')

# Register User
def register(request):
    if request.method=='POST':
        username = request.POST['name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if users.objects.filter(uname=username).exists():
            messages = "Username already exist"
            return render(request, 'registration.html', {"message": messages})
        elif password1 != password2:
            messages="Passwords does not match"
            return render(request, 'registration.html', {"message": messages})
        else:
            user = users(uname=username,pword=password1)
            user.save()
            return render(request, 'login.html')
    else:
        return render(request, 'registration.html')

#Get and Show feedback
def feeds(request):
    if request.method=='POST':
        uname = request.POST['Name']
        feedback=request.POST['feedback']
        ratings=request.POST['rating']
        if uname=='':
            feed = Feedback(name="Anonymous", cmnt=feedback, rating=ratings)
        else:
            feed = Feedback(name=uname, cmnt=feedback, rating=ratings)
        feed.save()
        return redirect('/feedback')
    else:
        feed = Feedback.objects.all()[:5]
        return render(request, 'feedback.html', {'feedback': feed})

#Login and Show User Details
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if users.objects.filter(uname=name).exists() and users.objects.filter(pword=password).exists():
            return render(request, 'index.html', {'name':name})
        else:
            return HttpResponse('Invalid Credentials')
    else:
        return render(request, 'login.html')

#Save the Users Details from User
def Put_Details(request, username):
        if request.method == 'POST':
            firstname = request.POST.get('fname')
            lastname = request.POST.get('lname')
            gen=request.POST.get('gender')
            phn=request.POST.get('phone')
            mail=request.POST.get('mail')
            address=request.POST.get('addr')
            sem = request.POST.get('semester')
            dep = request.POST.get('department')
            imag = request.FILES.get('pic')
            if StuDetails.objects.filter(uname=username).exists():
                messages = "Username already exist"
                return render(request, 'Student_details.html', {"message": messages})
            else:
                studentD = StuDetails(uname=username, fname=firstname, lname=lastname, gender=gen,phone_no=phn,email=mail,addr=address, semester=sem, department=dep, image=imag)
                studentD.save()
                context = StuDetails.objects.all().filter(uname=username)
                return render(request, 'Student_details.html', {'name': context})
        else:
            if StuDetails.objects.filter(uname=username).exists():
                context = StuDetails.objects.all().filter(uname=username)
                return render(request, 'Student_details.html', {'name': context})
            else:
                return render(request, 'Enter_details.html', {'name': username})

#Load Bsc IT page
def bscit(request):
    return render(request,'bsc_it.html')       

#load Notice Board
def notice(request):
    return render(request,'notice_board.html')         