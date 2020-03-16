#THE GREEKS:

#THIS CODE WILL CALCULATE THE BLACK-SCHOLES GREEKS AND OPTIONS PRICE

#S0= Stock Price
#X= Strike Price
#r=Risk-free Rate
#Sigma=Volatility
#T=Time to expiration
#x=variable

import math
import numpy as np
from scipy.stats import norm

def D1(S0, X, r, Sigma, T):
  #a variable that is usedin all calculations
  d1=((np.log(S0/X)+(r+(Sigma**2)/2)*T)/(Sigma*(T**0.5)))
  return d1

def D2(S0, X, r, Sigma, T):
  #a variable that is usedin all calculations
  d2=((np.log(S0/X)+(r-(Sigma**2)/2)*T)/(Sigma*(T**0.5)))
  return d2

def Nline(x):
 #Derivative of normal cumulative distribution function
 NDer=(1/math.np.sqrt(2*np.pi()))*np.exp(-(x^2)/2)
 return NDer

def Delta(S0, X, r, Sigma, T,Type="Call"):
  #variation of option price per unit of variation of stock price
  d1=D1(S0, X, r, Sigma, T)
  if Type=="Call":
    myDelta=norm.cdf(d1)
  else:
    myDelta=norm.cdf(d1)-1
  return myDelta

def Gamma(S0, X, r, Sigma, T,Type="Call"):
   #variation of Delta per unit of variation of Stock Price
  d1=D1(S0, X, r, Sigma, T)
  NL=Nline(d1)
  
  myGamma=NL/(S0*Sigma*math.sqrt(T))  
  return myGamma

def Theta(S0, X, r, Sigma, T,Type="Call"):
  #variation of option price per unit of time variation
  d1=D1(S0, X, r, Sigma, T)
  d2=D2(S0, X, r, Sigma, T)
  NL=Nline(d1)
  
  myTheta=S0*NL*Sigma -r*X*np.exp(-r*T)*norm.cdf(d2)
  return myTheta

def BS(S0, X, r, Sigma, T,Type="Call"):
  #returns option price
  d1=D1(S0, X, r, Sigma, T)
  d2=D2(S0, X, r, Sigma, T)
  PV=X*np.exp(-r*(T))
  if Type=="Call":
    price=norm.cdf(d1)*S0-norm.cdf(d2)*PV
  else:
    price=PV*norm.cdf(-d2)-S0*norm.cdf(-d1)
  return price
