# Title: Plan for your portfolios


## Team Members:
- Haoyuan Song
- Jiajun Chen
- Yuyao Wang  
##### GitHub Link: https://github.com/CarolGo/Final-project.git


# Monte Carlo Simulation Scenario & Purpose:
It is difficult for someone who wants to invest his/her property reasonably without professional financial background.  
It is also unwise for them to take risks pursuing high profits regardless of high risks. Nowadays, robo-advisor helps people solve that problem. Based on this background, our systems will provide you your personal 
tailor investment method on stocks, which help you asset your allocations more precisely and make your investment decisions 
more rationally using Monte Carlo Simulation. Finally, You can get your specific stock portfolios trading frequency 
within the risks you can bear to maximum your income.


### Hypothesis before running the simulation:
Image that we have know the risk preference of users. Based on their preference, we take multiple data including stocks data(provided by yahoo finance),stocks code, time period(start date
and end date),trading frequency and excepted volatility into account. According those data, this system will return a portfolio with specific weight of stocks and trading frequency.
A financial model called utility function used by investor is applied to this system to help the system decide that.
- We use the following configuration for simulation:
1. Three particular stocks:(stock code)
1. start date:
1. end date:
1. trading frequency(days):

- Hypothesis:  

1. The larger the frequency, the wider the scope of the return.
1. Different excepted volatility results a particular weight ratio of portfolio, which is most suitable for investors.


### Simulation's variables of uncertainty
- various weight of portfolio:  

  The total weight of the portfolio is 100%.The weight is split by stocks randomly. It is good representation as any proportion of specific stock in portfolio is possible.
- Trading frequency:  

  Trading frequency can be range (3,30).The frequency can only be integers. All the numbers from 3 to 30 are in same possibility.


## Instructions on how to use the program:
User is required to type in their excepted volatility. According this volatility, the system will calculate the portfolio
with most suitable weight and trading frequency.


## Sources Used:
1. 
1. 
1. 

