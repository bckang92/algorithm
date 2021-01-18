i = int(input())

result = 0

for n in range(i+1):
    for m in range(60):
        for k in range(60):
            if '3' in str(n)+str(m)+str(k):
                result += 1

print(result)