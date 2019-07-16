def V_tridiagonal(nr,t):
    V=np.zeros((nr,nr))
    for i in range(nr):
        r=dr*i
        a=dt*(-sigma**2/(2*dr**2)+(theta(t)-kappa*r)/(2*dr))
        b=1+dt*(sigma**2/dr**2+r)
        c=dt*(-sigma**2/(2*dr**2)-(theta(t)-kappa*r)/(2*dr))
        if i==0:
            V[i][i]=b
            V[i][i+1]=1-b
        elif i==nr-1:
            V[i][i-1]=a
            V[i][i]=1-a
        else:
            V[i][i-1]=a
            V[i][i]=b
            V[i][i+1]=c          

    return V
