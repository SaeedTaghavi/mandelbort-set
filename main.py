import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


def mandelbrot(z,c,exponent):
    return(z**exponent+c)

XMIN=-1.2
XMAX=1.
YMIN=-1.5
YMAX=1.5
XSTEPS=100
YSTEPS=100
exponent=2.725

Grid=[]
X=np.linspace(XMIN,XMAX,XSTEPS)
Y=np.linspace(YMIN,YMAX,YSTEPS)

for x in X:
    for y in Y:
        Grid.append((x,y))

print(len(Grid))

CUTOFF=2.0
NUMITER=100

Mandelbrot_value=[]

for g in tqdm(Grid):

    x,y=g
    c=np.complex(x,y)
    it=0

    z=0.0+0.0j
    SUCCESS=True

    while it<NUMITER:
        z=mandelbrot(z,c,exponent)
        if np.abs(z)>CUTOFF:
            SUCCESS=False
            break
        it+=1

    Mandelbrot_value.append(it)

minD=min(Mandelbrot_value)
maxD=max(Mandelbrot_value)

Output=[]
i=0
for x in X:
    row=[]
    for y in Y:
        row.append(maxD-Mandelbrot_value[i])
        i+=1
    Output.append(row)
    
plt.figure(figsize=(15,15))    
plt.imshow(Output,cmap='viridis')
plt.show()
