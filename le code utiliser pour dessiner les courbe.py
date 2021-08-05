from math import *
from numpy import *
from scipy.integrate import *
from matplotlib.pyplot import *
from pandas import *

Pco =float(input(" entrer le taux d etre en contacte avec les gens en plan d affectation"))
     # le taux d etre en contacte avec les gens en plan d affectation
def pr(Y, t):
    s, nba, R,D = Y[0], Y[1], Y[2],Y[3]
    Ptr = 0.589189  # le taux de transfert de maladie en cas de cotacte
    N = nba + s + R  # le nombre tatale des gens
    r =0.5674  # le taux de retblisement
    d = 0.02201  # la probabilite de mourir
    a=float(r)+float(d)
    return (-Pco *  Ptr * (nba / N) * s, Pco *  Ptr * (nba / N) * s - nba *(a), nba *r,nba*d)


temps = np.linspace(-5, 175, 90000)
sol = odeint(pr, [36205726, 1, 0,0], temps)
nba = list()
for k in sol:
    nba.append(k[1])
figure(figsize=(5,5))


plot(temps, nba, 'r', label='les gens qui ont malade ')
xlabel('par jour de puis la premiere jour d affectation',fontsize=13)
ylabel('nombre des cas',fontsize=13)
title('modelisation')
axis([-5,175,0,120000])
legend()

show()