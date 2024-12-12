from random import randint
import time

start = time.time()
a = [1,2,3,4,5,6,7,8,9]
target_num = randint(1, 9)
print('target number: ', target_num)

left_index = 0
right_index = len(a)-1
while left_index<=right_index:
    middle_index = (left_index+right_index)//2
    if target_num==a[middle_index]:
        print("index of the targeted number: ", middle_index)
        break
    elif target_num>a[middle_index]:
        left_index = middle_index+1
    else:
        right_index = middle_index-1

end = time.time()
print("time taken to search the target num: ", (end-start))