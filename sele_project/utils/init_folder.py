import os, datetime

def init_html_folder(data):
    html_folder_path = './../report/html/'
    folder_path = html_folder_path + data
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def init_png_folder(data):
    html_folder_path = './../report/html/'
    folder_path = html_folder_path + data
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

date_time = datetime.datetime.now()
print(date_time.strftime('%Y-%m-%d-%H-%M-%S'))


#init_html_folder('20-07-15')