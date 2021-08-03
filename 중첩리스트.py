#중첩리스트.py
#여러단 주석 ctrl+/
day1 = [10,8,3,1]
day2 = [5,2,3,1]
day3 = [15,8,2,3]

total_record = [day1, day2, day3]
# print(total_record)
# print(total_record[0])
# print(total_record[0][0])
# print(total_record[2][3])
# print(total_record[2][0])


for daily in total_record:
    for each in daily:
        print(each)

numbers = []
for n in range(10):
    numbers.append(n)
print(numbers)