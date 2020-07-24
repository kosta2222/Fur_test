import numpy as np
import math
n=2
m=1
nn_narams=NN_params()
X_and_or=[[0,1],[1,0],[1,1],[0,0]]
Y_and=[[0],[0],[1],[0]]
Y_or=[[1],[1],[1],[0]]
Y_xor=[[1],[1],[0],[0]]

matr=np.zeros((m,n))+0.5674321

def my_dot(data:list)->tuple:
    tmp_v=0
    dst=[None] * m
    dst_acted=[None] * m
    i=0
    k=0
    for row in range(m):
        arg=-2 * math.pi * i / n
        for elem in range(n):
          tmp_v+=matr[row][elem] * data[elem]
          #tmp_v*=math.cos(arg)
          tmp_v*=math.cos(arg)
          k+=1
        dst[row]=tmp_v 
        i+=1
    #for row in range(m):
        #dst_acted[row]=operations(SIGMOID,dst[row],0,0,0,"",nn_narams)
        
    return   dst

def get_mse(out_nn,teacher,n):
    sum_=0
    for row in range(n):
        sum_+=math.pow((out_nn[row]-teacher[row]),2)
    return sum_    
        
def evaluate(X_test, Y_test):
    scores = []
    out_nn=None
    res_acc = 0
    rows = len(X_test)
    wi_y_test = len(Y_test[0])
    elem_of_out_nn = 0
    elem_answer = 0
    is_vecs_are_equal = False
    for row in range(rows):
        x_test = X_test[row]
        y_test = Y_test[row]
        out_nn=my_dot(x_test)
        for elem in range(wi_y_test):
            elem_of_out_nn = out_nn[elem]
            elem_answer = y_test[elem]
            if (elem_of_out_nn > 0.5):
                elem_of_out_nn = 1
                # print("output vector elem -> ( %f ) " % 1, end=' ')
            else:
                elem_of_out_nn = 0
                # print("output vector elem -> ( %f ) " % 0, end=' ');
            # print("expected vector elem -> ( %f )" % elem_answer);
            if elem_of_out_nn == elem_answer:
                is_vecs_are_equal = True
            else:
                is_vecs_are_equal = False
                break
        if is_vecs_are_equal:
           # print("-Vecs are equal-")
           scores.append(1)
        else:
            # print("-Vecs are not equal-")
            scores.append(0)
    # print("in eval scores",scores)
    res_acc = sum(scores) / rows * 100
  
    return res_acc

def feed_learn(X, Y, eps, l_r_,with_adap_lr,ac_):
    global matr
    alpha=0.99
    beta=1.01
    gama=1.01
    error=0
    error_pr=0
    delta_error=0
    l_r=l_r_
    net_is_running=True
    it=0
    exit_flag=False
    dst_acted=None
    
    while net_is_running:
      print("ep:",it)  
      for retrive_ind in range(len(X)):
        x=X[retrive_ind]
        x=np.array(x)
        y=Y[retrive_ind]
        out_nn=my_dot(x)
        mse=get_mse(out_nn,y,m)
        print("mse",mse)
        #if mse<0.01:
            #exit_flag=True
            #break
        print("out nn",out_nn)    
        delta=(out_nn[0] - y[0])
        delta_np=np.array(delta)
        if with_adap_lr:
            error=get_mse(out_nn,y,m)
            delta_error=error - gama * error_pr
            if delta_error>0:
                l_r=alpha * l_r
            else:
                l_r=beta * l_r
            error_pr=error
        #print("type matr",type(matr)) 
        koef=matr * delta_np
        matr-=koef * l_r  
        print("lr",l_r)
      ac=evaluate(X,Y)
      print("acc", ac)
      if ac==float(ac_):
          exit_flag=True
          break 
      if it==eps:
          break
      
      it+=1
      if exit_flag:
          break
    
feed_learn(X_and_or,Y_and, 100, 0.001, True,100)    