# Title: Plan for your portfolios

## Team Member(s):
Haoyuan Song,
Jiajun Chen,
Yuyao Wang.


# Monte Carlo Simulation Scenario & Purpose:
As robo-advisor, A Django based web system is designed to return a suitable stocks portfolio for people who are novice of finance. //what information needed
This system takes in multiple data including stocks data(provided by yahoo finance),stocks code, time period(start date
and end date),trading frequency and excepted volatility. According those data, this system will return a portfolio with specific weight of stocks and trading frequency.
A financial model is applied to this system,(PlEASE EXPLAIN)
// output what valuable results//how the system decide that.

### Hypothesis before running the simulation:
We use the following configuration for simulation:
Three particular stocks:(stock code)
start date:
end date:
trading frequency(days):

Hypothesis:
1. The larger the frequency, the wider the scope of the return.
2. Different excepted volatility results a particular weight ratio of portfolio, which is most suitable for investors.


### Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). 
For each such variable, how did you decide the range and which probability distribution to use?  
Do you think it's a good representation of reality?
various weight of portfolio: The total weight of the portfolio is 100%.The weight is split by th stocks randomly.
It is good representation as any proportion of specific stock in portfolio is possible.
Trading frequency: Trading frequency can be range (3,30).The frequency can only be integers. All the numbers from 3
to 30 are in same possibility.
## Instructions on how to use the program:
User is required to type in their excepted volatility. According this volatility, the system will calculate the portfolio
with most suitable weight and trading frequency.

## Sources Used:

