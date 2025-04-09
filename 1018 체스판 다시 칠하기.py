# N과 M은 8보다 크거나 같고 50보다 작거나 같은 자연수이어야 한다
# [0,0]이 B로 시작하거나 W로 시작
# B로 시작하면 바로 옆이 B이거나 2번째 옆이 W이면 1을 칠하는 횟수 + 1 
N, M = map(int, input().split())

Chess_Board = []
result = []

for _ in range(N):
    Chess_Board.append(input().upper()) # 백준에서는 .upper()를 굳이 사용하지 않아도 입력이 대문자로 보장이 된다.

for i in range(N-7):
    for j in range(M-7): #8x8 체스판 만들기 과정
        black = 0
        white = 0
        
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
                        
        result.append(black)
        result.append(white) # 모든 값을 쌓아 놓고 최소값을 구하면 됨

print(min(result))                        
