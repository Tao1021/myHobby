'''
Created on 3 Mar 2017

@author: Tao
'''
from nose.tools import *
from assignment3.main import *


#
#The following test are for basic light status changes

a = "Switch"
b = "on"
c = "off"
def test_SwitchCheckStatus():
    assert True == SwitchCheckStatus(False)
    
def test_SwitchCheckStatus2():
    assert False == SwitchCheckStatus(True)
def test_changelights():
    assert True == ChangeStatus(a, False)
def test_changelights2():
    assert False == ChangeStatus(a, True)    
 
def test_changelights3():
    assert True == ChangeStatus(b, True)
def test_changelights4():
    assert True == ChangeStatus(b, False)
def test_changelights5():
    assert False == ChangeStatus(c, True)
def test_changelights6():
    assert False == ChangeStatus(c, False)


mynum1=100
mynum2=-200
mynum3=10000

boardsize = 1000
def test_check_overSize():
    assert mynum1 == Check_Over_size(mynum1,boardsize)
def test_check_overSize2():
    assert 999 == Check_Over_size(mynum3,boardsize)
def test_check_value():
    assert 0 == Check_Value(mynum2)
def test_check_value2():
    assert mynum1 == Check_Value(mynum1)   
 
size=3
#  
def test_ControlLight():
    board=[ [True]*size for _ in range(size) ]
    d="switch"
    board[1][1]=False
    board[2][2]=False
    assert 2==Control_light(board,d, 0,0,2,2,size)  
def test_ControlLight2():
    board=[ [True]*size for _ in range(size) ]
    d="on"
    board[1][1]=False
    board[2][2]=False
    assert 9==Control_light(board,d, 0,0,2,2,size) 
def test_ControlLight3():
    board=[ [True]*size for _ in range(size) ]
    d="off"
    board[1][1]=False
    board[2][2]=False
    assert 0==Control_light(board,d, 0,0,2,2,size) 
 
 
# # this test for handling negative numbers or oversized number in my code ;
def test_ControlLight4():
    board=[ [True]*size for _ in range(size) ]
    d="off"
    board[1][1]=False
    board[2][2]=False
    assert 0==Control_light(board,d, -1,0,255,20,size)
# This test is for handling the situation when x1 > x2 or y1>y2;
def test_ControlLight5():
    board=[ [True]*size for _ in range(size) ]
    d="switch"
    board[1][1]=False
    board[2][2]=False
    assert 2==Control_light(board,d, 2,0,0,2,size) 
  
