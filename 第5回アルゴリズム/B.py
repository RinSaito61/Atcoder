'''文字列の上書き(同じ文字は１つまで)'''
n = 30
s = 'ryfoxchyvfmsewlwpoyvhdjkbvdjsa'
ans = ''
for st in s:
    if ans.count(st) > 0:
        ans = ans.replace(st,'')
    ans += st
print(ans)