import numpy as np

def guess_number(low,high):
    mid=round((low+high)/2)
    search_range=[low,mid,high]
    print(search_range)
    number = np.random.randint(low, high) # загадываем число 

    while True:
        
        predict_number = np.random.randint(search_range[0], search_range[2])
        mid=predict_number
        count += 1

        if predict_number == number:
            break
        elif search_range[0]<number<search_range[1]:
            high=search_range[1]
            mid=round((low+high)/2)
        elif search_range[1]<number<search_range[2]:
            low=search_range[1]
            mid=round((low+high)/2)

        search_range=[low,mid,high]
     
    return(count)