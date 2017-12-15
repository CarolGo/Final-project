import port_fin
import pandas as pd


def choose(all_stock, basic_start, basic_end, risk_a, processor, basic_times, stock_num):
    '''
    Choose particular stocks set from a given stocks poll by randomly choosing sets, then calculating the utility and compare.
    :param all_stock: Default stocks set.
    :param basic_start: start date of training stocks set.
    :param basic_end: end date of training stocks set.
    :param risk_a: preference rick of user.(ranges from 1 - 14)
    :param processor: number of multi process.
    :param basic_times: simulation times.
    :param stock_num: number of stocks in one set.
    :return: list of selected stocks.
    '''
    val_set = []
    # get all testing data.
    port = port_fin.Portfolio(all_stock)
    port.set_basic(basic_start, basic_end, risk_a, processor)
    returns = port.get_data(port)
    # find all the portfolio which contains two stocks and append them into a list
    for i in range(len(all_stock)):
        last = all_stock.pop()
        if len(all_stock) == 0:
            break
        for j in range(len(all_stock)):
            # generate the portfolio
            temp = [last, all_stock[j]]
            temp_port = port_fin.Portfolio(temp)
            temp_port.set_basic(basic_start, basic_end, risk_a, processor)
            # get data from all the testing data
            temp_port.returns = pd.concat(
                [returns.iloc[:, i], returns.iloc[:, j]], join='outer', axis=1)
            max_val = temp_port.plo(temp_port, 0, basic_times)[1]
            # generate a list containing the portfolios and their max utility
            val_set.append([temp, max_val])
    # sort the list by their max utility
    list_i = sorted(val_set, key=lambda d: d[1])
    select_stock = []
    # union the top ranking portfolios until reach the number
    while len(select_stock) < stock_num:
        temp = list_i.pop()[0]
        select_stock = list(set(select_stock).union(set(temp)))
    return select_stock


if __name__ == '__main__':
    # setting the initial value
    all_stock = ['MSFT', 'GE', 'C', 'AMD', 'AAPL', 'F', 'T', 'NKE', 'CTL']
    basic_start = '2017-03-20'
    basic_end = '2017-05-20'
    risk_a = 5.5
    processor = 4
    basic_times = 150
    stock_num = 3
    # use choose to find selected stocks
    select_stock = choose(all_stock, basic_start, basic_end,
                          risk_a, processor, basic_times, stock_num)
    print("The choosen stocks are:", select_stock)
    # generate the final portfolio
    fin_port = port_fin.Portfolio(select_stock)
    fin_port.set_basic('2016-01-01', '2017-05-20', risk_a, processor)
    fin_port.get_data(fin_port)
    max_we = fin_port.plo(fin_port, 1, 4000)[0]
    fin_port.print(fin_port, max_we)
