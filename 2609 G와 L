num_1, num_2 = map(int, input().split())

gcd =[] # 최대공약수
lcm = [] # 최소공배수

a = num_1
b = num_2 

while b:
    a, b = b, a % b 
gcd.append(a)

lcm_num = num_1 * num_2 // a

lcm.append(lcm_num)
    


for i in range(1):
    print(gcd[i])
    print(lcm[i])
    
# 최대공약수 -> 계속 나누다가 % == 0 이면 그 값이고
# 최소공배수 = 값1 * 값2 // 최대공약수
    
