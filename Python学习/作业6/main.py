'''def year(numer):
    try:
        numer = int(numer)
    except ValueError:
        print('请输入数字')
    else:
        try:
            if numer/4==0 and numer/100!=0 or numer/100==0:
                print('此为闰年')
            else:
                print('这不是闰年')
        except ValueError:
            print('请输入整数')
    return numer
year((input('请输入年份<<<')))'''
'''def numer(*args):
    lis=[]
    for lis_1 in args:
        for lis_2 in lis_1:
            try:
                num=int(lis_2)
                lis.append(num)
            except ValueError:
                print('请输入数字')
    numer_max=max(lis)
    print(numer_max)
    return
numer_str=input('请输入(请用空格隔开)《《《')
numer(numer_str.split'''

