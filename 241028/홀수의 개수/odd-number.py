number=int(input())
a=[]
for i in range(len(str(number))):
    a.append(int(number%10))
    number/=10
a.reverse()
#print(a)


max_num=0
min_num=10000
def check(a):
    global max_num
    global min_num
    result=check_hol(a)
    if len(a)<=2:
        max_num = max(max_num, result)
        min_num = min(min_num, result)
    else:
        str_n=len(a)
        for i in range(1,str_n-1):
            for j in range(i+1,str_n):
                part1=a[:i]
                part2=a[i:j]
                part3=a[j:]
                n_part1 = check_hol(part1)
                n_part2 = check_hol(part2)
                n_part3 = check_hol(part3)
                #print(n_part1,n_part2,n_part3)
                result = result + n_part1 + n_part2 + n_part3
                #print(result)
                new_num = sum(part1) + sum(part2) + sum(part3)
                check([int(digit) for digit in str(new_num)])
        max_num=max(max_num, result)
        min_num=max(min_num, result)
    return max_num, min_num
        

def check_hol(a):
    holsu=0
    for su in a:
        if su%2==1:
            holsu+=1
    return holsu

maximum, minimum=check(a)
# print(minimum, maximum)
# maximum+=check_hol(a)
# minimum+=check_hol(a)
# print(minimum, maximum)
print(min_num,max_num)