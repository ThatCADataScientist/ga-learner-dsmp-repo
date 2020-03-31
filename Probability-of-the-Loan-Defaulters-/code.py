# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = (df['fico'][df['fico']>700].count())/df['customer.id'].count()
p_b = (df['purpose'][df['purpose']=='debt_consolidation'].count())/df['customer.id'].count()
df1 = df[df['purpose'] == 'debt_consolidation']
p_a_b=len(df1[df1['fico']>=700])/len(df1)
result = p_a_b==p_a
print(result)



# --------------
# code starts here
prob_lp=df['paid.back.loan'][df['paid.back.loan']=='Yes'].count()/df['paid.back.loan'].count()
prob_cs=df['credit.policy'][df['credit.policy']=='Yes'].count()/df['credit.policy'].count()


new_df = df[df['paid.back.loan']=='Yes']
prob_pd_cs=len(new_df[new_df['credit.policy']=="Yes"])/len(new_df)
bayes = prob_pd_cs*prob_lp/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a=df['purpose'].value_counts()
a.plot.bar()
plt.show()
df1=df[df['paid.back.loan']=='No']
b = df1['purpose'].value_counts()
b.plot.bar()
plt.show()


# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

df['installment'].plot.hist()
plt.show()


df['log.annual.inc'].plot.hist()
plt.show()
# code ends here


