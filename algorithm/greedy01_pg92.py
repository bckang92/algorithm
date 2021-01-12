#greedy 알고리즘 큰 수의 법칙 문제
n, m, k = map(int, input().split()) #n, m, k 입력

data = list(map(int, input().split())) #배열 값 입력

data.sort();

first = data[n-1]
second = data[n-2]

#최대 k 번 더해지고
#총 연산은 m 번
#결과값은 최대 더해진 것

mul = m // (k+1)
rest = m % (k+1)

result = (mul * (first * k + second)) + (rest * first)

print(result)
