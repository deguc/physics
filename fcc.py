from vpython import *

scene=canvas(forward=vector(-1,-0.5,-0.5),title='面心立方格子')


def draw_ffc(a=1,N=2):
    r=a*0.2

    for i in range(N+1):
        for j in range(N+1):
            for k in range(N+1):
            
                p=vector(a*i,a*j,a*k)-vector(N*a/2,N*a/2,N*a/2)
                l=vector(a/2,a/2,a/2)
                f1=vector(a/2,a/2,0)
                f2=vector(a/2,0,a/2)
                f3=vector(0,a/2,a/2)

                sphere(pos=p,radius=r,color=color.red)

                if i<N and j < N:  
                    sphere(pos=p+f1,radius=r,color=color.blue)
                if i<N and k<N:
                    sphere(pos=p+f2,radius=r,color=color.blue)
                if j<N and k<N:
                    sphere(pos=p+f3,radius=r,color=color.blue)

                if(i < N and j < N and k < N):
                    box(pos=p+l,size=vector(a,a,a),opacity=0.5)

def change_N(m):
    
    val = m.selected.replace('N=','')
    N = int(val)

    draw_ffc(N=N)


draw_ffc(N=1)

menu(choices=['N=1','N=2','N=3','N=4','N=5'],index=0,bind=change_N)

scene.waitfor('click')
