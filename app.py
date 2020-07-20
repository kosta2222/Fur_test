import numpy as np
from util import get_logger
import logging

Forward=1
Backward=-1
import math
import matplotlib.pyplot as plt

def plot(_file:str,label:str,x:list,y:list,logger:logging.Logger)->None:
    
    fig:plt.Figure=None
    ax:plt.Axes=None
    fig, ax=plt.subplots()
    plt.text(1,0, label)
    print(label)
    ax.plot(x,y)
    plt.xlabel('Gercs')
    plt.ylabel('Amplitude')
    ax.legend()
    plt.savefig(_file)
    print("Graphic saved")
    logger.info("Graphic saved")
    plt.show()

def DFT_slow(x):
    x=np.asarray(x, dtype=float)
    
    N=x.shape[0]
    
    n=np.arange(N)
    
    k=n.reshape((N,1))
    
    M=np.exp(-2j * np.pi * k * n / N)
    
    dot_=np.dot(M, x)
    return dot_
       

#def dft(data:list, direction:int)->tuple:
    #n = len(data) # Сколько элементов в data
    #arg = 0
    #cos = 0
    #sin = 0
    #dst = [Complex(0,0)] * n
    #for i in range(n):
        #arg=- direction * 2.0 *math.pi * i / n # i индекс данного сигнала в data
        
        #for j in range(n):
            #cos = math.cos( j * arg )
            #sin = math.sin( j * arg )
            #dst[i].real+=(data[j].real* cos - data[j].imag * sin)
            #dst[i].imag+=(data[j].real * sin + data[j].imag * cos)
    #if direction==Forward:
        #for i in range(n):
            #data[i].real=dst[i].real/n
            #data[i].imag=dst[i].imag        
    #return dst


(push_i, push_fl, push_str, push_obj,dft_,rfft_,fft_,dft_slow,plot_,fftfreq_,noarg) = range(11)


def vm(buffer, loger=None, date=None):
    len_ = 25
    data=None
    out=None
    x=None
    y=None    
    if loger:
        loger.info(f'Log started {date}')
    vm_is_running = True
    ip = 0
    sp = -1
    steck = [0] * len_
    op = buffer[ip]
    while ip < len(buffer):
        if op == push_i:
            sp += 1
            ip += 1
            steck[sp] = int(buffer[ip])  
        elif op == push_fl:
            sp += 1
            ip += 1
            steck[sp] = float(buffer[ip]) 
        elif op == push_str:
            sp += 1
            ip += 1
            steck[sp] = buffer[ip]
        elif op == push_obj:
            sp += 1
            ip += 1
            steck[sp] = buffer[ip]
        elif op==dft_:
            data=steck[sp]
            sp-=1
            direction=steck[sp]
            sp-=1
            out=dft(data,direction)
            print("out dft")
            for i in out:
               print(i, end=' ')
            print()  
        elif op==noarg:
            sp+=1
            steck[sp]=None
        elif op==rfft_:
            data=steck[sp]
            sp-=1
            out=np.fft.rfft(data)
            print("out np-fft-rfft",out) 
            loger.info(f'signal________"{data}\nout np-fft-fft{out}')            
        elif op==fft_:
            data=steck[sp]
            sp-=1
            print("signal________",data)
            out=np.fft.fft(data)
            print("out np-fft-fft",out) 
            loger.info(f'signal________"{data}\nout np-fft-fft{out}')
        elif op==fftfreq_:
            n=data.size
            x=np.fft.fftfreq(n)
            print("x fftreq",x)
            
        elif op==dft_slow:
            data=steck[sp]
            sp-=1
            print("signal________",data)
            out=DFT_slow(data)
            print("out DFT_slow",out) 
            loger.info(f'signal________"{data}\nout DFT_slow{out}')
            #x=range(len(data))
            y=np.abs(out)           
        elif op==plot_:
            label=steck[sp]
            sp-=1 
            plot("./graphic/gr.png",label,x,y,loger)
            
        ip += 1
        if ip > (len(buffer) - 1):
            return
        try:
            op = buffer[ip]
        except IndexError:
            raise RuntimeError('Maybe arg of bytecode skipped')


if __name__ == '__main__':
    loger,date=get_logger("debug","log.txt",__name__)
    signal = np.array([1, 2, 3, 4, 3, 2])
    signal1=np.array([1,1])
    p1 = (push_obj,signal,rfft_,push_obj,signal,fft_)
    p2=(push_obj,signal,dft_slow,plot_)
    p3=(push_obj,signal1,dft_slow,push_str,"sygnal1",plot_)
    p4=(push_obj,signal1,dft_slow,fftfreq_,push_str,"sygnal1req",plot_)
    vm(p4, loger, date)


        
        