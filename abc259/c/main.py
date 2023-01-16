s = input()
t = input()

s_lst = []
for char in s:
    if len(s_lst) and s_lst[-1][0] == char:
        s_lst[-1][1] += 1
    else:
        s_lst.append([char, 1])

t_lst = []
for char in t:
    if len(t_lst) and t_lst[-1][0] == char:
        t_lst[-1][1] += 1
    else:
        t_lst.append([char, 1])

is_same = True if len(s_lst) == len(t_lst) else False
for si, ti in zip(s_lst, t_lst):
    if any([si[0] != ti[0],
            si[1] > ti[1],
            ti[1] > 1 and si[1] == 1]):
        is_same = False
        break

print('Yes' if is_same else 'No')
