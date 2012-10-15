from django.shortcuts import render_to_response
from mysite.noteblog.models import *
from django.http import HttpResponseRedirect
from mysite.noteblog.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.create_user(
                username=form.cleaned_data['name'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
            )
            username = request.POST['name']
            password = request.POST['password']
            user_login = authenticate(username=username, password=password)
            login(request, user_login)
            return HttpResponseRedirect('/user/')
    else:
        form = RegistrationForm()
    return render_to_response('register.html',{'form':form})

def main_page(request):
    user = request.user
    page_id = request.GET.get('page_id','')
    now_page = 1
    if page_id:
        now_page = int(page_id)
    allnote = Noteblog.objects.count()
    
    if allnote%5 == 0:
        allpage = allnote/5
    else:
        allpage = allnote/5 + 1
    
    pageup = now_page - 1
    if now_page - 1 < 1:
        pageup = 1

    pagedown = now_page + 1
    if now_page + 1 > allpage:
        pagedown = allpage
    
    start = 5 * (now_page - 1)
    end = start + 5
    
    note = Noteblog.objects.all()[start: end]
    return render_to_response('main_page.html',locals())

@login_required(login_url='/login/')
def user_page(request):
    newtitle = request.POST.get('newtitle','')
    newnote = request.POST.get('newnote','')
    username = User.objects.get(username = request.user.username)
    note = Noteblog.objects.filter(user=username)
    if newtitle == '' and newnote == '':
        return render_to_response('conblog.html',locals())
    else:
        new = Noteblog(title=newtitle,context=newnote,category=Category.objects.get(id='3'),user=username)
        new.save()
        note = Noteblog.objects.filter(user=username)
        return HttpResponseRedirect('/user/')
        
def reply(request,parm1):
    re_context = request.POST.get('newreplay','')
    user = request.user
    if re_context != '':
        username = User.objects.get(username = request.user.username)
        note = Noteblog.objects.get(id=parm1)
        r_cont = Replay(name = re_context, user=username)
        r_cont.save()
        r_cont = Replay.objects.get(name = re_context)
        note.replays.add(r_cont)
        note.save()
        subnote = Noteblog.objects.get(id=parm1)
        return HttpResponseRedirect('/user/'+parm1)
    else:
        subnote = Noteblog.objects.get(id=parm1)
        return render_to_response('subnote.html',locals())

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')
    
