# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000
#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
#Code starts here
data = pd.read_csv(path)
data_sample = data.sample(n=sample_size,random_state=0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()
margin_of_error = (z_critical*sample_std)/(math.sqrt(2000))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
true_mean = data['installment'].mean()
print('sample mean is ', sample_mean)
print('confidence interval are ', confidence_interval)
print('true mean is ',true_mean)



# --------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Different sample sizes to take
sample_size=np.array([20,50,100])
m = []
#Code starts here
fig,axes = plt.subplots(3,1)
for i in range (len(sample_size)):
    for j in range(1000):
        m = data['installment'].sample(n=sample_size[i]).mean()
    mean_series = pd.Series(m)
axes[i].plot(mean_series)





# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest
import pandas as pd
#Code starts here
data = pd.read_csv(path)
data['int.rate']=pd.to_numeric(data['int.rate'].map(lambda x:x.rstrip('%')))
data['int.rate'] = data['int.rate']/100
z_statistic , p_value = ztest( data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative = 'larger')
print('z_statistic is ',z_statistic)
print('p_value is ',p_value)
if p_value < 0.05:
    inference = 'Reject'
    print(inference)
else:
    inference = 'Accept'
    print(inference)


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic , p_value = ztest(data[data['paid.back.loan']=='No']['installment'],data[data['paid.back.loan']=='Yes']['installment'])
print('z_statistic is ',z_statistic)
print('p_value is ',p_value)
if p_value < 0.05:
    inference = 'Reject'
    print(inference)
else:
    inference = 'Accept'
    print(inference)


# --------------
#Importing header files
from scipy.stats import chi2_contingency
import pandas as pd
#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1
data = pd.read_csv(path)
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
x1=data[data['paid.back.loan']=='No']['installment']
x2=data[data['paid.back.loan']=='Yes']['installment']
z_statistic,p_value=ztest(x1,x2)

yes=data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no=data[data['paid.back.loan']=='No']['purpose'].value_counts()

observed=pd.concat([yes.transpose(),no.transpose()],axis=1,keys=['Yes','No'])

chi2, p, dof, ex=chi2_contingency(observed)
if chi2 <critical_value:
    print("Reject the null hypothesis that the two distributions are the same")
else:
    print("Fail to reject the null hypothesis that the two distributions are the same")



