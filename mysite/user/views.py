from django.shortcuts import render
from .models import user, user_invest, question, myindex, invest
from django.http import HttpResponse
from user import port_multi

def form(request):
    question_list = question.objects.filter(type=0)
    return render(request, 'user/form.html', {'question_list':question_list})

def plo(request):
    p = user.objects.get(user_name='1234')
    invest_list = invest.objects.filter()
    stock_set = []
    for i in invest_list:
        stock_set.append(i.no)
    port = port_multi.Portfolio(stock_set)
    print(invest_list)
    port.set_basic('2016-01-01', '2017-05-20', p.risk, 4)
    port.get_data(port)
    temp = port.plo(port)
    max_we = temp[0]
    max_re = temp[1]
    cash = (p.mobility_a + p.mobility_b + p.mobility_c + p.mobility_d)/100 * p.size
    p.balance = p.size - cash
    p.max_re = max_re
    p.save()
    print(cash)
    count =0
    temp_list = []
    for i in invest_list:
        invest_temp = user_invest.objects.get(invest=i)
        invest_temp.size = max_we[count] * p.size
        d = {'name': i.invest_name, 'size': invest_temp.size, 'we': max_we[count]*100}
        temp_list.append(d)
        print(invest_temp.size)
        invest_temp.save()
        count = count + 1
    return render(request, 'user/plo.html', {'p':p, 'temp':temp_list, 'max_re':max_re*100})

def buy(request):
    p = user.objects.get(user_name='1234')
    return render(request, 'user/buy.html', {'p':p})

def test(request):
    if request.method == 'POST':
        inputs = request.POST.getlist('arr')
        p = user.objects.get(user_name='1234')
        flag = inputs.pop()
        if flag == '1':
            score = 0
            for i in inputs:
                score = score + int(i)
            p.score = score
            print(score)
            p.save()
        elif flag == '2':
            p.mobility_a = int(inputs[0])
            p.mobility_b = int(inputs[1])
            p.mobility_c = int(inputs[2])
            p.mobility_d = int(inputs[3])
            p.save()
        else:
            per = int(inputs[4])/100
            index_a = myindex.objects.get(pk=1)
            if per <= 0.1:
                risk_o = (index_a.Rm - index_a.Rf) / (0.1 * index_a.risk_m2)
            else:
                risk_o = (index_a.Rm - index_a.Rf) / (per * index_a.risk_m2)
            p.risk_o = risk_o
            age = int(inputs[0])
            sex = int(inputs[5])
            fin = int(inputs[9])
            score_n = 32/89 * p.score + 4/89
            risk_a = 4.1715 - 0.0266 * score_n
            print(risk_a)
            risk_b = 7.6491 - 0.1795 * age + 0.0018 * age * age - 0.2851 * sex - 0.6642 * fin
            print(risk_b)
            p.risk = (risk_o + risk_a + risk_b)/3
            p.save()
        return HttpResponse('{"status":"success"}', content_type='application/json')
    else:
        return HttpResponse("<h1>test</h1>")