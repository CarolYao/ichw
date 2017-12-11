
# coding: utf-8

# In[ ]:


def exchange(currency_from,currency_to,amount_from): 
    '''return the amount of money in currenct_to based on currency_from,the given amount of money in currency_from
    and the real time exchange rate.'''
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=%s&to=%s&amt=%.2f'%(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')#transfer the result into string
    if "true" in jstr:
        start=jstr.find('"to" : ')+8
        end=start+1
        while ord(jstr[end])==46 or 48<=ord(jstr[end])<=57:
            end=end+1
        answer=jstr[start:end]
        return answer
    else:
        return "Wrong!"
        
def main():
    currency_from=input("")
    currency_to=input("")
    amount_from=float(input(""))
    amount=exchange(currency_from,currency_to,amount_from)
    if amount=="Wrong!":
        print("Wrong!")
    else:
        print(amount)#main body, get input and print out result
        
def test_get_from():
    '''testing function'''
    assert exchange("USD","EUR",2.5)=="2.0952375"
    
def testB():
    '''testing function'''
    assert exchange("USD","EUR",2.7)=="2.2628565"
    
def testC():
    '''testing function'''
    assert exchange("EUR","USD",2.5)=="2.9829553928851"
    
def testall():
    '''test a few specific cases.'''
    test_get_from()
    testB()
    testC()
    print("All tests passed.")
        
if "__name__"=="__main__":
    main()

