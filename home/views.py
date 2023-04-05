from django.shortcuts import render, redirect

# Create your views here.

from .form import *
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("/")

def homepage(request):
    context = {'blogs': BlogModel.objects.all()}

    return render(request, 'home.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect("/user_panel/")
    else:
        return render(request, 'login.html')

def subscribe(request):
    return render(request, 'subscribe.html')

def blog_detail(request, slug):
    context = {}
    try:
      blog_obj = BlogModel.objects.filter(slug = slug).first()
      context['blog_obj'] = blog_obj
      context['blogs'] = BlogModel.objects.exclude(slug=slug)
      context['blogs'] = context['blogs'].filter(genre=blog_obj.genre)
      context['views'] = blog_obj.views + 1
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

def update_blog(request, slug):
    context = {}
    try:

        blog_obj = BlogModel.objects.get(slug=slug)

        if blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image
            )

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)

    return render(request, 'update_blog.html', context)

  
def user_panel(request):
    context = {}

    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)

    print(context)
    return render(request, 'user_panel.html', context)

def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES.get('image', '')
            title = request.POST.get('title')
            user = request.user
            genre = request.POST.get('radoption')
            genre = str(genre)

            if form.is_valid():
                print('Valid')
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user=user, title=title,
                content=content, image=image, genre=genre,  
            )
            print(blog_obj)

          
            return redirect('/user_panel/')
    except Exception as e:
        print(e)

    return render(request, 'add_blog.html', context)

def delete_blog(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)

    return redirect('/user_panel/')

