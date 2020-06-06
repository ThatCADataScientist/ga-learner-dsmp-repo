# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv(path)

data=data[data['Rating']<=5]
data['Rating'].plot(kind='hist')
plt.show()

#Code ends here


# --------------
total_null=data.isnull().sum()
percent_null=total_null/data.isnull().count()
missing_data= pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
data.dropna(axis=0,inplace=True)
total_null_1=data.isnull().sum()
percent_null_1=total_null_1/data.isnull().count()
missing_data_1=pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])
print(missing_data_1)


# --------------
import seaborn as sns
#Code starts here
sns.catplot(x="Category",y="Rating",data=data, kind="box",height = 10)
plt.xticks(rotation=90)
plt.title('Rating vs Category [BoxPlot]')
plt.show()
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

data.Installs.value_counts
data['Installs'] = data['Installs'].astype(str)
data['Installs'] = data['Installs'].str.replace(',', '')
data['Installs'] = data['Installs'].str.replace('+', '')
data['Installs'] = data['Installs'].astype(int)
data['Installs'].dtypes
le=LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
sns.regplot(x="Installs", y="Rating",data=data).set_title('Rating vs Installs [RegPlot]')
plt.show()


# --------------
#Code starts here
import seaborn as sns
print(data["Price"])
data['Price']=data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)

plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Price", y="Rating", color = 'yellow',data=data)

#Setting the title of the plot
plt.title('Rating vs Price[RegPlot]',size = 20)
plt.show()
#Code ends here


# --------------
#Code starts here
data['Genres']=data.Genres.str.split(';', expand=True)

gr_mean =data.groupby('Genres',as_index=False)[['Rating']].mean()
gr_mean
gr_mean=gr_mean.sort_values(by=['Rating'])
print(gr_mean)


# --------------

#Code starts here

data['Last Updated'] =data['Last Updated'].apply(pd.to_datetime)
max_date=data['Last Updated'].max()
max_date
data['Last Updated Days']=(max_date - data['Last Updated']).dt.days

plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Price
sns.regplot(x="Last Updated Days", y="Rating", color = 'Red',data=data)

#Setting the plot title
plt.title('Rating vs Last Updated [RegPlot]',size = 20)



