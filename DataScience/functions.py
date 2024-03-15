# 1. import pandas

import pandas as pd

# 2. make a parameters of table

jq = {
    'name': ["Joseph", "Joe", "Milly", "Kanm", "kiki", "Paul"], 
    'age': [23, 45, 20, 12, 56, 22],
    'color_hair': ["black", "black", "red", "yellow", "blue", "brown"],
    'id_number': [12345, 885545, 6632, 872, 442, 9963],
    'phone_number': [85464038, 8554721, 96321247, 9654423, 8745202, 96301470]
    }

# 3. define the dataFrame

jw = pd.DataFrame(data = jq)

#visualize data

print(jw)

#using Functions


## max()

Average_pulse_max = max(35, 85, 100, 200)

print(Average_pulse_max)

## min()

less_number = min(10, 55, 98, 100, 85, 33)

print(less_number)






