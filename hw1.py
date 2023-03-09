import pylab
import numpy as np
import math
from scipy import integrate

def func(x):       
    return math.sin(3*x)*math.sin(3*x)*math.cos(3*x)
isum,err = integrate.quad(func,0,0.5*math.pi)
pi = pylab.pi
a,b,n= 0,pi/2,100
fn = lambda x:pylab.sin(3*x)**2*pylab.cos(3*x)
xs,h=pylab.linspace(a,b,n+1,retstep=True)
ys = pylab.sin(3*xs)**2*pylab.cos(3*xs)

rsum , lsum, usum , tsum = 0,0,0,0
y1 = ys[0]
for y2 in ys[1:]:
    rsum += y1
    if y1<y2:
        lsum += y1
        usum += y2
    else:
        lsum +=y2
        usum +=y1
    tsum += y1+y2
    y1=y2
rsum *= h
lsum *= h
usum *= h
tsum *= h/2
isum1=h*sum(ys[:-1])
print("數學積分    :",round(isum,9),end="\n\n")
print("迴圈求積:")
print("矩形積分    :",round(isum1,9)," 誤差:",round(abs(isum-isum1),10))
print("上矩形積分  :",round(usum,9),"誤差:",round(abs(isum-usum),10))
print("下矩形積分  :",round(lsum,9),"誤差:",round(abs(isum-lsum),10))

