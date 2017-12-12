from django.db import models
class user(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default='')
    nickname = models.CharField(max_length=200)
    score = models.IntegerField()
    risk = models.FloatField()
    mobility_a = models.FloatField()
    mobility_b = models.FloatField()
    mobility_c = models.FloatField()
    mobility_d = models.FloatField()
    risk_o = models.FloatField()
    size = models.FloatField()
    balance = models.FloatField()
    max_re = models.FloatField()
    def __str__(self):
        return self.user_name

class invest(models.Model):
    invest_name = models.CharField(max_length=200)
    no = models.CharField(max_length=200)
    risk = models.FloatField()
    benefit = models.FloatField()
    lost = models.FloatField()
    mobility = models.IntegerField()
    type = models.IntegerField()
    def __str__(self):
        return self.invest_name

class user_invest(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    size = models.FloatField()
    invest = models.ForeignKey(invest, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    # 暂时数据
    invest_type= models.IntegerField()

class myindex(models.Model):
    Rm = models.FloatField()
    Rf = models.FloatField()
    risk_m2 = models.FloatField()

class question(models.Model):
    question_text = models.CharField(max_length=200)
    type = models.IntegerField()
    # 0：证监会选择
    choice_a = models.CharField(max_length=200)
    num_a = models.IntegerField()
    choice_b = models.CharField(max_length=200)
    num_b = models.IntegerField()
    choice_c = models.CharField(max_length=200)
    num_c = models.IntegerField()
    choice_d = models.CharField(max_length=200)
    num_d = models.IntegerField()
    choice_e = models.CharField(max_length=200)
    num_e = models.IntegerField()
    def __str__(self):
        return self.question_text