# n= number of vertices
# gd= graph distance

import matplotlib.pyplot as plt
import pandas as pd

lists = []
n_list=[]

min=1
max=100

for n in range(min, max+1):
   # print(n)
   if n%2==0:
       gd= n**2/(4*n-4)
   else:
       gd= (n+1)/4
   
   lists.append(gd)
   n_list.append(n)

   # print("L =", gd)

# print(lists)


df = pd.DataFrame(n_list)
df[1]= lists
df.columns = ['number of vertices','mean graph distance']
print(df)

df.plot.scatter(x='number of vertices', y='mean graph distance')


from sklearn.linear_model import LinearRegression

mod = LinearRegression(fit_intercept = True)
lm = mod.fit(df[["number of vertices"]], df[["mean graph distance"]])
print(lm)
#print(mod.coef_)
#print(mod.intercept_)

slope =  mod.coef_[0,0]
print("slope = ",slope)

interception = mod.intercept_[0]

print("interception = ",interception)



