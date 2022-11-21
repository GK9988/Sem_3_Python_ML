import pandas as pd
import numpy as np

data1 = pd.DataFrame(np.random.rand(3, 5), np.arange(3))
# print(data1)
data1.columns = ["uid", "name", "nameofprogram", "phone_no", "city"]
# print(data1)
# data1.loc
data1.loc[:, ['uid']] = ['21BCS6590', '21BCS7878', '21BCS6578']
data1.loc[:, ['name']] = ['pushkar', 'rishab', 'aashish']
data1.loc[:, ['nameofprogram']] = ['aiml', 'aiml', 'aiml']
data1.loc[:, ['phone_no']] = [9076854557, 6765675677, 67676785599]
data1.loc[:, ['city']] = ['chandigarh', 'jhansi', 'phagwara']

data2 = pd.DataFrame({
    'uid': ['21bcs6786', '3261ghghj', '21bcs5556'],
    'name': ['aaryan', 'kartik', 'anshul'],
    'nameofprogram': ['devops', 'datascience', 'web developer'],
    'phone_no': [9065675678, 89787776880, 8866788965],
    'city': ['meerut', 'jhalandar', 'ghaziabad']
})
data1 = data1.append(data2, ignore_index=True)
data3 = pd.DataFrame(np.random.rand(3, 2), columns=[3, 4],)
print(data3)
data3 = data3.to_csv('data3.csv', index=False)
print(data1)
