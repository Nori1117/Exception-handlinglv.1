#Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors. 
#Handle the possible errors in the code written inside the function.
def find_smallest_number(num):
i=int(1)
    while(True):
        x=find_factors(i)
        if(len(x)==num):
            print(x)
            break
        else:
            i=i+int(1)
    return x[-1]
    
    def find_factors(num):
    factors = []
    for i in range(1,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors
    
    num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)

