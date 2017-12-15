# Personal Tailor Portfolio


## Team Members:
- Haoyuan Song
- Jiajun Chen
- Yuyao Wang  
#### GitHub Link: https://github.com/CarolGo/Final-project.git


# Monte Carlo Simulation Scenario & Purpose:
It is difficult for someone who wants to invest his/her property reasonably without professional financial background.  It is also unwise for them to take risks pursuing high profits regardless of high risks. Nowadays, robo-advisor helps people solve that problem. 
Based on this background, our systems choose a series kind of stocks as input and will provide some specific stock (for example, three stocks from all the stocks) as output using Monte Carlo Simulation. 
By choosing stocks well for you, we also provide you your personal tailor investment method on stocks you choose, which help you asset your allocations more precisely and make your investment decisions 
more rationally. 


### Hypothesis before running the simulation:
Image that all the stocks obey Normal Distribution. We randomly choose eight stocks data from Yahoo Finance including stocks data, tickers, time period (start date
and end date, for example we consider three months to choose specific stock and one year data from website to calculate weights) into account. 
According to those data, this program will return a portfolio with specific weight of stocks.
- We use the following configuration for simulation:
1. A given set of particular stocks.
1. historical prices from YAHOO FINANCE!
1. Investor's utility function and modern portfolio theory.


- Hypothesis:  

1. With Monte Carlo Simulation, we can get to know which kind of stocks we should choose from a large number 
of stock market.
1. After simulation, we will know the exact percentage of each stock we should allocate.


### Simulation's variables of uncertainty
- various weight of portfolio:  

  The total weight of the portfolio is 100%.The weight is split by stocks randomly. It is good representation as any proportion of specific stock in portfolio is possible.
- type of stock:  


  Image that we don't know how to choose stock from various stock market. Maybe we can choose randomly.
  However, depending on investor's utility function, we can calculate the maximum of utility with Monte Carlo Simulation and list the utility to get three stocks.


## Instructions on how to use the program:
- Using Terminal:
1. Clone the repository: git clone https://github.com/CarolGo/Final-project.git
1. Run command: python3 choose.py
1. Close Figure1: the weight will shown in the window.
- Using PyCharm:
1. Clone the repository: git clone https://github.com/CarolGo/Final-project.git
1. Open the file Final-project in PyCharm.
1. Run file: choose.py
1. Close Figure1: the weight will shown in the console.


## Conclusion:
From the eight stocks 'MSFT', 'GE', 'C', 'AMD', 'AAPL', 'F', 'T', 'NKE', 'CTL', we can choose three stocks: 'GE', 'MSFT', 'C'. If user 
invest on the three stocks, invest GE for 11.1982483995%, invest MSFT for 76.8910031075% and invest C for 11.9107484929% can satisfy their
expected returns with low risk. The point can be found on the graph.


## Sources Used:
1. Harry Markowitz. (1952, July). Portfolio Selection. The Journal of Finance. 1952.7:77-91.
1. Sharpe, W. F., Alexander, G. J., & Bailey, J. V. (1999). Investments (Vol. 6). Upper Saddle River, NJ: Prentice-Hall.

