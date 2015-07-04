# trips/views.py
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def hello_world(request):
#    return HttpResponse("Hello World!")
	return	render(request,'hello_world.html',{'current_time':datetime.now()})




def home(request):
	post_list = Post.objects.all()
	return render(request,'home.html',{'PostList':post_list})

def post_detail(request,id):
	post = Post.objects.get(id=id)
	return render(request, 'post.html',{'post':post})

# def hello_shawn(request):
# 	output = """
# 	<!DOCTYPE html>
# 	<html>
# 		<head>
# 			This is Head
# 		</head>
# 		<body>
# 			<p> Hello Shawn ! <em style="color:LightSeaGreen;">{current_time} </em> </p>
# 		</body>
# 	</html>
# 	""".format(current_time=datetime.now())

# 	return HttpResponse(output)