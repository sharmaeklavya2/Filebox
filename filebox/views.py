from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
import os

def base_response(request,body,h1=None):
	context_dict = {"base_body": body}
	if h1!=None:
		context_dict["base_h1"] = h1
	return render(request, "base.html", context_dict)

def get_folder_size_and_file_count(path):
	total_size = 0
	file_count = 0
	for dirpath, dirnames, filenames in os.walk(path):
		file_count+= len(filenames)
		for fname in filenames:
			fpath = os.path.join(dirpath, fname)
			total_size += os.path.getsize(fpath)
	return (total_size, file_count)

def save_uploaded_file(uploaded_file, overwrite=False):
	dest_file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)

	file_exists = os.path.isfile(dest_file_path)
	if file_exists and not overwrite:
		return "already_exists"
	if file_exists:	old_size = os.path.getsize(dest_file_path)
	else: old_size = 0

	folder_size, file_count = get_folder_size_and_file_count(settings.MEDIA_ROOT)
	if folder_size - old_size + uploaded_file.size > settings.FOLDER_SIZE_LIM:
		return "too_large"
	if not file_exists and file_count>=settings.FILE_COUNT_LIM:
		return "too_many"

	with open(dest_file_path,"wb+") as dest_file:
		for chunk in uploaded_file.chunks():
			dest_file.write(chunk)
	return "success"

message_map = {
	"success": "{0} was successfully saved",
	"already_exists": "{0} already exists",
	"too_large": "{0} does not fit because it is too large",
	"too_many": "{0} does not fit because the folder has too many files",
}

def upload(request):
	context_dict = {}
	if request.method=="POST":
		if "files" in request.FILES:
			file_list = request.FILES.getlist("files")
		else:
			file_list = []
		context_dict["status_list"] = []
		for ufile in file_list:
			retval = save_uploaded_file(ufile)
			print(ufile.name,type(ufile))
			message = message_map[retval].format(ufile.name)
			context_dict["status_list"].append(message)
	folder_size, file_count = get_folder_size_and_file_count(settings.MEDIA_ROOT)
	context_dict["num_remaining"] = settings.FILE_COUNT_LIM - file_count
	context_dict["mib_remaining"] = (settings.FOLDER_SIZE_LIM - folder_size)/(1024*1024)
	return render(request, "upload.html", context_dict)
