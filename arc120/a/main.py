n = int(input())
a = []
max_nums = []
max_num = 0
for i in list(map(int, input().split())):
    a.append(i)
    max_num = max(max_num, i)
    max_nums.append(max_num)

sum_num = 0
diff_num = 0
for idx, num in enumerate(a):
    sum_num += num
    print(sum_num + diff_num + max_nums[idx] * (idx + 1))
    diff_num += sum_num
