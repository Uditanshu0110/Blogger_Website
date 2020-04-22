from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def All_category():
    all_cat = Category.objects.all()
    return all_cat

def Popular_recent():
    allpost = Post.objects.all()
    recent_three = allpost[::-1][:3]
    likes = []
    post = []
    for i in allpost:
        li = PostLike.objects.filter(post_data = i).count()
        likes.append(li)
    for i in allpost:
        if max(likes)>0:
            m = max(likes)
            ind = likes.index(m)
            p = allpost[ind]
            post.append(p)
            likes.pop(ind)
            likes.insert(ind, 0)
    top_three = post[:3]
    return top_three,recent_three



from .models import *
def Home(request):
    allpost = Post.objects.all()
    top3,recent3 = Popular_recent()
    d = {"allcat":All_category(),"allpost":allpost,"top3":top3,
         "recent3":recent3}
    return render(request,'index.html',d)

def About(request):
    top3, recent3 = Popular_recent()
    d = {"allcat":All_category(),"top3":top3,
         "recent3":recent3}
    return render(request,'about.html',d)

def Contact(request):
    d = {"allcat":All_category()}
    return render(request,'contact.html',d)

def Login(request):
    error = False
    if request.method == "POST":
        dd = request.POST
        p = dd['pwd']
        u = dd['user']
        user = authenticate(username=u,password = p)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error = True



    d = {"allcat": All_category(),"error":error}
    return render(request,'login.html',d)

def Blog_detail(request,bid):
    blog_data = Post.objects.get(id = bid)

    d = {"allcat": All_category(),"detail":blog_data}
    return render(request,'singlepage.html',d)

def LikeThePost(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Post.objects.get(id = pid)
    user = request.user
    data2 = PostLike.objects.filter(post_data = data,usr = request.user)
    if not data2:
       PostLike.objects.create(post_data = data,usr = user,like =True)
    return redirect('home')
from datetime import date
def CommentThePost(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        c = request.POST['msg']
        user = request.user
        td = date.today()
        postdata = Post.objects.get(id = pid)
        PostComment.objects.create(usr = user,post_data=postdata,comment = c
                                   ,date = td)

    return redirect('detail',pid)

def Signup(request):
    error = False
    if request.method == "POST":
        dd = request.POST
        n = dd['name']
        u = dd['user']
        p = dd['pwd']
        e = dd['em']
        i = request.FILES['img']
        udata = User.objects.filter(username=u)
        if udata:
            error = True
        else:
            user = User.objects.create_user(username=u,password=p,email=e,
                                     first_name = n)
            UserDetail.objects.create(usr = user,image = i)
            return redirect('login')


    d = {"allcat": All_category(),"error":error}
    return render(request,'signup.html',d)


def Logout_user(request):
    logout(request)
    return redirect('login')


def MyBlog(request):
    allblogs = Post.objects.filter(usr = request.user)
    d = {"allblogs":allblogs,"allcat": All_category()}
    return render(request,'fashion.html',d)

def Delete_post(request,pid):
    data = Post.objects.get(id = pid)
    data.delete()
    return redirect('blogs')

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
def Add_Blog(request):
    d = {"allcat": All_category()}
    if request.method == "POST":
        dd = request.POST
        c = dd['cat']
        t = dd['title']
        s = dd['short']
        lt = dd['long']
        i = request.FILES['img']
        u = request.user
        td = date.today()
        catdata = Category.objects.get(id = c)
        Post.objects.create(cat = catdata,usr = u,title=t,
                            short_des =s,long_des = lt,
                            image = i,date = td)
        to_mail = request.user.email
        from_mail = settings.EMAIL_HOST_USER
        sub = "BLOG DETAIL"
        msg = EmailMultiAlternatives(sub,'',from_mail,[to_mail])
        dic = {"name":request.user.username,'title':t,
               "short":s}
        html = get_template('mail.html').render(dic)
        msg.attach_alternative(html,'text/html')
        msg.send()

        return redirect('blogs')
    return render(request,'add_blog.html',d)

def Category_detail(request,cid):
    catdata = Category.objects.get(id = cid)
    d = {"catdata": catdata, "allcat": All_category()}
    return render(request,'category_detail.html',d)


def Chenge_image(request):
    userdata = UserDetail.objects.filter(usr=request.user).first()
    d = {"userdata": userdata, "allcat": All_category()}
    if request.method == "POST":
        i = request.FILES['img']
        userdata.image = i
        userdata.save()
        return redirect('blogs')
    return render(request,'change_image.html',d)


def Change_password(request):
    error = False
    if request.method == "POST":
        o = request.POST['old']
        n = request.POST['new']
        user = authenticate(username = request.user.username,
        password = o)
        if user:
            user.set_password(n)
            user.save()
            logout(request)
            login(request,user)
            return redirect('blogs')
        else:
            error = True
    d = {"error": error, "allcat": All_category()}
    return render(request, 'change_pwd.html',d)
