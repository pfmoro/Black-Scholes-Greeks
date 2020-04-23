# Black-Scholes-Greeks

This repository contains python code that return the greeks (Delta, Gama and Theta), as well as the Black and Scholes price 
for a given options.

It requires numpy and norm(from scipy.stats) references. 

Inputs for the calculations are:

#S0= Stock Price
#X= Strike Price
#r=Risk-free Rate (In continuous capitalization, see below)
#Sigma=Volatility (must be estimated, see below)
#T=Time to expiration (In Years)

risk free rate is the base interest rate for the market in which you are evaluating the options, as examples, for US it would be the Fed Fund Effective Rate and for EU the ESTER Rate.Fed Fund rates can be obtained from Federals Reserve bank API (python reference: fredapi) by using 'FEDFUNDS' key.

Continuous capitalization is calculated by: S=P*Exp(rT), where S is future value and P is Presenv Value. Most Interest rates are published as simple interest form. in Python, simple interest can be converted to continous by apllying: np.log(1+rs) to the rs simple interest rate  

Volatility is the only variable that cannot be directly calculated or obtained from the markets but only estimated. There are several ways to estimate it, but the two most popular are:

1 - Calculate the standard deviation of past 30 market closure days. - this is called Historical Volatility

2 - Obtain current market prices of options and find the volatility that, when inserted in the Black-Scholes formula returns the current market price. - This is called Implicit Volatility.

It is important to mention that Black and Scholes is based on the assumption that market returns are normally distributed, which is not allways true (specially during high volatility times). A development of the formulas in this repo would be to use a Power law instead of normal distribution. However, the estimation of the parameteres of this distribution would require extensive ressearch.

The Repo Also include a package that calculates payoff of Option Strategies
