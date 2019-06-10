import pandas as pd
from scipy.interpolate import interp1d
from math import exp
from scipy.optimize import minimize

def Nelson_Siegel(t,b0,b1,b2,t1,t2):
    '''
    t: maturity
    b0: beta0
    b1: beta1
    b2: beta2
    t1: tau1
    t2: tau2
    return: predicted value of yield
    '''

    factor1=(1-exp(-t/t1))/(t/t1)
    factor2=(1-exp(-t/t2))/(t/t2)-exp(-t/t2)
    return (b0+b1*factor1+b2*factor2)

def error_NS(params):
    b0,b1,b2,t1,t2=params
    T=list(data["Maturity"])
    Y=list(data["spot"]/100)
    errorsq=0
    for i,t in enumerate(T):
        y=Y[i]
        errorsq+=(exp(-y*t)-exp(-Nelson_Siegel(t,b0,b1,b2,t1,t2)*t))**2
    return errorsq



def Svensson(t,b0,b1,b2,b3,t1,t2):
    '''
    t: maturity
    b0: beta0
    b1: beta1
    b2: beta2
    b3: beta3
    t1: tau1
    t2: tau2
    return: predicted value of yield
    '''
    factor1=(1-exp(-t/t1))/(t/t1)
    factor2=(1-exp(-t/t1))/(t/t1)-exp(-t/t1)
    factor3=(1-exp(-t/t2))/(t/t2)-exp(-t/t2)
    return b0+b1*factor1+b2*factor2+b3*factor3

def error_SV(params):
    b0,b1,b2,b3,t1,t2=params
    T=list(data["Maturity"])
    Y=list(data["spot"]/100)
    errorsq=0
    for i,t in enumerate(T):
        y=Y[i]
        errorsq+=(exp(-y*t)-exp(-Svensson(t,b0,b1,b2,b3,t1,t2)*t))**2
    return errorsq
