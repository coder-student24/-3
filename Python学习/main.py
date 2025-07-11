'''class temperature:
    def __init__(self):
        count=0
        while 1:
            try:
                self.temperature_any=input('请输入你要转换的模式 华氏度转摄氏度为1 摄氏度转华氏度为2 如果不是请写/ :').replace(' ','')
                if self.temperature_any=='1':
                    self.temperature_h=input('请输入华氏度:'.replace(' ',''))
                    self.tempuature_h=float(self.temperature_h)
                    self.tempuature_c=((self.tempuature_h-32)*9/5 if self.tempuature_h>32
                                       else print('华氏度需要小于32'))
                    print(f'为{self.tempuature_c}摄氏度')
                    break
                elif self.temperature_any=='2':
                    self.tempuature_c=input('请输入摄氏度：'.replace(' ' ,''))
                    self.temperature_c=float(self.tempuature_c)
                    self.tempuature_h=self.tempuature_c*9/5+32
                    print(f'为{self.tempuature_h}华氏度')
                    break
                elif self.temperature_any=='/':
                    print('好的哥')
                    break
                else:
                    print('请正确选择')
                    count+=1
                    if count==3:
                        print('sb是不是，别玩了')
                        break
            except ValueError:
                print('请输入数字')


a=temperature()'''

class bankaccount:
    def __init__(self,account_holder:str,balance:float=0):
        self.account_holder=account_holder
        self.balance=balance
    def despoit(self,amount:float):
        try:
            if amount < 0:
                print('余额应为正数哦')
            else:
                self.amount=amount
        except TypeError:
            print('请输入数字')
    def withdraw(self,amount:float):
        try:
            if amount>self.amount:
                print('余额不足')
            else:
                self.amount=self.amount-amount
        except AttributeError:
            pass
    def __str__(self):
        try:
            return f'账户名{self.account_holder},余额{self.amount}'
        except AttributeError:
            pass
acc=bankaccount('xubu',0)
acc.despoit(-9)
acc.withdraw(20)
try:
    print(acc)
except TypeError:
    pass


























