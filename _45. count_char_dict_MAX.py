s = input('Введите строку: ')

ans = ''
count_char = 0

for now in set(s):
    nowcnt = 0
    for j in range(len(s)):
        if now == s[j]:
            nowcnt += 1
    if nowcnt > count_char:
        ans = now
        count_char = nowcnt

print(ans, count_char)

