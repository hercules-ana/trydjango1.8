from django.shortcuts import render

def about(request):
	title = "Welcome"
	
	if request.user.is_authenticated():
		title = "My title %s" %(request.user)
	context = {
		"title": title,
	}
	return render(request, "about.html", context)