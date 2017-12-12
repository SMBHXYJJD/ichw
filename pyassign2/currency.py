"""currency.py: 计算汇率.

__author__ = "Weixuyan"
__pkuid__  = "1700011733"
__email__  = "weixuyan@pku.edu.cn"
"""

from urllib.request import urlopen

#第一部分：打开网页，得到字符串

def urlright(currency_from, currency_to,amount_from):
    '''得到url,测试url是否符合格式
    '''
    a= 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from= source &to= target &amt= amount '
    b = a.split(' ')
    b[1] = currency_from
    b[3] = currency_to
    b[5] = str(amount_from)
    c = ''.join(b)       
    return c   

a1= urlright('USD','EUR',2.5)


def test_urlright():
    '''测试url是否正确
    '''
    assert(urlright('USD','EUR',2.5) == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')


def B(c):
    '''得到网页显示的字符串
    '''
    doc = urlopen(c)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr    

a2=B(a1)


def test_B():
    '''测试字符串是否正确
    '''
    assert(B(a1)=='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }')


#第二部分：解析字符串，得到结果

def C(jstr):
    '''得到一个列表，其中第4项和第6项包含有效信息。
    '''
    jstr = jstr.replace('{','')
    jstr = jstr.replace('}','')
    jstr = jstr.replace(':',',')
    j = jstr.split(',')
    k=len(j)
    for i in range(0, k):
        j[i] = j[i].replace('"','')
        j[i] = j[i].strip()
    return j     

a3 = C(a2)


def test_C():
    '''测试列表是否符合预期
    '''
    assert(C(a2) == ['from', '2.5 United States Dollars', 'to', '2.0952375 Euros', 'success', 'true', 'error', ''])


def D(j):
    '''判断结果是否有意义，即第6项为‘true’，如有，输出结果，如没有，报错。
    '''
    if j[5] == 'false':
        return 'ERROR!'
    elif j[5] == 'true':
        list1 = j[3].split(' ')
        return  list1[0]   


def test_D():
    '''测试结果是否正确
    '''
    assert(D(a3) == '2.0952375')


#第三部分：测试所有函数：
    
def testAll():
    """test all cases"""
    test_urlright()
    test_B()
    test_C()
    test_D()
    print("All tests passed")   

testAll()

#主程序:

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    c = urlright(currency_from, currency_to,amount_from)
    jstr = B(c)
    j = C(jstr)
    result = D(j)

    print(D(j))

#输入部分：
   
currency_from = str(input())
currency_to = str(input())
amount_from = float(input())

#输出部分：

exchange(currency_from, currency_to, amount_from)
