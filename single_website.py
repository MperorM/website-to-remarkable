import remarkable_functions as rf
import sys

if not len(sys.argv) == 3:
    print("not enough arguments please add a link and a filename")
    print('to upload a pdf of a website to your remarkable run:\n\npython remarkable_pdf.py <link to website> <name you want for the pdf>\n\n')
    exit()

retval = rf.create_and_upload_article(sys.argv[1], sys.argv[2], '')

if retval == 0:
    print('website successfully uploaded to remarkable')
if retval == -1:
    print('failure, unable to create pdf of website')
if retval == -2:
    print('failure, unable to upload file to remarkable')
if retval == -3:
    print('succesfully uploaded to remarkable, but failed to delete pdf from system, please delete pdf manually.')