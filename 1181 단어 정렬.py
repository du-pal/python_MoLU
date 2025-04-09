N = int(input())

words = []

for i in range(N):
    words.append(input().strip())
    
words = set(words)


words = list(sorted(words, key=lambda x: (len(x), x))) 
#길이가 짧은 것 부터, 길이가 같으면 사전적 의미 먼저! 
# key = lambsa x: (정렬 기준1, 정렬 기준2)
# https://daeun-computer-uneasy.tistory.com/74

for word in words:
    print(word)
_____________________________________________________________________

N = int(input())

words = []

for i in range(N):
    words.append(input().strip())
    
words = list(set(words))


for i in range(len(words)):
    for j in range(i+1, len(words)):
		    #버블 정렬
        if len(words[i]) > len(words[j]) or (len(words[i]) == len(words[j]) and words[i] > words[j]):
            words[i], words[j] = words[j], words[i]

for word in words:
    print(word)
