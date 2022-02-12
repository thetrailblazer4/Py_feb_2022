from django.shortcuts import render

# Create your views here.


posts = [
	{
		'author': 'Tom',
		'title' : 'Post 1',
		'content': 'First Post Content',
		'date_posted' : 'Feb 10, 2022'
	},
	{
		'author': 'John',
		'title' : 'Post 2',
		'content': 'Second Post Content',
		'date_posted' : 'Feb 11, 2022'
	}

]


def home(request):

	context = {

		'posts' : posts
	}
	
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})



