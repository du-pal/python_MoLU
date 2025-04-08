from collections import deque

N = int(input())
card = deque([])


for i in range(N):
    card.append(i+1)
    
while len(card) > 1:
    card.popleft()
    top_card = card.popleft()
    card.append(top_card)
    
    
    
print(card[0])


-> 정답!




#%%
N = int(input())

card = []

for i in range(N):
    card.append(i+1)
    
    
    
while len(card) > 1:
    for j in card:
        
        del card[0]
        
        top_card = card[0]
        
        card.append(top_card)
        
        del card[0]
        
print(card[0])
 
#%%


N = int(input())

card = []

for i in range(N):
    card.append(i+1)
    
    
    
while len(card) > 1:
    for j in card:
        card.pop(0)
        top_card = card.pop(0)
        card.append(top_card)
        
print(card[0])
