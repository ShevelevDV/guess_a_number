import numpy as np

low=1
mid=50
high=101
count=0
search_range=[low,mid,high]
number = np.random.randint(1, 101) # загадываем число

while True:
    
    count += 1
    predict_number = np.random.randint(low, high)
    
    if predict_number == number:
        break
    elif search_range[0]<predict_number<search_range[1]:
        high=search_range[1]
        mid=round((low+high)/2)
    elif search_range[1]<predict_number<search_range[2]:
        low=search_range[1]
        mid=round((low+high)/2)
    
    print(search_range)
    
    
print(count)