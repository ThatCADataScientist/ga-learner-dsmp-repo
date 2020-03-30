# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar', title ="Gender",figsize=(15,10),legend=True, fontsize=12)
plt.show()


# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
alignment.plot.pie()
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
import pandas as pd
#strength and combat
sc_df = data[['Strength','Combat']].copy()
sc_covariance= round((sc_df['Strength'].cov(sc_df['Combat'])),2)
sc_strength = round((sc_df['Strength'].std()),2)
sc_combat = round((sc_df['Combat'].std()),2)
sc_pearson = round((sc_covariance/(sc_combat*sc_strength)),2)
#intelligence and combat
ic_df = round((data[['Intelligence','Combat']].copy()),2)
ic_covariance = round((ic_df['Intelligence'].cov(ic_df['Combat'])),2)
ic_intelligence = round((ic_df['Intelligence'].std()),2)
ic_combat = round((ic_df['Combat'].std()),2)
ic_pearson = round((ic_covariance/(ic_combat*ic_intelligence)),2)



# --------------
#Code starts here
total_high = np.quantile(data['Total'], .99)
#print(total_high)
super_best = data[data['Total']>total_high]

super_best_names = super_best['Name'].tolist()
print(super_best_names)


# --------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
fig,(ax_1,ax_2,ax_3) = plt.subplots(3,1)
ax_1.plot(data['Intelligence'])
ax_1.set_title('Intelligence')
ax_1.set_xlabel('Intelligence')
ax_1.legend()

ax_2.plot(data['Speed'])
ax_2.set_title('Speed')
ax_2.set_xlabel('Speed')
ax_2.legend()

ax_3.plot(data['Power'])
ax_3.set_title('Power')
ax_3.set_xlabel('Power')
ax_3.legend()
plt.tight_layout()
plt.show()


