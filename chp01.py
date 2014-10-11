__author__ = 'ninglu'
import scipy as sp
data = sp.genfromtxt("web_traffic.tsv",delimiter="\t")
print(data.shape)

x = data[:,0]
y = data[:,1]

x= x[~sp.isnan(y)]
y= y[~sp.isnan(y)]




def error(f,x,y):
    return sp.sum((f(x)-y)**2)

fp1, res, rank, sv, rcond= sp.polyfit(x,y,1,full=True)

f1 = sp.poly1d(fp1)
print error(f1,x,y)

inflection = 3.5*7*24
xa=x[:inflection]
ya=y[:inflection]
xb=x[inflection:]
yb=y[inflection:]

fa=sp.poly1d(sp.polyfit(xa,ya,True))
fb=sp.poly1d(sp.polyfit(xb,yb,1))

fa_error=error(fa,xa,ya)
fb_error=error(fb,xb,yb)

print('Error inflection=%f'% (fa_error+fb_error))


fbt2=sp.polyfit(x,y,2)
print fbt2


import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range((10))],['week %i'%w for w in range(10) ])
plt.autoscale(tight=True)

fx_a = sp.linspace(0,x[inflection],1000)
fx_b = sp.linspace(x[inflection],x[-1],1000)
plt.plot(fx_a,fa(fx_a),'r-',linewidth=4)
plt.plot(fx_b,fb(fx_b),'g-',linewidth=4)
plt.legend(['dim=%i'% fa.order,'dim=%i'% fb.order],loc="upper left")
plt.grid()
plt.show()