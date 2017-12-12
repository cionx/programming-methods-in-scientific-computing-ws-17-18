from scipy import *

def poisson_solver(f,g,m): 
    
    from scipy import ones, linspace, meshgrid
    from scipy import sparse
    from scipy.sparse import diags, identity, kron
    from scipy.sparse.linalg import spsolve
    
    n = m - 1
    h = 1/(n+1)
    
    # Construction of sparse Poisson-matrix
    v = 4 * ones(n)
    w = ones(n-1)
    Nb = diags(w, 1) + diags(w, -1)
    B = diags(v) - Nb
    I = identity(n)
    A = kron(I,B) + kron(Nb, -I)
    A = A.tocsr()
    
    # Construction of  grid                 
    lin =  linspace(0,1,n+2)
    X, Y = meshgrid(lin,lin) 
    
    u = zeros((n+2,n+2)) # initialze solution matrix with 0s
    
    # Insert boundaryu values
    for i in range(n+2): 
        u[i,0] = g(lin[i], lin[0])
        u[i,n+1] = g(lin[i], lin[n+1])
    for j in range(1,n+1): 
        u[0,j] = g(lin[0], lin[j])
        u[n+1,j] = g(lin[n+1], lin[j])
        
    F = zeros((n,n)) # solution matrix 0-initialized
    
    # insert function values f_ij
    for i in range(n):
        for j in range(n):
            F[i,j] = f(lin[i+1], lin[j+1])
            
    # modify boundary-adjacent values    
    F[:,0]    = F[:,0] + u[1 : n+1, 0] / h**2
    F[:,n-1]  = F[:,n-1] + u[1 : n+1, n+1] / h**2
    F[0, :]   = F[0, :] + u[0, 1 : n+1] / h**2
    F[n-1, :] = F[n-1, :] + u[n+1, 1 : n+1] / h**2
    
    # as column-vector
    F = F.flatten()
    
    # solve
    u_inner = spsolve(A,F*h*h) 
    
    # store values in solution-matrix
    u[1:n+1,1:n+1] = u_inner.reshape(n,n)
    
    # plot
    import matplotlib.pyplot as plot
    from matplotlib import cm
    fig = plot.figure()
    from mpl_toolkits.mplot3d import Axes3D
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, u, rstride=1, cstride=1, 
                       cmap=cm.jet,linewidth=0) 
    plot.show()
