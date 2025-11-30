
import functions
import numpy as np 

v = functions.Vector([1,2,3,4,5])
#print(v)
v1 = v*10783646
#print(v1)
print(np.var(v))
var = functions.Var(v)
print(var)
    

#vec = np.array([1,2,3,4])
#print(vec)
#print(vec + 1)
#print("Hello World")
#prices = [10,12,13,15]


#log_returns = [-0.1,0.22,0.15,0.344,-0.2]
#avg_return = 0
#avg_return = (np.sum(log_returns))/len(log_returns)
#portfolio = [100,120,100,80,155]
#log_return = []
#for i in range(len(portfolio)-1):
    #log_return.append(np.log(portfolio[i+1]/portfolio[i]))
# cumulative log return
#print(str(100*np.sum(log_return))+ "%")
# total log return (in terms of simple returns e^cum_log_return)
#print(100*np.exp(np.sum(log_return)))