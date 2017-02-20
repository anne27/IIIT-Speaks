from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.shortcuts import get_object_or_404
from .forms import BlogForm
# Create your views here.
def home(request):
	context = {}
	return render(request, "first_page.html", context)

def logoutUser(request):
    logout(request)
    return render(request, "first_page.html", {})

def SignUp(request):
	errors = []
	if request.method == 'POST':
		username, password, email = request.POST['username'], request.POST['pass'], request.POST['email'] 
		first, last = request.POST['first'], request.POST['last']
		existing = User.objects.filter(username__iexact=username)
		if existing.exists():
			errors.append('username already exists')
		else:
			user = User.objects.create_user(username, email, password)
			user.first_name = first
			user.last_name = last
			user.is_active = True
			user.save()
			return HttpResponseRedirect("/login")

	context = {
			"errors": errors
			}
	return render(request, 'signup.html', context)

def loginUser(request):
	error = None
	context = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['pass']
		user = authenticate(username=username, password=password)
		if user is not None:
			if(user.is_active):
				login(request, user)
				return redirect("myfeed")
			else:
				error = 'your account is not active'
		else:
			error = 'Invalid Credentials'
	context = {
		"error" : error
	}

	return render(request, "login.html", context)

@login_required
def myFeed(request):
	listOfBlogs = []
	user_loggedin = request.user
	blog_query = Blog.objects.filter(Author = user_loggedin)
	# print (user_loggedin)
	for i in blog_query:
		listOfBlogs.append(i)
	context = {
	 "listBlogs" : listOfBlogs,

	}
	return render(request, "feed.html", context)

def rssFeed(request):
	listOfBlogs = []
	user_loggedin = request.user
	blog_query = Blog.objects.all()
	for i in blog_query:
		listOfBlogs.append(i)
	context = {
	 "listBlogs" : listOfBlogs,

	}
	return render(request, "rssfeed.html", context)


@login_required
def addBlog(request):
	form = BlogForm(request.POST or None)


	context = {
		"form": form,
	}
	if form.is_valid():
		currentBlog = form.save(commit=False)
		currentBlog.Author = User.objects.get(username__iexact = request.user)
		currentBlog.save()
		return HttpResponseRedirect("/myfeed")


	return render(request, "addblog.html", context)

# @login_required
# def getPost(request, slug):
# 	post = get_object_or_404(Post, slug=slug)
# 	context = {"posts": post}
# 	return render(request, "getpost.html", context)






# @login_required
# def addBlog(request):
# 	form = BlogForm(request.POST or None)


# 	context = {
# 		"form": form,
# 	}

# 	if form.is_valid:
# 		currentBlog = form.save(commit=False)
# 		currentBlog.Author = User.objects.get(username = request.user)
# 		currentBlog.save()
# 		return HttpResponseRedirect("/myfeed")


# 	return render(request, "addblog.html", context)

# @login_required
# def getPost(request, slug):
# 	post = get_object_or_404(Post, slug=slug)
# 	context = {}
# 	return render(request, "getpost.html", context)


