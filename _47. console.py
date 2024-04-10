word = input()
task = [a for a in input().replace("<delete>", '|-|').replace("<bspace>", '|--|').replace("<left>", '|<|').replace("<right>", '|>|').split('|') if a]

ans = ''
curr_pos = 0

for t in task:
    if t == '>':
        if curr_pos < len(ans):
            curr_pos += 1
    elif t == '<':
        if curr_pos > 0:
            curr_pos -= 1
    elif t == '-':
        if curr_pos < len(ans):
            ans = ans[:curr_pos] + ans[curr_pos + 1:]
    elif t == '--':
        if curr_pos > 0:
            ans = ans[:curr_pos - 1] + ans[curr_pos:]
            curr_pos -= 1
    else:
        ans = ans[:curr_pos] + t + ans[curr_pos:]
        curr_pos += len(t)

if word == ans:
    print("Yes")
else:
    print("No")


#print(console("hellochild", "helto<left><bspace>l<delete>ochilds<bspace>"))
#print(console("programming", "programming<left><left><right><delete>"))


