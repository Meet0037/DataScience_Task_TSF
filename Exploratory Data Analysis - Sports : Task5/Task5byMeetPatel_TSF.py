#Linkedin Id : https://www.linkedin.com/in/meet-patel-8896561b6/

'''
P.S = Exploratory Data Analysis - Sports

Aim  :  Perform ‘Exploratory Data Analysis’ on dataset ‘Indian Premier League’.
        As a sports analysts, find out the most successful teams, players and factors contributing win or loss of a team.
        Suggest teams or players a company should endorse for its products.

'''

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot

deliveries =pd.read_csv('deliveries.csv')
matches = pd.read_csv('matches.csv')

#Print the data of the file
print(deliveries.head())
print(matches.head())

print(deliveries.describe())
print()
print(matches.describe())
print()

print(deliveries.info())
print()
print(matches.info())
print()

#Find NULL value of the each field
print('Null Values Of Matches Dataframe : \n',matches.isnull().sum())
print()
print('Null Values Of Deliveries Dataframe : \n',deliveries.isnull().sum())
print()

#Overview of the given dataset
print("----------------------------")
print("Overview of the given dataset\n")
print("Numbers of matches played : ",matches.shape[0])
print("\nNumbers of seasons played : ",matches['season'].value_counts())
print("Top 10 well played Players of IPL : \n",matches['player_of_match'].value_counts()[:10])
print("Most Winning Team and Number Of Matches: \n",matches['winner'].value_counts())
print("Most Winning Team: \n",matches['winner'].value_counts().idxmax())
print("Player Of The Match & Number Of Matches : \n",matches['player_of_match'].value_counts())
print("Player who played the max matches : \n",matches['player_of_match'].value_counts().idxmax())

#returns all columns for the win_by_run max values
print()
print("All columns for the win_by_run max values : ")
print(matches.iloc[matches['win_by_runs'].idxmax()])

#team which won by maximum runs
print()
print("which team won by maximum runs ?")
print(matches.iloc[matches['win_by_runs'].idxmax()]['winner'])

#which team won by maximum wickets?
print()
print("which team won by maximum wickets ?")
print(matches.iloc[matches['win_by_wickets'].idxmax()]['winner'])

#which team won by minimum runs?
print()
print("which team won by minimum runs ?")
print(matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner'])

#which season had most number of matches?
print("\nwhich season had most number of matches?")
sns.countplot(x="season", data=matches)
plt.show()

#which is the most successful IPL team ?
print("\nwhich is the most successful IPL team ?")
sns.countplot(y='winner', data=matches)
pyplot.show()

top_players = matches['player_of_match'].value_counts()[:10]
fig, ax = plt.subplots()
ax.set_ylim([0,20])
#ax.set_ylabel("aaaa")
ax.set_xlabel("Players")
ax.set_title("Top 10 player of the match Winners")
sns.barplot(x = top_players.index, y = top_players, orient='v')
pyplot.show()

#Is winning the toss lead to winning the match??
match_toss = matches['toss_winner'] == matches['winner']
print(match_toss.groupby(match_toss).size())
sns.countplot(match_toss)
plt.show()

def barplot(x_axis, y_axis, plot_data, title, x_label, y_label):
    """Bar plot using seaborn library"""
    plot = sns.barplot(x=x_axis, y=y_axis, data=plot_data)
    plot.set(xlabel=x_label, ylabel=y_label)
    plot.set_title(title)
    pyplot.show()
    
#merge season value from the matches dataframe to deliveries
runs = matches[['id','season']].merge(deliveries, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
#get sum of scores by batting and bowling teams
high_scores = runs.groupby(['match_id','season','inning','batting_team','bowling_team'])['total_runs'].sum().reset_index() 
#slice by runs greater than 200
high_scores = high_scores[high_scores['total_runs']>=200]

#bar plot
barplot('season', 'match_id', high_scores.groupby(['season'])['match_id'].count().reset_index(), 'Number of 200+ scoring matches in each season', 'Season', 'Number of matches')
plt.show()


#count plots comparing scoring and conceding teams
plot, ax =plt.subplots(1,2)
sns.countplot(high_scores['batting_team'],ax=ax[0])
sns.countplot(high_scores['bowling_team'],ax=ax[1])
pyplot.show()


high_scores = deliveries.groupby(['match_id', 'inning','batting_team','bowling_team'])['total_runs'].sum().reset_index()
#high score in 1st innings
firstinning_scores = high_scores[high_scores['inning']==1]
#high score in 2nd innings
secondinning_scores = high_scores[high_scores['inning']==2]
#merge to get complete match scores
fullmatch_scores = firstinning_scores.merge(secondinning_scores[['match_id', 'inning', 'total_runs']], on='match_id')

#rename columns based on 1st and 2nd innings
fullmatch_scores.rename(columns={'inning_y':'inning_2','total_runs_x':'inning1_runs','inning_x':'inning_1','total_runs_y':'inning2_runs'},inplace=True)
fullmatch_scores = fullmatch_scores[fullmatch_scores['inning1_runs']>=200]

#engineer new column to get if the score was chased successfully or not
fullmatch_scores['chase_success'] = 1
fullmatch_scores['chase_success'] = np.where(fullmatch_scores['inning1_runs']<=fullmatch_scores['inning2_runs'], 'yes', 'no')

#pie plot success rate of teams batting second
counts = fullmatch_scores['chase_success'].value_counts().reset_index().chase_success
labels = ['Loss','Win']
plt.pie(counts,labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
plot = plt.gcf()
plot.set_size_inches(6,6)
plt.title("Win % when chasing 200+ runs")
plt.show()

''' From this we can conclude that "Mumbai Indians" are the best performing team and have won maximum time.'''

#By meet patel

