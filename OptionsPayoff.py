# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:38:01 2020

@author: PC
"""

from BSG import BS
import math

def putpayoff(BuySell,premium,Strike,ClosePrice,Quantity,T,Sigma,r):
  premium=math.fabs(premium)
  T=float(T)/365 #convertendo T de dias para Anos
  if BuySell=='BUY':
    payoff=(BS(Strike, ClosePrice, r, Sigma, T,Type="Put")-premium)*Quantity  
    #if Strike >= ClosePrice:
      #payoff=((Strike-ClosePrice)-premium)*Quantity
    #else:
      #payoff=-premium*Quantity
  elif BuySell=='SELL':
    payoff=(premium-BS(Strike, ClosePrice, r, Sigma, T,Type="Put"))*Quantity  
    #if Strike >= ClosePrice:
      #payoff=((ClosePrice-Strike)+premium)*Quantity
    #else:
      #payoff=premium*Quantity
  return payoff

def callpayoff(BuySell,premium,Strike,ClosePrice,Quantity,T,Sigma,r):
  premium=math.fabs(premium)
  T=float(T)/365
  if BuySell=='BUY':
     payoff=(BS(Strike, ClosePrice, r, Sigma, T,"Call")-premium)*Quantity   
    #if ClosePrice >= Strike:
    #  payoff=((ClosePrice-Strike)-premium)*Quantity
    #else:
    #  payoff=-premium*Quantity
  elif BuySell=='SELL':
    payoff=(premium-BS(Strike, ClosePrice, r, Sigma, T,"Call"))*Quantity
    #if ClosePrice >= Strike:
    #  payoff=((Strike-ClosePrice)+premium)*Quantity
    #else:
    #  payoff=premium*Quantity
  return payoff

def Boipayoff(lowcallpremium,highcallpremium,lowcallStrike,highcallStrike,ClosePrice,Quantity,highlowratio=3,T=0,Sigma=0,r=0):
  #venda de uma opção e compra de maior quantidade de opção de strikesuperior - Compra de volatilidade
  lowcallpayoff=callpayoff('SELL',lowcallpremium,lowcallStrike,ClosePrice,Quantity,T,Sigma,r)
  highcallpayoff=callpayoff('BUY',highcallpremium,highcallStrike,ClosePrice,highlowratio*Quantity,T,Sigma,r)
  payoff=highcallpayoff+lowcallpayoff
  return payoff

def IronBoipayoff(lowcallpremium,highcallpremium,lowcallStrike,highcallStrike,ClosePrice,Quantity,highlowratio=3,T=0,Sigma=0,r=0):
  #venda de uma opção e compra de maior quantidade de opção de strikesuperior - Compra de volatilidade
  lowcallpayoff=putpayoff('SELL',lowcallpremium,lowcallStrike,ClosePrice,Quantity,T,Sigma,r)
  highcallpayoff=putpayoff('BUY',highcallpremium,highcallStrike,ClosePrice,highlowratio*Quantity,T,Sigma,r)
  payoff=highcallpayoff+lowcallpayoff
  return payoff

def TravaAltapayoff(CP,premiumStrikeBaixo, premiumStrikeAlto, StrikeBaixo, StrikeAlto, Quantity,ClosePrice,T,Sigma,r):
  if CP=='CALL':
    lowpayoff=callpayoff('BUY',premiumStrikeBaixo, StrikeBaixo,ClosePrice, Quantity,T,Sigma,r)
    highpayoff=callpayoff('SELL',premiumStrikeAlto, StrikeAlto,ClosePrice, Quantity,T,Sigma,r)
  elif CP=='PUT':
    lowpayoff=putpayoff('SELL',premiumStrikeAlto, StrikeAlto,ClosePrice, Quantity,T,Sigma,r)
    highpayoff=putpayoff('BUY',premiumStrikeBaixo, StrikeBaixo,ClosePrice, Quantity,T,Sigma,r)
  payoff=highpayoff+lowpayoff
  return payoff

def TravaBaixapayoff(CP,premiumStrikeBaixo, premiumStrikeAlto, StrikeBaixo, StrikeAlto, Quantity,ClosePrice,T,Sigma,r):
  if CP=='CALL':
    lowpayoff=callpayoff('SELL',premiumStrikeBaixo, StrikeBaixo,ClosePrice, Quantity,T,Sigma,r)
    highpayoff=callpayoff('BUY',premiumStrikeAlto, StrikeAlto,ClosePrice, Quantity,T,Sigma,r)
  elif CP=='PUT':
    lowpayoff=putpayoff('BUY',premiumStrikeAlto, StrikeAlto,ClosePrice, Quantity,T,Sigma,r)
    highpayoff=putpayoff('SELL',premiumStrikeBaixo, StrikeBaixo,ClosePrice, Quantity,T,Sigma,r)
  payoff=highpayoff+lowpayoff
  return payoff

def Vacapayoff(lowcallpremium,highcallpremium,lowcallStrike,highcallStrike,ClosePrice,Quantity,lockpremium,lockstrike,highlowratio=3,T=0,Sigma=0,r=0):
  # venda de volatilidade: compra de opção, venda de maior quantidade de strike superior, trava em strike mais alto ainda:
  lowcallpayoff=callpayoff('BUY',lowcallpremium,lowcallStrike,ClosePrice,Quantity,T,Sigma,r)
  highcallpayoff=callpayoff('SELL',highcallpremium,highcallStrike,ClosePrice,highlowratio*Quantity,T,Sigma,r)
  lockcallpayoff=callpayoff('BUY',lockpremium,lockstrike,ClosePrice,Quantity*(highlowratio-1),T,Sigma,r)
  payoff=highcallpayoff+lowcallpayoff+lockcallpayoff
  return payoff

def VacaRevertidapayoff(lowcallpremium,highcallpremium,lowcallStrike,highcallStrike,ClosePrice,Quantity,lockpremium,lockstrike,highlowratio=5,T=0,Sigma=0,r=0):
  # venda de volatilidade, mas ao contrário da vaca, volta a ganhar numa explosão de vol
  lowcallpayoff=callpayoff('BUY',lowcallpremium,lowcallStrike,ClosePrice,Quantity,T,Sigma,r)
  highcallpayoff=callpayoff('SELL',highcallpremium,highcallStrike,ClosePrice,highlowratio*Quantity,T,Sigma,r)
  lockcallpayoff=callpayoff('BUY',lockpremium,lockstrike,ClosePrice,highlowratio*Quantity,T,Sigma,r)
  payoff=highcallpayoff+lowcallpayoff+lockcallpayoff
  return payoff

def Condor(IRON,lowoptpremium,highoptpremium,lowlockpremium,highlockpremium,lowoptStrike,highoptStrike,lowlockstrike,highlockstrike,ClosePrice,Quantity,T,Sigma,r):
  #venda de volatilidade: se deseja que o preço permaneça em uma faixa
  if IRON==True:
    lowlockpayoff=putpayoff('BUY',lowlockpremium,lowlockstrike,ClosePrice,Quantity,T,Sigma,r)
    lowoptpayoff=putpayoff('SELL',lowoptpremium,lowoptStrike,ClosePrice,Quantity,T,Sigma,r)
    highoptpayoff=callpayoff('SELL',highoptpremium,highoptStrike,ClosePrice,Quantity,T,Sigma,r)
    highlockpayoff=callpayoff('BUY',highlockpremium,highlockstrike,ClosePrice,Quantity,T,Sigma,r)
  else:
    lowlockpayoff=callpayoff('BUY',lowlockpremium,lowlockstrike,ClosePrice,Quantity,T,Sigma,r)
    lowoptpayoff=callpayoff('SELL',lowoptpremium,lowoptStrike,ClosePrice,Quantity,T,Sigma,r)
    highoptpayoff=callpayoff('SELL',highoptpremium,highoptStrike,ClosePrice,Quantity,T,Sigma,r)
    highlockpayoff=callpayoff('BUY',highlockpremium,highlockstrike,ClosePrice,Quantity,T,Sigma,r)
  payoff=highlockpayoff+highoptpayoff+lowoptpayoff+lowlockpayoff
  return payoff