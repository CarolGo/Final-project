import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import pandas_datareader.data as web # API to get stocks data from yahoo.
from dateutil.relativedelta import relativedelta
from multiprocessing import Pool
from pandas_datareader._utils import RemoteDataError
import concurrent.futures


class Portfolio():
    """
    This class realizes the main function of our program.
    Thi class uses the Monte Carlo Simulation to find the best weights of portfolio.
    """
    stock_set = ['IBM','AAPL','GOOGL']
    end_date = datetime.datetime.today().replace(hour=0, minute=0,second=0,microsecond=0)
    start_date = end_date - relativedelta(years=2)
    returns = False
    index_a = 5.5
    processes = 4

    def __init__(self, stock_list=[]):
        """
        :param stock_list: stock id list, you can add or replace some of them.
        """
        self.stock_set = stock_list

    def set_basic(self, start_date: str, end_date: str, index_a: float, processes:int):
        """
        :param start_date: The start date of stock data.(Format: '2016-01-01')
        :param end_date: The end date of stock data.(Format:'2017-05-20')
        :param index_a: Risk Aversion Coefficient, different from users,range from 0~14,you can change it and test.
        :param processes: Amount of processes.
        :return: a matrix contain daily earnings of the stocks
        """
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').replace(hour=0, minute=0,second=0,microsecond=0)
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').replace(hour=0, minute=0,second=0,microsecond=0)
        self.index_a = index_a
        self.processes = processes

    @staticmethod
    def request(arr:list):
        """
        get a stock's data from yahoo.
        :param arr: Array that stores the information of stocks we acquire..
        :return: return the daily earnings of stocks.
        """

        re = None
        num = 0
        while re == None:
            try:
                arr = web.DataReader(arr[2], 'yahoo', start=arr[0], end=arr[1])
            except RemoteDataError:
                # It automatically
                print('Data request failed, trying again..')
                time.sleep(3)
                num += 1
                if num == 5:
                    print('The request failed for 5 times, Please check your input.')
                    break
            else:
                re = np.log(arr['Close'] / arr['Close'].shift(1))  # get daily earnings
                return re


    @staticmethod
    def get_data(self):
        self.returns = False
        returns = False
        temp = []
        for i in self.stock_set:
            temp.append([self.start_date,self.end_date, i])
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.processes) as executor:
            re_ar = executor.map(self.request,temp)
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
    def plo(self, tag:int, times:int):
        '''

        :param self:
        :param tag: draw or not
        :param times:
        :return:
        '''
        port_returns = []
        port_variance = []
        max_val = -100
        temp = []
        for i in range(times):
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
        if tag ==1 :
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False
            plt.scatter(port_variance, port_returns, c=port_returns - self.index_a * np.array(port_variance) * np.array(port_variance), marker='o')
            plt.grid(True)
            plt.plot(max_va, max_re, 'r*', markersize=10.0)
            plt.xlabel('variance')  # variance
            plt.ylabel('returns')  # returns
            plt.colorbar(label='Investor utility')  # Investor utility
            plt.show()

        return max_we, max_val

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
        max_we = self.plo(self,0, 3000)[0]
        self.print(self, max_we)

if __name__ == '__main__':
    port = Portfolio(['IBM','AAPL','GOOGL'])
    port.set_basic('2016-01-01', '2017-05-20', 5.5, 4)
    port.get_data(port)
    max_we = port.plo(port,1, 3000)[0]
    port.print(port,max_we)
