from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from posts.forms import PostForm
from posts.models import Post

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		#print (form.cleaned_data.get("title"))
		instance.save()
		#message success
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
		
	#else:
		#messages.success(request," Not Successfully Created")
		

	#if request.method=="POST":
	#	print request.POST.get("content")
	#	print request.POST.get("title")
	#   Post.objects.create(title=title)
	context={
	    "form":form,
	}
	return render (request,"post_form.html",context)
	#return HttpResponse("<h1>Create</h1>")


def post_detail(request,id=None):#reterive
    #instance=Post.objects.get(id=5)
    instance=get_object_or_404(Post,id=id)
    context={
       "title":instance.title,
       "instance":instance
    }
    return render (request,"post_detail.html",context)
	#return HttpResponse("<h1>detail</h1>")

def post_list(request):  #list 
    queryset=Post.objects.all()
    context={
        "object_list":queryset,
    	"title":'List'
    }
   # if request.user.is_authenticated():
    #	context={
    #     "title":'My user list'
     #   }
    #else:
    #	context={
    #	   "title":'List'
    #	}
        
    return render (request,"post_list.html",context)
	#return HttpResponse("<h1>list</h1>")

def post_update(request,id=None):
	instance=get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request,"<a href='#'> Item </a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
        

	context={
       "title":instance.title,
       "instance":instance,
       "form":form
    }
	return render(request,"post_form.html",context)


def post_delete(request,id=None):
	instance=get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"Successfully Deleted")
	return redirect("posts:list")
			