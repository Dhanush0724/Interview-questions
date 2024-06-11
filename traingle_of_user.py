n = 5

for i in range(1,n+1):
    current_sum = 0
    current_rows = []
    for j in range(1,i+1):
        current_rows.append(str(j))
        current_sum+=j
    rows_exp = '+'.join(current_rows)
    print(rows_exp+"=",current_sum)
