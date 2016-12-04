__revision__ = '1.0'  
__author__ = 'qz757' 
  
currentPath= r'D:\workstation\test'  
FILE_TYPE_LIST= ['py']  
  
if __name__ == '__main__':  
    import os  
    f = open('cscope.files','w')
    import sys
    PATH=sys.path
    PATH.append(currentPath)
    for p in PATH:
        for root,dirs,files in os.walk(p):  
            for file in files:  
                for file_type in FILE_TYPE_LIST:  
                    if file.split('.')[-1] == file_type:  
                        f.write('%s\n' %os.path.join(root,file))  
    f.close()  
    cmd = 'cscope -bk'  
    os.system(cmd)   
