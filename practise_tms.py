x0 = 5
y0 = 2
x = float(input('enter any value for x: '))
y = float(input('enter any value for y: '))
def fun(x,y,x0,yo):
    distance= ((x-x0)**2+(y-y0)**2)**0.5
    return distance
print(fun(x,y,x0,y0))