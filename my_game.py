import numpy as np

def guess_number(low,high):
    mid=round((low+high)/2)
    count=0
    search_range=[low,high]
    number = np.random.randint(low, high)

    while True:
        
        predict_number = np.random.randint(search_range[0], search_range[1])
        count += 1

        if predict_number == number:
            break
        elif predict_number<number:
            low=predict_number
        elif predict_number>number:
            high=predict_number

        search_range=[low,high]
     
    return(count)

def efficiency_function(low, high, runs):
    tries=[]
    for i in range(runs):
        tries.append(guess_number(low,high)) 
    return round(sum(tries)/len(tries))

print(efficiency_function(1,100,10000))