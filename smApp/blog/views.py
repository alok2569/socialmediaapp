from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post,comment,Profile
from .forms import PostFeed,CommentForm,UserForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages 

def feeds(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/index.html',{'posts':posts})

def post_new(request):
	if request.method=="POST":
		form = PostFeed(request.POST,request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('feed_detail',pk=post.pk)
	else:
		form = PostFeed()
	return render(request,'blog/add-feed.html',{'form':form})

def feed_detail(request, pk):
	post = get_object_or_404(Post,pk=pk)
	comments = post.comments
	new_comment = None
	if request.method == 'POST':
		commentform = CommentForm(data=request.POST)
		if commentform.is_valid():
			new_comment = commentform.save(commit=False)
			new_comment.post = post
			new_comment.author = request.user
			new_comment.save()
	else:
		commentform = CommentForm()
	return render(request,'blog/feed_detail.html',{'post':post,'comments':comments,'new_comment':new_comment,'commentform':commentform})

def delete_feed(request,pk):
	context = {}
	post = get_object_or_404(Post,pk=pk)
	if request.method == "POST":
		post.delete()
		return redirect('/')
	return render(request,'blog/delete_feed.html',context)

def feed_edit(request,pk):
	post = get_object_or_404(Post,pk=pk)
	form = PostFeed(request.POST or None, request.FILES or None, instance=post)

	if request.method=="POST":
		form.save()
		return redirect('feed_detail',pk=post.pk)
	return render(request,'blog/feed-edit.html',{'post':post})

def profile(request):
	return render(request,'blog/profile.html') 

def edit_profile(request):
	if request.method == "POST":
		userform = UserForm(request.POST, instance=request.user)
		profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if userform.is_valid() and profileform.is_valid():
			userform.save()
			profileform.save()
			messages.success(request, ('Your profile was successfully updated!'))
			return redirect('profile')
		else:
			messages.error(request, ('Please correct the error below.'))
	else:
		userform = UserForm(instance=request.user)
		profileform = ProfileForm(instance=request.user.profile)
	return render(request,'blog/edit_profile.html',{'userform':userform,'profileform':profileform})
