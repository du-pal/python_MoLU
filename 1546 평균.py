N = int(input())
scores = list(map(int, input().split()))
new_scores = []


M = max(scores)

for j in scores:
	new_score = float(j/M*100)
	new_scores.append(new_score)

new_avg = sum(new_scores)/N

print(new_avg)	
