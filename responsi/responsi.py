In [1] :
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

In [2]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

In [3]
url='../input/cristiano-ronald-vs-lionel-messi-weekly-updated/cristiano_vs_messi.csv'
df=pd.read_csv(url)

In[4]
df.info()

In [5]
df.head(30)

In [6]
df.columns

In [7]
df['comp']=df['comp'].ffill()
df['date']=df['date'].ffill()
df['round']=df['round'].ffill()
df['venue']=df['venue'].ffill()
df['opp']=df['opp'].ffill()
df.info()

In [8]
df['min']=df['min'].apply(lambda x:x.replace("'",''))
df['min']=df['min'].apply(lambda x:x.replace("+",''))
df['min'].unique()

In [9]
df.info()

In [10]
df['min']=pd.to_numeric(df['min'])
df['time_class']=df['min'].apply(lambda x:'first_half' if x<=45 else ( 'secound_half' if 45<x<=90 else 'extra_time'))
df.head(10)

In [11]
df['assist']=df['assisted'].fillna(0)
df['solo']=df['assist'].apply(lambda x:'solo' if x==0 else 'assisted')
df.head()

In [12]
from datetime import date
df['date']=pd.to_datetime(df['date'])
#== 
L = ['year', 'month', 'day', 'dayofweek', 'dayofyear', 'weekofyear', 'quarter']
df = df.join(pd.concat((getattr(df['date'].dt, i).rename(i) for i in L), axis=1))

In [13]
df['dayofweek']=pd.to_numeric(df['dayofweek'])
df['dayofweek']=df['dayofweek'].apply(lambda x:x+1)
df['dayofweek'].unique()
df['goal']=df['goal']=1

In [14]
df.head()

In [15]
df['player'].value_counts()

In [16]
df_ronaldo=df.loc[df['player']=='ronaldo']
df_messi=df.loc[df['player']=='messi']
#===== 
ronaldo_solo=df_ronaldo[df_ronaldo['solo']=='solo'] 
ronaldo_assisted=df_ronaldo[df_ronaldo['solo']=='assisted'] 
slices=[len(ronaldo_solo),len(ronaldo_assisted)]
labels=['solo','assisted']
#==== 
messi_solo=df_messi[df_messi['solo']=='solo'] 
messi_assisted=df_messi[df_messi['solo']=='assisted'] 
slices1=[len(messi_solo),len(messi_assisted)]
labels1=['solo','assisted']
#===
fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=False)
fig.suptitle('Cristiano Vs Messi/Solo&assisted')
axes[0].pie(slices,labels=labels,startangle=90,shadow=1,explode=(0,0.4),autopct='%1.2f%%',colors=['#808080','#F2EBED']);
axes[0].set_title('Cristiano Ronaldo')
axes[1].pie(slices1,labels=labels1,startangle=90,shadow=1,explode=(0,0.4),autopct='%1.2f%%',colors=['#7868DF','#DF6870']);
axes[1].set_title('Lionel Messi');

In [17]
r_goal=pd.DataFrame(df_ronaldo['date'].value_counts().sort_values(ascending=False))
r_goal['nick']=r_goal['date'].apply(lambda x:'hatrick' if x==3 else ('haul' if x==4 else ('glut' if x==5 else ('brace' if x ==2 else 'single goal'))))
r_goal.head()

In [18]
m_goal=pd.DataFrame(df_messi['date'].value_counts().sort_values(ascending=False))
m_goal['nick']=m_goal['date'].apply(lambda x:'hatrick' if x==3 else ('haul' if x==4 else ('glut' if x==5 else ('brace' if x ==2 else 'single goal'))))
r_goal['player']='ronaldo'
m_goal['player']='messi'
#=== 
all_goal = r_goal.append(m_goal).reset_index()
all_goal.rename(columns={'date':'goal_count'},inplace=True)

In [19]
fig = px.box(all_goal, x="player", y='goal_count')
fig.show()

In [20]
plt.figure(figsize=(10,7))
sns.countplot(data=all_goal,x='nick',hue='player',palette='magma').set_title('Cristano Vs Messi (Goals in one Match)');

In [21]
plt.figure(figsize=(10,7))
sns.countplot(data=df,x='player',hue='venue',palette="Paired").set_title('Cristano Vs Messi (Home & Away)');

In [22]
plt.figure(figsize=(25,7))
sns.countplot(data=df,x='type',hue='player',palette="hls").set_title('Cristano Vs Messi (Goal Type)');

In [23]
plt.figure(figsize=(25,7))
sns.countplot(data=df,x='pos',hue='player',palette="cubehelix").set_title('Cristano Vs Messi (Goalposition)');

In [24]
r_assist =df_ronaldo['assisted'].value_counts()
r_assist = r_assist[:10]
sns.set_style("darkgrid")
plt.figure(figsize=(20,6));
r_assist_vis = sns.barplot(r_assist.index, r_assist.values, alpha=0.8,palette='winter');
plt.title('Most Player assisted to cristiano',fontsize=15);
plt.ylabel('assists', fontsize=12);
plt.xlabel('player name', fontsize=12);
r_assist_vis.set_xticklabels(rotation=30,labels=r_assist.index,fontsize=15);
plt.show();

In [25]
m_assist =df_messi['assisted'].value_counts()
m_assist = m_assist[:10]
sns.set_style("darkgrid")
plt.figure(figsize=(20,6));
m_assist_vis = sns.barplot(m_assist.index, m_assist.values, alpha=0.8,palette="coolwarm");
plt.title('Most Player assisted to messi',fontsize=15);
plt.ylabel('assists', fontsize=12);
plt.xlabel('player name', fontsize=12);
m_assist_vis.set_xticklabels(rotation=30,labels=m_assist.index,fontsize=15);
plt.show();

In [26]
r_op =df_ronaldo['opp'].value_counts()
r_op = r_op[:10]
sns.set_style("darkgrid")
plt.figure(figsize=(20,6));
r_op_vis = sns.barplot(r_op.index, r_op.values, alpha=0.8,palette="dark");
plt.title('cristiano favourite opponents',fontsize=15);
plt.ylabel('Goals', fontsize=12);
plt.xlabel('opponet', fontsize=12);
r_op_vis.set_xticklabels(rotation=30,labels=r_op.index,fontsize=15);
plt.show();

In [27]
m_op =df_messi['opp'].value_counts()
m_op = m_op[:10]
sns.set_style("darkgrid")
plt.figure(figsize=(20,6));
m_op_vis = sns.barplot(m_op.index, m_op.values, alpha=0.8,palette="Spectral");
plt.title('messi favourite opponents',fontsize=15);
plt.ylabel('Goals', fontsize=12);
plt.xlabel('opponet', fontsize=12);
m_op_vis.set_xticklabels(rotation=30,labels=m_op.index,fontsize=15);
plt.show();

In [28]
min_ronaldo1=df_ronaldo.groupby(['min']).size().to_frame('count').reset_index()
min_ronaldo=min_ronaldo1.sort_values(by='count', ascending=False)[:10]
min_ronaldo=min_ronaldo.reset_index()
min_ronaldo=min_ronaldo.rename(columns={'min':('Ronald_min')})
min_ronaldo=min_ronaldo.drop(columns=['index'])
#=====
#=====
min_messi=df_messi.groupby(['min']).size().to_frame('count').reset_index()
min_messi=min_messi.sort_values(by='count', ascending=False)[:10]
min_messi=min_messi.reset_index()
min_messi=min_messi.rename(columns={'min':('messi_min')})
min_messi=min_messi.drop(columns='index')
#==== 
min_ronaldo

In [29]
min_messi

In [30]
min_cr7=df_ronaldo[df_ronaldo['min']<90]
min_values=min_cr7['min'].values
#========
min_messi=df_messi[df_messi['min']<90]
min_values_messi=min_messi['min'].values
min_values_messi
#=== 
#figure,axes = plt.subplots(1,2,figsize=(10,5))
plt.figure(figsize=(15,5))
plt.hist(min_values,histtype='bar',bins=45,density=True,label='Ronaldo',alpha=0.5);
plt.hist(min_values_messi,bins=45,histtype='bar',density=True,label='Messi',alpha=0.5);
plt.legend(loc='upper left')

In [31]
plt.figure(figsize=(14,7))
sns.kdeplot(min_values, shade = True)
sns.kdeplot(min_values_messi, shade = True)
plt.legend(['Cristiano','Messi'])
plt.xlabel('Home Factor')

In [32]
df_stack = pd.pivot_table(df, values='goal', index=['player'],
                    columns=['time_class'], aggfunc=np.sum).reset_index()
df_stack

In [33]
sns.set_style("darkgrid")
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=False)
fig.suptitle('Cristiano Vs Messi/TimeClass')

sns.barplot(ax=axes[0], x=df_stack.player, y=df_stack.first_half,palette='icefire')
axes[0].set_title('First Half')
sns.barplot(ax=axes[1], x=df_stack.player, y=df_stack.secound_half,palette='icefire')
axes[1].set_title('Secound Half')
sns.barplot(ax=axes[2], x=df_stack.player, y=df_stack.extra_time,palette='icefire')
axes[2].set_title('Extra Time')

In [34]
df['comp'].unique()

In [35]
df_champ=df.loc[df['comp']=='Champions League']
#==== 
df_champ['player'].value_counts()

In [36]
from IPython.core.display import HTML
HTML('''<div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/4882308" data-url="https://flo.uri.sh/visualisation/4882308/embed"><script src="https://public.flourish.studio/resources/embed.js"></script></div>''')

In [37]
fig, axes = plt.subplots(1, 2, figsize=(15, 5), sharey=False)
fig.suptitle('Cristiano Vs Messi')

sns.countplot(ax=axes[0],data=df,x='dayofweek',hue='player',palette="hls")
axes[0].set_title('DayofWeek')
sns.countplot(ax=axes[1],data=df,x='quarter',hue='player',palette="hls")
axes[1].set_title('quarter')