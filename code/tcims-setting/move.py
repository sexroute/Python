import glob
import os
import re
import shutil
from pprint import pprint



filterSets = "Users|\.svn|\.settings|dml|tcims_pkg"
targetPath = r"tcims_j2ee\\src\\config"
target = "core"
# target = r"D:\NETS_TCIMS\tcims_j2ee\src\config"

class TcimsFilter(object):
	"""docstring for AppsFilter"""
	def __init__(self):
		super(TcimsFilter, self).__init__()
		self.result = []

	def _walkdir(self,dirname,filterSets,targetPath):
		try:
			ls = os.listdir(dirname)
		except Exception as e:
			raise e
		else:
			for l in ls:
				if re.findall(filterSets,l):
					continue
				temp = os.path.join(dirname, l)
				if(os.path.isdir(temp)):
					if re.findall(targetPath,temp):
						self.result.append([l,temp])
					self._walkdir(temp,filterSets,targetPath)
		return self.result

	def getDirs(self,dirname,filterSets,targetPath):
		if self.result != []:
			return self.result
		self._walkdir(dirname,filterSets,targetPath)
		return self.result

	def report(self,dirname,filterSets,targetPath,target):
		result = self.getDirs(dirname,filterSets,targetPath)
		for l in result:
			if re.findall(target,l[0]):
				print l[1]

	def copying(self,target,destination):
		for l in glob.glob("./"+target+"/*"):
			# print l, destination+"/"+l.split("\\")[-1]
			shutil.copyfile(l, destination+"/"+l.split("\\")[-1])

	def startCopying(self,dirname,filterSets,targetPath,target):
		self._walkdir(dirname,filterSets,targetPath)
		for l in self.result:
			if re.findall(target,l[0]):
				self.copying(target,l[1])






# for ls in glob.glob(r"D:\NETS_TCIMS\*\*"):
# 	print ls



tcims = TcimsFilter()
# tcims.report(r"D:\NETS_TCIMS",filterSets,targetPath,target)
tcims.startCopying(r"D:\NETS_TCIMS",filterSets,targetPath,target)


# def copyFile():
# 	shutil.copyfile("build.properties",r"D:\tmp\build.properties")
# copyFile()








class WeblogicConfig:
	"""docstring for WeblogicConfig"""
	@staticmethod
	def configmodify(configfile):
		with open(configfile, "r+") as config:
			configdata = config.read()
			print configdata.replace('opends-group-dev.paic.com.cn', 'aaa')

	@staticmethod
	def configsearch():
		for configpath in glob.glob(searchpath+r"\*"):
			configfile = configpath+r"\config\config.xml"
			if os.path.exists(configfile):
				WeblogicConfig.configmodify(configfile)
			else:
				pass
				# print configfile," is not exists."

# WeblogicConfig.configsearch()







def getDir():
	for root,dirs,files in os.walk(target):
		if re.findall(filterSets,root):
			print root
		else:
			for f in files:
				print root+f