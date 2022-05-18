import numpy as np

tries=[]
number = np.random.randint(1, 101) # загадываем число
predict_number = np.random.randint(1, 101) # первая попытка угадать
tries.append(predict_number)
predict_number = np.random.randint(1, 101) # вторая попытка угадать
tries.append(predict_number)
count = 2
print(number)

lower=1
higher=101

while True:
    
    if tries[0]==number:
        count=1
        break
    elif tries[1]==number:
        count=2
        break
    
    for i in tries:
        if lower<i<number:
            lower=i
        elif higher>i>number:
            higher=i 
    
    predict_number = np.random.randint(lower, higher)
    tries.append(predict_number)
    
    count += 1
    
    if predict_number==number  or tries[0]==number or tries[1]==number:
        break
    
    lower=1
    higher=101
    
print(tries)
print(count)