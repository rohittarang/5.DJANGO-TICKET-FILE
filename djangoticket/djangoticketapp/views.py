from django.shortcuts import render, redirect
from .models import *
from django.contrib import auth
from django.core.files.storage import FileSystemStorage

# Create your views here.

def registerpage(request):
    return render(request, 'register.html')

def index(request):
    if request.method == "POST":
        if request.POST['loginrole'] == "User":
            vlurole = request.POST['loginrole']
            uname = request.POST['frontusername']
            psw = request.POST['frontpassword']
        
            try:
                newuser = Register.objects.get(musername=uname)
        
                if newuser:
                    if newuser.mpassword == psw:
                        request.session['loginrole'] = newuser.murole
                        request.session['frontusername'] = newuser.musername
                        request.session['frontpassword'] = newuser.mpassword
                        message = "Login Successfully"
                        return render(request,'ticketview.html',{'msg':message})
                    else:
                        message = "Password does not match"
                        return render(request,'index.html',{'msg':message})
                else:
                    message = "User does not exist"
                    return render(request,'index.html',{'msg':message})
            except:
                return render(request,'index.html')
        else:
            if request.POST['loginrole'] == "Admin":
                vlarole = request.POST['loginrole']
                uname = request.POST['frontusername']
                psw = request.POST['frontpassword']
        
                try:
                    newuser = Register.objects.get(musername=uname)
        
                    if newuser:
                        if newuser.mpassword == psw:
                            request.session['loginrole'] = newuser.marole
                            request.session['frontusername'] = newuser.musername
                            request.session['frontpassword'] = newuser.mpassword
                            message = "Admin Login Successfully"
                            return render(request,'ticketview.html',{'msg':message})
                        else:
                            message = "Password does not match"
                            return render(request,'index.html',{'msg':message})
                    else:
                        message = "Admin does not exist"
                        return render(request,'index.html',{'msg':message})
                except:
                    return render(request,'index.html')
            return render(request,'index.html')
    else:
        return render(request,'index.html')
    
########################### ORIGINAL ###########################

# def registeruser(request):
#     if request.method == "POST":
#         if request.POST['role'] == "User":
#             runame = request.POST['registerusername']
#             rpsw = request.POST['registerpassword']
#             try:
#                 ruser = Register.objects.filter(musername=runame)
#                 print(ruser)
#                 if ruser:
#                     message = "User Already Exists"
#                     return render(request,'register.html',{'msg':message})
#                 else:
#                     newruser = Register.objects.create(musername=runame, mpassword=rpsw)
#                     message = "User Created"
#                     return render(request,'index.html',{'msg':message})
#             except:
#                 return render(request,'index.html')

def registeruser(request):
    if request.method == "POST":
        if request.POST['registerrole'] == "User":
            vurole = request.POST['registerrole']
            runame = request.POST['registerusername']
            rpsw = request.POST['registerpassword']

            try:
                ruser = Register.objects.filter(musername=runame)
                print(ruser)
                if ruser:
                    message = "User Already Exists"
                    return render(request,'register.html',{'msg':message})
                else:
                    newruser = Register.objects.create(murole=vurole, musername=runame, mpassword=rpsw)
                    message = "User Created"
                    return render(request,'index.html',{'msg':message})
            except:
                return render(request,'index.html')
        else:
            if request.POST['registerrole'] == "Admin":
                varole = request.POST['registerrole']
                runame = request.POST['registerusername']
                rpsw = request.POST['registerpassword']
                try:
                    ruser = Register.objects.filter(musername=runame)
                    print(ruser)
                    if ruser:
                        message = "Admin Already Exists"
                        return render(request,'register.html',{'msg':message})
                    else:
                        newruser = Register.objects.create(marole=varole,musername=runame, mpassword=rpsw)
                        message = "Admin Created"
                        return render(request,'index.html',{'msg':message})
                except:
                    return render(request,'index.html')
            else:
                return render(request,'index.html')
    else:
        return render(request,'index.html')
        

def ticketview(request):
    tno = request.POST['ticketno']
    sdetails = request.POST['serverdetails']
    sdate = request.POST['senddate']
    lno = request.POST['licenseno']
    vfile = request.FILES['uploadfile']
    fs = FileSystemStorage()
    filename = fs.save(vfile.name, vfile)
    uploadedviewfile = fs.url(filename)
    
    newticket = Ticket.objects.create(ticketno=tno, serverdetails=sdetails, senddate=sdate, licenseno=lno, mfile=vfile)
    newticket.save()
    
    return redirect('showticket')

def showticket(request):
    all_data = Ticket.objects.all()
    return render(request, 'showticket.html',{'key1':all_data})

def logout(request):
    auth.logout(request)
    return render(request,'index.html')

