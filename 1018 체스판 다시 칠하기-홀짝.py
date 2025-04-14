N, M = map(int, input().split())

Chess_Board = []
result = []

for _ in range(N):
    Chess_Board.append(input())

for i in range(N-7):
    for j in range(M-7): #8x8 체스판 만들기 과정
        black = 0
        white = 0
# a = row, b = column [0],[0]부터 시작
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0: # 짝수이면 항상 처음 시작한 색이 위치
                    if Chess_Board[a][b] != 'B': # 시작이 B라 a+b 짝수 위치면 B여야 하는데 없으니까 바꿔야함.
                        black += 1
                        
                    if Chess_Board[a][b] != 'W':
                        white += 1
                        
                else: # a + b 가 홀수이면 처음과 반대 색이 위치 해야 함
                    if Chess_Board[a][b] != 'W':
                        black += 1
                        
                    if Chess_Board[a][b] != 'B':
                        white += 1
                        
    result.append(min(black, white))
    


print(min(result))       
