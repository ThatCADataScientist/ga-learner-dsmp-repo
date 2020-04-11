# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df = pd.read_csv(path)
df.head()
X=df.drop('list_price',axis=1)
y=df['list_price']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=6)

# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = X_train.columns
fig, axes = plt.subplots(3,3, figsize=(20,8))
for i in range(3):#row numbers
    for j in range(3):#col numbers
        col = cols[ i * 3 + j]
        axes[i, j].scatter(X_train[col], y_train)
        plt.show()
        


# code ends here



# --------------
# Code starts here
corr = X_train.corr(method='pearson')
a= [(corr>0.75) | (corr<-0.75)]#We can see that the features of play_star_rating, val_star_rating and star_ratin have a correlation of greater than 0.75. We should drop two of these features to make our model better
X_train=X_train.drop(['play_star_rating','val_star_rating'],axis=1)
X_test=X_test.drop(['play_star_rating','val_star_rating'],axis=1)
print(X_train.head())
print(X_test.head())
# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()
# fit model on training data
regressor.fit(X_train, y_train)
# predict on test features
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test,y_pred)
r2= r2_score(y_test,y_pred)
print(mse)
print(r2)



# --------------
# Code starts here

residual = y_test - y_pred
# plot the figure for residual
plt.figure(figsize=(15,8))
plt.hist(residual, bins=30)
plt.xlabel("Residual")
plt.ylabel("Frequency")   
plt.title("Error Residual plot")
plt.show()


