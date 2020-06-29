#최대공약수
def gcd(a,b): 
    return b if (a==0) else gcd(b%a,a)

#list 최대 요소
maximum=0
for i,value in enumerate(priorities):
    if value>maximum:
        maximum=value
        index=i
print(index) 


#number 자릿수 합
def solution(n):
    answer = 0
    #number to string
    n_list = list(str(n))
    
    # list element => string to number
    strtotnum_list_ = list(map(int, n_list))
    
    # list sum
    sum_val = sum(strtotnum_list_)
    return sum_val
