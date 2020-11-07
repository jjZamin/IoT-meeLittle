###############################################################
#                                                             #
#                  ~    Written by    ~                       #
#                     Ghennadie Mazin                         #
#                                                             #
###############################################################
### --------------------------------------------------------###

import os

def write_file(name, data):
    try:
        f = open(name, 'w')
        f.write(data)
        f.close()
    except:
        print("cant write file")

def read_file(name):
    try:
        f = open(name, 'r')
        return f.read()
    except:
        print("can't read file")
    finally:
        f.close()

def delete_file(name):
    os.remove(name)
    
def find_txtFiles():
    flist = os.listdir()
    rlist = []
    for x in flist:
        if(x[-4:] == ".txt"):
            rlist.append(x)   
    return rlist
            
def find_pyFiles():
    flist = os.listdir()
    rlist = []
    for x in flist:
        if(x[-2:] == "py"):
            rlist.append(x)   
    return rlist

def is_on_list(name, dirc):
    flist = os.listdir(dirc)
    for x in flist:
        if(x == name):
            return True
    return False

def rename_file(name, rename):
    os.rename(name, rename)
