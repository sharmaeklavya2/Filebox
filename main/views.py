from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import os

def base_response(request,body,h1=None):
	context_dict = {"base_body": body}
	if h1!=None:
		context_dict["base_h1"] = h1
	return render(request, "base.html", context_dict)

def save_uploaded_file(uploaded_file, overwrite=False):
	dest_file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
	with open(dest_file_path,"wb+") as dest_file:
		for chunk in uploaded_file.chunks():
			dest_file.write(chunk)

def upload(request):
	context_dict = {}
	if request.method=="POST":
		if "files" in request.FILES:
			file_list = request.FILES.getlist("files")
			for ufile in file_list:
				save_uploaded_file(ufile)
				print(type(ufile))
			context_dict["upload_success"] = "Files have been saved"
		else:
			return base_response(request,"Invalid data")
	return render(request, "upload.html", context_dict)
