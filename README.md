# Filebox

Using this webapp, users can upload files to a folder on the server. There is a limit on the size of the folder and the maximum number of files the folder can have.

To set these limits, make the files `project_conf/file_count_lim.txt` and `project_conf/folder_size_lim.txt`. These files should have a single integer.

If a user uploads a file which exceeds the folder size limit, it will be downloaded and later deleted. To work around this issue, set a limit on the maximum upload size in your webserver.
