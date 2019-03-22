#THE GREEKS:

#THIS CODE WILL CALCULATE THE BLACK-SCHOLES GREEKS AND OPTIONS PRICE

#S0= Stock Price
#X= Strike Price
#r=Risk-free Rate
#Sigma=Volatility
#T=Time to expiration
#x=variable

import math
from scipy.stats import norm

def D1(S0, X, r, Sigma, T):
  #a variable that is usedin all calculations
  d1=math.log((S0/X)+(r+(Sigma^2)/2)*T/(Sigma*math.sqrt(T)))
  return d1

def D2(S0, X, r, Sigma, T):
  #a variable that is usedin all calculations
  d2=math.log((S0/X)+(r-(Sigma^2)/2)*T/(Sigma*sqrt(T)))
  return d2

def Nline(x)
 #Derivative of normal cumulative distribution function
 NDer=(1/math.sqrt(2*pi()))*exp(-(x^2)/2)
return NDer

def Delta(S0, X, r, Sigma, T,type="Call"):
  #variation of option price per unit of variation of stock price
  d1=D1(S0, X, r, Sigma, T)
  if type="Call":
    myDelta=norm.cdf(d1)
  else:
    myDelta=norm.cdf(d1)-1
  return myDelta

def Gamma(S0, X, r, Sigma, T,type="Call"):
   #variation of option price per unit of variation of delta
  d1=D1(S0, X, r, Sigma, T)
  NL=Nline(d1)
  
  myGamma=NL/(S0*Sigma*math.sqrt(T))  
  return myGamma

def Theta(S0, X, r, Sigma, T,type="Call"):
  #variation of option price per unit of time variation
  d1=D1(S0, X, r, Sigma, T)
  d2=D2(S0, X, r, Sigma, T)
  NL=Nline(d1)
  
  myTheta=S0*NL*Sigma -r*X*exp(-r*T)*norm.cdf(d2)
  return myTheta

def BS(S0, X, r, Sigma, T,type="Call")):
  #returns option price
  d1=D1(S0, X, r, Sigma, T)
  d2=D2(S0, X, r, Sigma, T)
  PV=X*exp(-r*(T))
  if type="Call":
    price=norm.cdf(d1)*S0-norm.cdf(d2)*PV
  else:
    price=PV-S0+norm.cdf(d1)*S0-norm.cdf(d2)*PV
  return price
