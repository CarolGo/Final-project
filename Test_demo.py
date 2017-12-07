import tushare as ts # tushare, a free api to get chinese stock data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


class Portfolio():
    """
    Demo for presentation.
    """
    stock_set = ['600050','000725','600519']
    start_date = '2016-01-01'
    end_date = '2017-05-20'
    returns = False
    index_a = 5.5

    def __init__(self, stock_list=[]):
        """
        :param stock_list: stock id list, you can add or replace some of them.
        # stock_set = ['601212', '601212', '600050', '000725', '600519']
        """
        self.stock_set = stock_list

    def set_basic(self, start_date: str, end_date: str, index_a: float):
        """
        :param start_date: '2016-01-01'
        :param end_date: '2017-05-20'
        :param index_a: Risk Aversion Coefficient, different from users,range from 0~14,you can change it and test.
        :return: a matrix contain daily earnings of the stocks
        """
        self.start_date = start_date
        self.end_date = end_date
        self.index_a = index_a

    @staticmethod
    def get_data(self):
        returns = False
        for i in self.stock_set:
            arr = ts.get_k_data(i, start=self.start_date, end=self.end_date)  # tushare, a free api to get chinese stock data
            arr.set_index('date', inplace=True)
            re = np.log(arr['close'] / arr['close'].shift(1))  # get daily earnings
            if returns is False:
                returns = re
            else:
                returns = pd.concat([returns, re], join='outer', axis=1)
        return returns

    @staticmethod
    def plo(self, returns):
        """
        :param self:
        :param returns: a matrix contain daily earnings of the stocks
        :return:Best weights
        """
        port_returns = []
        port_variance = []
        max_val = -1
        for x in range(8000):
            # random many times to get to find numerical solution
            weights = np.random.random(len(self.stock_set))
            weights /= np.sum(weights)  # random weight
            temp_re = np.sum(returns.mean() * 252 * weights)
            temp_va = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))  # Converted to annual revenue
            val = temp_re - self.index_a * temp_va * temp_va  # Investor utility
            if val > max_val:
                max_val = val
                max_we = weights
                max_re = temp_re
                max_va = temp_va
            port_returns.append(temp_re)
            port_variance.append(temp_va)
        port_returns = np.array(port_returns)
        port_variance = np.array(port_variance)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.scatter(port_variance, port_returns, c=port_returns - self.index_a * port_variance * port_variance, marker='o')
        # plt.scatter(port_variance, port_returns, marker='o')
        plt.grid(True)
        plt.plot(max_va, max_re, 'r*', markersize=10.0)
        plt.xlabel('variance')  # variance
        plt.ylabel('returns')  # returns
        plt.colorbar(label='Investor utility')  # Investor utility
        plt.show()
        return max_we

    @staticmethod
    def print(self, max_we):
        """
        print results
        :param self:
        :param max_we: Best weights
        :return:
        """
        for i in range(len(max_we)):
            print(self.stock_set[i] + ":  "+ str(max_we[i] * 100) + "%")

    def compute(self):
        """
        Do the computing
        :return:
        """
        returns = self.get_data(self)
        max_we = self.plo(self, returns)
        self.print(self, max_we)

if __name__ == '__main__':
    port = Portfolio(['600050','000725','600519'])
    port.set_basic('2016-01-01', '2017-05-20', 5.5)
    port.compute()
