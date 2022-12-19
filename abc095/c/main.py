a_pay, b_pay, c_pay, a_num, b_num = map(int, input().split())

if a_num > b_num:
    a_num, b_num = b_num, a_num
    a_pay, b_pay = b_pay, a_pay

ans = 0
if (a_pay + b_pay) / 2 < c_pay:
    ans = a_pay * a_num + b_pay * a_num
else:
    ans = c_pay * a_num * 2

if b_pay < (c_pay * 2):
    ans += b_pay * (b_num - a_num)
else:
    ans += c_pay * 2 * (b_num - a_num)

print(ans)
