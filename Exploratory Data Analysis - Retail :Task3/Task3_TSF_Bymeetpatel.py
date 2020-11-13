
#Linkedin Id : https://www.linkedin.com/in/meet-patel-8896561b6/

#Import all essential module
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import seaborn as sns
#from plotnine import *
import warnings
warnings.filterwarnings('ignore')

#Import data
data=pd.read_csv('SampleSuperstore.csv')
print(data.head(5))  #1

#If you want to check missing value then write,
print(data.isnull().sum()) #2
print()
print(data.info())  #3
print()
print(data.describe()) #4

#Data Cleaning
##Deleting Identicle rows to reduce noise from the data
print()
data.drop_duplicates(keep= 'first',inplace=True)
print(data) #5

'''------------------------------------'''
#Data Visulization and Data Analysis
'''------------------------------------'''

#Find total sales and profit of organization.
print("\nSales and profits of an organization\n")
Sales_profits = data.groupby('Segment').sum().iloc[:,[1,-1]].sum()
print(round(Sales_profits, 3)) #6

#Top 10 States by sales and profits
print()
Top10_sales = data.groupby('State').Sales.sum().nlargest(n=10)
Top10_profits = data.groupby('State').Profit.sum().nlargest(n=10)
print("Top 10 states by sales\n")
print(Top10_sales)  #7
print("Top 10 states by profits\n")
print(Top10_profits) #8

#Visulize it by graph
plt.style.use('seaborn')
Top10_sales.plot(kind ='bar', figsize =(14,8), fontsize =14)
plt.xlabel("States", fontsize =13)
plt.ylabel("Total Sales",fontsize =13)
plt.title("Top 10 States by Sales",fontsize =16)
plt.show() #9

plt.style.use('seaborn')
Top10_profits.plot(kind ='bar', figsize =(14,8), fontsize =14)
plt.xlabel("States", fontsize =13)
plt.ylabel("Total Profits",fontsize =13)
plt.title("Top 10 States by Profits",fontsize =16)
plt.show() #10



#Correlation Between Variables.
print(data.corr()) #11

#plot a histogram for each column 
data.hist(bins=50, figsize=(20,15))
plt.show() #12


#Barchart
sns.set(style="whitegrid")
plt.figure(2, figsize=(20,15))
sns.barplot(x='Sub-Category',y='Profit', data=data, palette='Spectral')
plt.suptitle('Pie Consumption Patterns in the United States', fontsize=16)
plt.show() #13

'''Next,"Copiers" Sub-category has gain highest amount of profit with no loss.
There are other sub-categories too who are not faced any kind of losses but their profit margins are also low.
Next,Suffering from highest loss is machines. '''

# Pair_plot
financial=data.loc[:,['Sales','Quantity','Discount','Profit']]
sns.pairplot(financial)
plt.show() #14

'''------------------------------'''
#Play with correlation matrix
'''------------------------------'''

#correlation matrix
correlation=financial.corr()
sns.heatmap(correlation,xticklabels=correlation.columns,yticklabels=correlation.columns,annot=True)
pyplot.show() #15
'''
From Above map we see that,
1)sales and profits are positively correlated
2)Discount and Profits are Negatively correlated
Hence we consider these cases and proceed further. '''

#Case-1 : When discount is 0

without_discount_data=data[data['Discount']==0]
sns.relplot(x='Sales',y='Profit',data=without_discount_data)
pyplot.show() #16

'''Hence we say that there positive relation between Profit and sales.when Discount is 0 Now we plot heat_map to get correlaton'''
correlation=without_discount_data.corr()
sns.heatmap(correlation,xticklabels=correlation.columns,yticklabels=correlation.columns,annot=True)
pyplot.show() #17

#Rel_plot with respect category
sns.relplot(x='Sales',y='Profit',hue='Category',data=without_discount_data)
pyplot.show() #18

# Regression Plot 
sns.regplot(without_discount_data['Sales'],without_discount_data['Profit'])
pyplot.show() #19
'''There is positive trend between Profit and sales'''

#Now we plot a boxplot
sns.boxplot(x='Category',y='Profit',data=without_discount_data)
pyplot.show() #20


#Case-2 : When discount is not 0
with_discount_data=data[data['Discount']!=0]
sns.relplot(x='Sales',y='Profit',hue='Discount',data=with_discount_data)
pyplot.show() #21

'''In above graph we see that as percentages of Discount increses
the sales is also goes increase but profit goes decrease.'''

#Now we can check how it can be affects on different sectors of businesses
sns.relplot(x='Sales',y='Profit',hue='Category',data=with_discount_data)

#realtion analysis by correlation matrix
correlation=with_discount_data.corr()
sns.heatmap(correlation,xticklabels=correlation.columns,yticklabels=correlation.columns,annot=True)
pyplot.show() #22

'''From Above map we see that,
1)sales and profits are also negatively correlated
2)Discount and Profits are Negatively correlated'''

pivot=pd.pivot_table(with_discount_data,index='Sub-Category',values='Profit')
pivot.plot(kind='bar')
pyplot.show()
'''from Above chart we see that copiers had highest Profit and Machines had highest loss'''

pivot=pd.pivot_table(with_discount_data,index='Sub-Category',values='Sales')
pivot.plot(kind='bar')
pyplot.show() #23
'''from above chart we see that copiers had highest sale and Machines had second highest sales'''

'''In above two graph we see that 'Machines' had second highest sale but due to large discount it is in loss and
in second graph we see that sales in 'Fasteners','labels'and 'Art' category are so weak.so we have to concentrate on these sub-category businesses. '''

'''----------------------------------------------'''
#Distribution of Profits across diffrent regions
'''-----------------------------------------------'''

#Profit by region with segment
plt.figure(figsize = (12,4))
sns.set(font_scale=1, palette= "viridis")
sns.barplot(data = data , x = "Region",y = "Profit" ,hue = "Segment")
pyplot.show() #24
'''See that each segment is profitable'''

#Profit by region with category
plt.figure(figsize = (12,4))
sns.set(font_scale=1, palette= "viridis")
sns.barplot(data = data , x = "Region",y = "Profit" ,hue = "Category")
pyplot.show() #25
'''Furniture Category is the only loss making sector that to only in Central Region'''

'''--------------------------------------------------------------'''
#Investigating losses in Furniture category in the Central region
'''---------------------------------------------------------------'''

# Grouping Data by Region and only slicing Data for Central Region from whole Data Set
gb_Central = list(data.groupby("Region"))[0][1]

# Investing Further in cenral Region 
plt.figure(figsize = (12,4))
sns.set(font_scale=1.5, palette= "viridis")
sns.barplot(data = gb_Central, x = "Category",y = "Profit" ,hue = "Ship Mode")
plt.title("Investigation of central region: Profit making(by Ship Mode)")
pyplot.show() #26

'''From above chart Losses are inccured in Furniture Cateory irrespective to ship mode in Central Region'''

#Slicing Furniture Data from whole data set
gb_Category_Furniture =list(list(data.groupby("Region"))[0][1].groupby("Category"))[0][1]

# Correlation matrix
plt.figure(figsize = (12,8))
sns.set(font_scale=1.4)
sns.heatmap(gb_Category_Furniture.corr() , annot = True, cmap ="Reds")
pyplot.show() #27

'''From above matrix
There is unusually high positive correlation between Postal Code and Discount
Also, Their is negative correlation between Discount and Sales eventhough dicounts are entered as positive values...
they are not helping in improving sales of "Furniture" category of the company'''

'''--------------------------------------------------------------------'''
#Investigating individual performance by states in the central region
'''--------------------------------------------------------------------'''

#Investigation of Furniture Category in Central Region: Profit Analysis(by Sub Category)
plt.figure(figsize = (12,8))
sns.set(font_scale=1, palette= "viridis")
sns.barplot(data = gb_Category_Furniture , x = "State",y = "Profit" ,hue = "Sub-Category")
plt.title("Investigation of Furniture Category in Central Region: Profit Analysis(by Sub Category)", fontsize = 20)
pyplot.show() #28

#Investigation of Furniture Category in Central Region: Profit Analysis(by Sub Segment)
plt.figure(figsize = (12,8))
sns.set(font_scale=1, palette= "viridis")
sns.barplot(data = gb_Category_Furniture , x = "State",y = "Profit" ,hue = "Segment")
plt.title("Investigation of Furniture Category in Central Region: Profit Analysis(by Segment)", fontsize = 20)
pyplot.show() #29

'''From above chart Texas and Illiois are only two states contributing to all the losses in Furniture category in the Central Region'''
'''Losses in Tables Sub Category is significanlty high.'''

'''Question : What they are doing differently?'''

plt.figure(figsize = (12,8))
sns.set(font_scale=1, palette= "viridis")
sns.barplot(data = gb_Category_Furniture , x = "State",y = "Discount" ,hue = "Sub-Category")
plt.title("Discounts provided by each state", fontsize = 20)
pyplot.show() #30

'''From above chart we see that,
Texas and Illinois are only states providing discounts in the whole central region this justifies high positive correlation between postal codes and discounts.
Also, these discounts are very high!
1. 60% on Furnishings.
2. 30% on Bookcases and Chairs.
3. 50% disount on Tables in Illinois and 30% in Texas.
'''

plt.figure(figsize = (12,8))
sns.set(font_scale=1.5)
sns.lmplot(data = gb_Category_Furniture , x = "Discount", y ="Sales", aspect = 1, height = 8, col ="Sub-Category", col_wrap= 2)
plt.show() #31

'''From above all chart you see that discount increases along with sales decreases.'''

'''-------------------------------------------------'''
#Some more insights regarding Distribution of data
'''--------------------------------------------------'''

# box plot
sns.boxplot(x='Category',y='Profit',data=data)
pyplot.show() #32

'''From above box plot we conclude that Technology sector is more variation than two other sectors'''

#Category vs Discount
pivot=pd.pivot_table(data,index='Category',values='Discount')
pivot.plot(kind='bar')
pyplot.show() #33

#Category vs Sales
pivot=pd.pivot_table(data,index='Category',values='Sales')
pivot.plot(kind='bar')
pyplot.show() #34

#Category vs profit
pivot=pd.pivot_table(data,index='Category',values='Profit')
pivot.plot(kind='bar')
pyplot.show() #35

'''
From above three plot we say that,
1) More Discount is given in Furniture category and less Discount is given in Technology category businesses
2) Sales of Technology category businesses are more as compared to Furniture category
3) Profit of Technology category businesses are more as compared to Furniture category
'''

#Final conclusion

'''Hence To get good profit in any business you have to focus on increasing sales but not giving more discount'''


#Done by Meet Patel
