import os
import glob
import shutil
import logging
from os import path

#The glob module finds all the pathnames matching a specified pattern according to the path name.Here it will return all the paths from the given expression.
filename=glob.glob('/home/chinmay/Downloads/*')

#Create and configure logger
logging.basicConfig(filename="/home/chinmay/Downloads/logfile.log", format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filemode='a')
#Creating an object
logger=logging.getLogger()
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#We declare the list of folders which should be created according to the file extension present in the Source folder(here in this script it is Downloads folder) alongwith the extensions of files which should be included in our destination folder.
Documents = ['.pdf','.docx','.doc','.txt','.odt','.ppt','.pptx','.csv']
Media = ['.jpeg','.jpg','.svg','.png','.PNG','.mp4','.mp3']
Compressed_files = ['.zip','.tar.gz','.rar','.tar.bz2','.deb']
Setup_files = ['.exe','.msi','.sh']
Program_files = ['.py','.py3','.html','.css','.php','.cpp','.c','.js','.ipynb']

#Path of the destination folder
docs_path = '/home/chinmay/Downloads/Documents'
media_path = '/home/chinmay/Downloads/Media'
compressed_path = '/home/chinmay/Downloads/Compressed_files'
setup_path = '/home/chinmay/Downloads/Setup_files'
program_path = '/home/chinmay/Downloads/Program_files'

for i in filename:
	if os.path.splitext(i)[1] in Documents:		#It splits the file into path name and path extension we will use only extension
		if(path.exists(docs_path)):				#Check whether the path exists
			shutil.move(i,docs_path)			#Shutil module helps in automating process of moving the files from source to destination
			logger.info(i + " Moved from Downloads to Documents")
		else:
			os.mkdir(docs_path)					#If path does not exist create the folder from the given path
			shutil.move(i,docs_path)			#Moves the file from source to destination
			logger.info(i + " Moved from Downloads to Documents")

	if os.path.splitext(i)[1] in Media:
		if(path.exists(media_path)):
			shutil.move(i,media_path)
			logger.info(i + " Moved from Downloads to Media")
		else:
			os.mkdir(media_path)
			shutil.move(i,media_path)
			logger.info(i + " Moved from Downloads to Media")

	if os.path.splitext(i)[1] in Compressed_files:
		if(path.exists(compressed_path)):
			shutil.move(i,compressed_path)
			logger.info(i + " Moved from Downloads to Compressed_files")
		else:
			os.mkdir(compressed_path)
			shutil.move(i,compressed_path)
			logger.info(i + " Moved from Downloads to Compressed_files")

	if os.path.splitext(i)[1] in Setup_files:
		if(path.exists(setup_path)):
			shutil.move(i,setup_path)
			logger.info(i + " Moved from Downloads to Setup_files")
		else:
			os.mkdir(setup_path)
			shutil.move(i,setup_path)
			logger.info(i + " Moved from Downloads to Setup_files")

	if os.path.splitext(i)[1] in Program_files:
		if(path.exists(program_path)):
			shutil.move(i,program_path)
			logger.info(i + " Moved from Downloads to Program_files")
		else:
			os.mkdir(program_path)
			shutil.move(i,program_path)
			logger.info(i + " Moved from Downloads to Program_files")
