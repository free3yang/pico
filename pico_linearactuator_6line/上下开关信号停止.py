##该程序主要是对6芯接线的推杆进行检验使用
#6芯的接线推杆是2芯电机线直接接出，上下开关到位闭合的线路图
#实现的方式为 1.按特定要求接线，2按下按钮推杆伸出，到上开关后停止，3，再次按下按钮后缩回去到行程开关停止

##是否可以制作3个函数，一个电机正转函数，一个电机反转函数，一个电机停止函数，程序循环1秒监测一次开关信号

from machine import Pin,PWM
import utime
buttonstart= Pin(1,Pin.IN,Pin.PULL_UP)
keyup=Pin(17,Pin.IN,Pin.PULL_UP)
keydown=Pin(18,Pin.IN,Pin.PULL_UP)

pwm = PWM(Pin(15))
fx1=machine.Pin(8,machine.Pin.OUT)
fx2=machine.Pin(7,machine.Pin.OUT)
pwm.freq(1000)
zt=2
n=0
def turnR(): #伸出
    global zt
    fx1.value(1)
    fx2.value(0)         
    pwm.duty_u16(65025)
    utime.sleep(1)
    zt=1
def turnL(): #缩回
    global zt
    fx1.value(0)
    fx2.value(1)      
    pwm.duty_u16(65025)
    utime.sleep(1) #反应时间
    zt=0    

def turnoff():
    fx1.value(1)
    fx2.value(1)         
    pwm.duty_u16(65025)    


while True:
    print("进入循环",n)
    if (n == 0):
        if (buttonstart.value()==0):
            utime.sleep(0.01)
            if (buttonstart.value()==0):
                turnR()
                print("开始按钮按下",n)
                n=n+1
    if (keyup.value()==0):
        turnoff()
        print("上微动开关到位",zt)
    if (keydown.value()==0):
        turnoff()
        print("上微动开关到位",zt)
        
    if (zt == 1):
        if (buttonstart.value()==0):
            utime.sleep(0.01)
            if (buttonstart.value()==0):
                turnL()
    if (zt == 0):
        if (buttonstart.value()==0):
            utime.sleep(0.01)
            if (buttonstart.value()==0):
                turnR()



                           
                


