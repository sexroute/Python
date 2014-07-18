__author__ = 'CHENGSIQIN754'

def ioStart01():
    f = open(r"D:\python.txt", 'w')
    print type(f)
    # f.writable()
    f.write('Hello, ')
    f.writelines(("World!", "World!", 'Now!'))
    f.close()

    f = open(r"D:\python.txt", 'r')
    print f.read(4)
    print f.read()

def ioStart02():
    try:
        file = open(r"D:\python.txt")
        pass
    finally:
        file.close()
    with open(r"D:\python.txt") as somefile:
        print somefile.read()

class IoStart03:
    def simpleText(self):
        with open(r"D:\somefile.txt", 'w') as somefile:
            somefile.write("""Welcome to this file
There is nothing here except
This stupid haiku""")
    def read(self):
        f = open(r"D:\somefile.txt")
        for i in range(3):
            print str(i) + ': ' + f.readline()
# IoStart03().simpleText()
# IoStart03().read()

def process(string):
    print 'Processing: ', string
def iostart04():
    f = open(r"D:\somefile.txt")
    while True:
        line = f.readline()
        if not line:
            break
        process(line)
    f.close()
# iostart04()

def ioStart05(var):
    if not var:
        print 'not var'
    else:
        print 'else'
# ioStart05(None)

def ioStart06():
    for line in open(r"D:\somefile.txt"):
        process(line)
# ioStart06()

import sys
def ioStart07():
    for line in sys.stdin:
        process(line)
# ioStart07()



import sys
def ioStart08():
    text = sys.stdin.read()
    words = text.split()
    worddcount = len(words)
    print 'Wordcount:', worddcount

