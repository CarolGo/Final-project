import django
django.setup()
import tushare as ts # tushare, a free api to get chinese stock data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
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
    processes = 4

    def __init__(self, stock_list=[]):
        import django
        django.setup()
        """
        :param stock_list: stock id list, you can add or replace some of them.
        # stock_set = ['601212', '601212', '600050', '000725', '600519']
        """
        self.stock_set = stock_list

    def set_basic(self, start_date: str, end_date: str, index_a: float, processes:int):
        """
        :param start_date: '2016-01-01'
        :param end_date: '2017-05-20'
        :param index_a: Risk Aversion Coefficient, different from users,range from 0~14,you can change it and test.
        :return: a matrix contain daily earnings of the stocks
        """
        self.start_date = start_date
        self.end_date = end_date
        self.index_a = index_a
        self.processes = processes

    @staticmethod
    def request(arr:list):
        """
        get a stock's data
        :param arr:
        :return:
        """
        arr = ts.get_k_data(arr[1], start=arr[0].start_date,
                            end=arr[0].end_date)  # tushare, a free api to get chinese stock data
        arr.set_index('date', inplace=True)
        re = np.log(arr['close'] / arr['close'].shift(1))  # get daily earnings
        return re

    @staticmethod
    def get_data(self):
        self.returns = False
        returns = False
        temp = []
        for i in self.stock_set:
            temp.append([self, i])
        with Pool(processes=self.processes) as pool:
            re_ar = pool.map(self.request, temp)
        for i in re_ar:
            if returns is False:
                returns = i
            else:
                returns = pd.concat([returns, i], join='outer', axis=1)
        self.returns = returns

    @staticmethod
    def point(self):
        """
        get a random set of weights
        :param self:
        :return:
        """
        weights = np.random.random(len(self.stock_set))
        weights /= np.sum(weights)  # random weight
        temp_re = np.sum(self.returns.mean() * 252 * weights)
        temp_va = np.sqrt(np.dot(weights.T, np.dot(self.returns.cov() * 252, weights)))  # Converted to annual revenue
        val = temp_re - self.index_a * temp_va * temp_va  # Investor utility
        return val, weights, temp_re, temp_va

    @staticmethod
    def plo(self):
        """
        :param self:
        :return:Best weights
        """
        port_returns = []
        port_variance = []
        max_val = -1
        temp = []
        for i in range(8000):
            temp.append(self)
        with Pool(processes=self.processes) as pool:
            re_ar = pool.map(self.point, temp)
        for i in re_ar:
            if i[0] > max_val:
                max_val = i[0]
                max_we = i[1]
                max_re = i[2]
                max_va = i[3]
            port_returns.append(i[2])
            port_variance.append(i[3])
        if os.path.exists('user/static/assets/images/plo1.png'):
            os.remove('user/static/assets/images/plo1.png')
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        pic = plt.figure(figsize=(8, 4))
        plt.scatter(port_variance, port_returns, c=port_returns - self.index_a * np.array(port_variance) * np.array(port_variance), marker='o')
        plt.grid(True)
        plt.plot(max_va, max_re, 'r*', markersize=10.0)
        plt.xlabel('variance')  # variance
        plt.ylabel('returns')  # returns
        plt.colorbar(label='Investor utility')  # Investor utility
        pic.savefig('user/static/assets/images/plo1.png')
        plt.close(pic)
        plt.close()
        return max_we,max_re

    @staticmethod
    def print(self, max_we:list):
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
        self.get_data(self)
        max_we = self.plo(self)[0]
        self.print(self, max_we)

if __name__ == '__main__':
    port = Portfolio(['600050','000725','600519'])
    port.set_basic('2016-01-01', '2017-05-20', 5.5, 4)
    port.compute()
