import pdfkit
import subprocess
import re

def create_and_upload_article(link, filename, destination_folder):
    '''
    spawns a subprocess that uploads an article to remarkable
    :param link: website link to create pdf from
        filename: name for the pdf
        destination_folder: destination folder in the remarkable tablet
    :return
        success: 0
        failure, pdf couldn't be created: -1
        failure, remarkable upload failed: -2
        failure, file deletion failed: -3
    '''
    # create pdf, return on failure
    try:
        pdfkit.from_url(link, filename)
    except Exception as inst:
        print(inst)
        return -1
    # upload pdf to remarkable
    proc = subprocess.Popen([f'./rmapi put {filename} /{destination_folder}'], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if out and err != None:
        return -2
    # delete pdf from system
    proc = subprocess.Popen([f'rm {filename}'], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if out and err != None:
        return -3
    # success
    return 0


def remove_article(folder, filename):
    '''
    removes an article from the remarkable
    :param
        file_path: path to remarkable file location
    :return
        sucess: 0
        failure: -1
    ''' 
    proc = subprocess.Popen([f'./rmapi rm {folder}/{filename}'], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if out and err == None:
        return 0
    else:
        return -1


def sanitize_file_name(filename):
    return re.sub(r'\W+', '', filename)