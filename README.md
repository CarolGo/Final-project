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
and end date)and trading frequency into account. According those data, this system will return a portfolio with specific weight of stocks and trading frequency.
Financial models called investor's utility function and modern portfolio theory are applied to this system to help the system decide that.
- We use the following configuration for simulation:
1. A given set of particular stocks:(stock code)
1. historical prices form YHOO stock
1. trading frequency(days):

- Hypothesis:  

1. We use the investor’s utility function to evaluate the portfolios. The formula is from WF. sharp(1999)
1. When there are two portfolios with same expected profits, investors will choose the portfolio with less excepted risk.
1. The formula used in calculating excepted risk is from modern portfolio theory(Markowitz, 1952)


### Simulation's variables of uncertainty
- various weight of portfolio:  

  The total weight of the portfolio is 100%.The weight is split by stocks randomly. It is good representation as any proportion of specific stock in portfolio is possible.
- Trading frequency:  

  Trading frequency can be range (3,30).The frequency can only be integers. All the numbers from 3 to 30 are in same possibility.


## Instructions on how to use the program:
User is required to fill in a questionnaire to evaluate his(her) risk preference. According this, the system will calculate
the history price data and provide the most suitable weight and trading frequency.


## Sources Used:
1. Markowitz. Portfolio Selection, The journal of finance[J], 1952, 1540-6261
1. Sharpe, W. F., Alexander, G. J., & Bailey, J. V. (1999). Investments (Vol. 6). Upper Saddle River, NJ: Prentice-Hall.

