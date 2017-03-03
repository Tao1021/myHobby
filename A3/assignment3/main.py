'''
Created on 3 Mar 2017

@author: Tao
'''

import time 
import urllib.request
import argparse



if __name__ == '__main__':
    pass


#filename ="/Users/Tao/Desktop/Workspace/Comp30670/A3/file_for_manual_test/input_assign2b.txt"

#filename ="/Users/Tao/Desktop/Workspace/Comp30670/A3/file_for_manual_test/input_assign2a.txt"
#filename ="/Users/Tao/Desktop/Workspace/Comp30670/A3/file_for_manual_test/input_assign2b.txt"
#create a empty 2-dimension array for data structure ;
#filename = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
Boardsize=0
x=0
Status=False
start_time = time.time()
def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    args = parser.parse_args()
    url=args.input
    print(url)
    return url


def read_Uri(fname):
    if fname.startswith('http'):
        uri = fname
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8').strip().split('\n')
    else:
        buffer = open(fname).read().strip().split('\n')
    return buffer

def SwitchCheckStatus(status):
    
    if(status==False):
        status=True
    else:
        status=False
    return status


def OnCheckStatus(status):
    
    return True

def OffCheckStatus(status):
    return False

def ChangeStatus(string,status):
    mystatus=False
   
    if(string=="off"):
        mystatus=OffCheckStatus(status)
        
        
               
    elif(string=="on"):
        mystatus=OnCheckStatus(status)
        
    else:
        mystatus=SwitchCheckStatus(status)
        
    
    
        
    return mystatus

def Check_Value(num):
    if(num<0):
        num=0
    
    return num

def Check_Over_size(num,boardsize):
    if(num>=boardsize):
        num=boardsize-1
    
    return num 
      
    
def Control_light(Board,string, x1,y1,x2,y2,boardsize):
    count=0
    x1=Check_Over_size(Check_Value(int(x1)), int(boardsize))
    x2=Check_Over_size(Check_Value(int(x2)), int(boardsize))
    #print("y1: " ,int(y1)," Boardsize: ",int(boardsize)) for trouble shooting 
    y1=Check_Over_size(Check_Value(int(y1)), int(boardsize))
    y2=Check_Over_size(Check_Value(int(y2)), int(boardsize))
    
    for m in range(min(int(x1),int(x2)),max(int(x1),int(x2))+1): #use min and max to reverse the value ;
        
        for n in range (min(int(y1),int(y2)),max(int(y1),int(y2))+1):
                        
                
            Board[m][n]= ChangeStatus(string, Board[m][n]) 
    
    for c in range(int(boardsize)):
        for d in range(int(boardsize)):
            
            if(Board[c][d]==True):
                count=count+1
          
    return count 
def mymain(): 
        filename=arg_parse()
        f=read_Uri(filename) 
#         f.splitlines()
        
        Boardsize=int(f[0]);
        print(Boardsize)
        
        LedBoard = [ [Status]*Boardsize for _ in range(Boardsize) ]
    
        for i,line in enumerate(f):
            #process line 
            if line.startswith("switch") or line.startswith("turn on") or line.startswith("turn off"):
                
                values = line.replace('turn ', '')
                values2 = values.replace(' through', '')
                #print("values2 : ",values2)
                values3 = values2.replace(' ', ', ')
                #print("values3: ",values3)
                values3a=values3.replace(',,',',')
                values3b=values3a.replace(', ,',',')
                values4 = values3b.replace(' ', '')
                #print(values4)
            
                values5 = values4.strip().split(",")
                #print(i, values5)
            
                print(Control_light(LedBoard,values5[0], values5[1], values5[2], values5[3], values5[4], Boardsize))
        print('finished')
        
            
            
#mymain()           
#print("--- %s seconds ---" % (time.time() - start_time))  
#finished 
#--- 178.7664909362793 seconds --- for d 

#finished
#--- 348.9808440208435 seconds --- for b 

# finished
# --- 161.65182375907898 seconds ---for c 


