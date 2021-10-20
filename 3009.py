from collections import Counter

x = [0,0,0]
y = [0,0,0]

for i in range(3):
    x[i], y[i] = map(int, input().split())

counter_x = Counter(x).most_common()
counter_y = Counter(y).most_common()


data_x = list(x[0] for x in counter_x)
data_y = list(y[0] for y in counter_y)

print(data_x[-1], data_y[-1])


#for data in counter_x:
#    min_count = 99999999
#    if counter_x[data] < min_count:
#        min_count = counter_x[data]
#        min_data = data
#result_x = min_data
#
#for data in counter_y:
#    min_count = 99999999
#    if counter_y[data] < min_count:
#        min_count = counter_y[data]
#        min_data = data
#result_y = min_data

#print(result_x, result_y)


