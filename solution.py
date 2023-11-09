f = open("three_digit_numbers.txt")
solution =f.read()
cols = solution.split()
# print(cols)
num_list=[]
for col in cols:
    num = int(col)
    num_list.append(num)
# print(num_list)
start = min(num_list)
sorted_list = []
for count in range(start, max(num_list)):
   
    if count not in num_list:
        sorted_list.append(count)
with open("sorted_numbers.txt",'w') as file:
    file.write(str(sorted_list))
         