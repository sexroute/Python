import threading, zipfile, time, thread

class AsyncZip(threading.Thread):
	"""docstring for AsyncZip"""
	def __init__(self, infile, outfile):
		threading.Thread.__init__(self)
		self.infile = infile
		self.outfile = outfile
	def run(self):
		f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
		f.write(self.infile)
		f.close()
		time.sleep(10)
		print 'Finished background zip of: ', self.infile

# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
# print 'The main program continues to run in foreground'
# background.join(5)
# print 'Main program waited until background was done.'




mylock = thread.allocate_lock()  #Allocate a lock  
num=0  #Shared resource  
  
def add_num(name):  
    global num  
    while True:  
        mylock.acquire() #Get the lock   
        # Do something to the shared resource  
        print 'Thread %s locked! num=%s'%(name,str(num))  
        if num >= 5:  
            print 'Thread %s released! num=%s'%(name,str(num))  
            mylock.release()  
            thread.exit_thread()  
        num+=1  
        print 'Thread %s released! num=%s'%(name,str(num))  
        mylock.release()  #Release the lock.  
  
def test():  
    thread.start_new_thread(add_num, ('A',))  
    thread.start_new_thread(add_num, ('B',))
# test()



mlock = thread.allocate_lock()
num = 0

def add_num(name,arg):
	print arg 
	global num
	while True:
		mlock.acquire()
		print 'Thread %s locked! num=%s'%(name,str(num))
		if num >= 5:
			print 'THread %s release! num=%s'%(name,str(num))
			mlock.release()
			thread.exit_thread()
		num += 1
		print 'Thread %s release! num=%s'%(name,str(num))
		# mlock.release()


# thread.start_new_thread(add_num,('A',1,))
# thread.start_new_thread(add_num,('B',2,))




mylock02 = threading.RLock()
num = 0
class myThread(threading.Thread):
	"""docstring for mhThread"""
	def __init__(self, name):
		super(myThread, self).__init__()
		self.name = name
	
	def run(self):
		global num
		while True:
			mylock02.acquire()
			print '\nThread(%s) locked, Number: %d'%(self.name,num)
			if num >= 4:
				mylock02.release()
				print '\nThread(%s) released, Number: %d'%(self.name, num)
				break
			num += 1
			print '\nThread(%s) released, Number: %d'%(self.name,num)
			mylock02.release()

def test02():
	thread01 = myThread('A')
	thread02 = myThread('B')
	thread01.start()
	thread02.start()

# test02()




import threading
import random
import time

class MyThread(threading.Thread):

    def run(self):
        wait_time=random.randrange(1,4)
        print "%s will wait %d seconds" % (self.name, wait_time)
        time.sleep(wait_time)
        print "%s finished!" % self.name

if __name__=="__main__":
    threads = []
    for i in range(5):
        t = MyThread()
        # t.setDaemon(True)
        t.start()
        threads.append(t)
    print '\nmain thread is waitting for exit...'        
    # for t in threads:
    #     t.join()
        
print 'main thread finished!'