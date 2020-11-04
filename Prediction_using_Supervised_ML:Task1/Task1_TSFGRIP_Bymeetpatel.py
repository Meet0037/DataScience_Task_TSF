#Task-1 of TSF internship
#======================================================================
#Predict the percentage of an student based on the no. of study hours.
#======================================================================

#Linkedin Id : https://www.linkedin.com/in/meet-patel-8896561b6/



'''-------------------------------------------------
Linear regression
----------------------------------------------------'''

#Import all essential module
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression


#Extract from url and print that data
url = "http://bit.ly/w-data"
data=pd.read_csv(url)
print(data)

'''-------------------------------------------------
Data visulization
----------------------------------------------------'''

#Plot a graph
data.plot(x='Hours', y='Scores', style='o')
plt.title('Percentage according to Hours of studied')
plt.xlabel('Hours studied')
plt.ylabel('Percentage Score')
plt.show()

'''-------------------------------------------------
Linear regression model
----------------------------------------------------'''

#Now we prepare the data and split it in test data
x = data.iloc[:, :-1].values
y = data.iloc[:, 1].values
x_train, x_test, y_train, y_test= train_test_split(x, y,train_size=0.80,test_size=0.20,random_state=0)

#Training the model
linearRegressor= LinearRegression()
linearRegressor.fit(x_train, y_train)
y_predict= linearRegressor.predict(x_train)

#Train the algorithm
regressor = LinearRegression()  
regressor.fit(x_train, y_train) 
print("Complete.")

#Plot the regression line
line = regressor.coef_*x+regressor.intercept_

#plotting for the test data
plt.scatter(x, y)
plt.plot(x, line);
plt.show()

#Check for accuracy of scores of testing and training set
print()
print('Test Score',regressor.score(x_test, y_test))
print()
print('Training Score',regressor.score(x_train, y_train))

#Make predictions
a = {'Actual': y_test,'Predicted': y_predict}
data= pd.DataFrame.from_dict(a, orient='index')
data = data.transpose()
print(data)

print()
print('Score of student who studied for 9.25 hours per day', regressor.predict([[9.25]]))


#Done by Meet Patel
