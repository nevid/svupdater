# CergioSoft (c) 2018
# http://svsoft.svhome.org

import os
import shutil
import zipfile
import sys
import datetime

dstdir="" #"c:/Temp/testupd"
srcdir="" #"testdir" #"."

if(len(sys.argv)!=3):
	print("usage: svupdater fromdir todir")
	#quit()
	sys.exit(0)
	

srcdir=sys.argv[1]
dstdir=sys.argv[2]

def OpenZip(dir,zipname):
	today = datetime.datetime.today()
	zname=zipname+"_"+today.strftime("%Y-%m-%d-%H.%M.%S")+".zip"
	print("zipfile:",zname)
	zf = os.path.join(dir,zname) 
	zipfl = zipfile.ZipFile(zf, mode='w')
	return zipfl


def BeforCpy(zipfl,srcpath,dstpath):
	#print (srcpath,dstpath)
	curd=os.getcwd()
	os.chdir(dstdir)
	zp=os.path.relpath(dstpath,dstdir)
	print ("tozip",zp)
	try:
		zipfl.write(zp)
	finally: 
		os.chdir(curd)
		#print("fin")
		return
	#return


try:   
	zipfl=OpenZip(dstdir,"upd")   
except Exception as e:
	print ("Error({0}): {1}".format(e.errno, e.strerror))
	sys.exit(1)
		
	

try:
	tree = os.walk(srcdir) 
except:
	print ("Error({0}): {1}".format(e.errno, e.strerror))

#print (tree)

for dpath, dirs, files in tree:
	#print (dirs)
	#print (files)
	#print(dpath)
	#for d in dirs:
		#print (d)
		#path = os.path.join(d,files) 
		#print(path)
	
	for f in files:
		path = os.path.join(dpath,f) 
		#print ("path",path)
		#print(f)
		relp=os.path.relpath(path,srcdir)
		#print("relp",relp)
			
		dstpath = os.path.join(dstdir,relp) 
		#print (dstpath)
		dr=os.path.dirname(dstpath) 

		if (os.path.isdir(dr)==False):
			try:
				os.makedirs(dr)
			except:
				pass
	

		
		BeforCpy(zipfl,path,dstpath)
		
		try:
			print ("Copy",path,dstpath)
			shutil.copy(path,dstpath)
		except Exception as e:
		#except IOError as e:
			#print ("I/O error({0}): {1}".format(e.errno, e.strerror))
			print ("Error({0}): {1}".format(e.errno, e.strerror))
		
		
		
		

	
	
	
	
	

