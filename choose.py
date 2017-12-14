import port_fin
import pandas as pd


def choose(all_stock, basic_start, basic_end, risk_a, processor, basic_times, stock_num):
    '''

    :param all_stock: 备选库
    :param basic_start: 测试开始时间
    :param basic_end:
    :param risk_a:
    :param processor:
    :param basic_times: 测试模拟次数
    :param stock_num:挑选个数
    :return:
    '''
    val_set = []
    port = port_fin.Portfolio(all_stock)
    port.set_basic(basic_start, basic_end, risk_a, processor)
    returns = port.get_data(port)
    for i in range(len(all_stock)):
        last = all_stock.pop()
        if len(all_stock) == 0:
            break
        for j in range(len(all_stock)):
            temp = [last, all_stock[j]]
            temp_port = port_fin.Portfolio(temp)
            print(temp)
            temp_port.set_basic(basic_start, basic_end, risk_a, processor)
            temp_port.returns = pd.concat([returns.iloc[:, i], returns.iloc[:, j]], join='outer', axis=1)
            max_val = temp_port.plo(temp_port, 0, basic_times)[1]
            val_set.append([temp, max_val])
    list_i = sorted(val_set, key=lambda d: d[1])
    select_stock = []
    while len(select_stock) < stock_num:
        temp = list_i.pop()[0]
        select_stock = list(set(select_stock).union(set(temp)))
    return select_stock


if __name__ == '__main__':
    all_stock = ['MSFT', 'GE', 'C', 'AMD', 'AAPL', 'F', 'T', 'NKE', 'CTL']
    basic_start = '2017-03-20'
    basic_end = '2017-05-20'
    risk_a = 5.5
    processor = 4
    basic_times = 100
    stock_num = 3
    select_stock = choose(all_stock, basic_start, basic_end, risk_a, processor, basic_times,stock_num)
    fin_port = port_fin.Portfolio(select_stock)
    fin_port.set_basic('2016-01-01', '2017-05-20', risk_a, processor)
    fin_port.get_data(fin_port)
    max_we = fin_port.plo(fin_port, 1, 4000)[0]
    fin_port.print(fin_port,max_we)

