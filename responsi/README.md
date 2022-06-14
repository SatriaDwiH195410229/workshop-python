# Persaingan antara Lionel Messi vs Cristiano Ronaldo
Perdebatan siapa yang lebih baik di antara Lionel Messi dan Cristiano Ronaldo seakan-akan tidak kenal habis. Dua pemain itu selalu menciptakan rekor-rekor baru yang mengejutkan dunia sepak bola. Messi dan Ronaldo layak disebut sebagai **The Greatest Of All Time**.

Menganalisis data Eksplorasi untuk menghitung berbagai statistik penting seperti rata-rata gol per game.
## Berikut adalah cuplikan datasetnya :
```python
	player	comp	round	date	venue	opp	pos	min	type	assisted
0	ronaldo	Liga NOS	6	10/7/2002	H	Moreirense	RW	34'	NaN	NaN
1	ronaldo	Liga NOS	6	10/7/2002	H	Moreirense	NaN	90'	NaN	NaN
2	ronaldo	Liga NOS	8	10/26/2002	A	Boavista	NaN	88'	NaN	Carlos Martins
3	ronaldo	Taça de Portugal Placard	Fourth Round	11/24/2002	H	Estarreja	NaN	67'	Left-footed shot	César Prates
4	ronaldo	Taça de Portugal Placard	Fifth Round	12/18/2002	H	Oliv. Hospital	NaN	13'	NaN	NaN
5	ronaldo	Premier League	11	11/1/2003	H	Portsmouth	RW	80'	Right-footed shot	NaN
6	ronaldo	FA Cup	Fifth Round	2/14/2004	H	Man City	RW	74'	Tap-in	Ryan Giggs
7	ronaldo	Premier League	29	3/20/2004	H	Spurs	NaN	89'	Right-footed shot	NaN
8	ronaldo	Premier League	32	4/10/2004	A	Birmingham	NaN	60'	Header	Ryan Giggs
9	ronaldo	Premier League	38	5/15/2004	A	Aston Villa	NaN	4'	Right-footed shot	NaN
10	ronaldo	FA Cup	Final	5/22/2004	H	Millwall	RW	44'	Header	Gary Neville
11	ronaldo	Premier League	16	12/4/2004	H	Southampton	NaN	87'	Right-footed shot	Gary Neville
12	ronaldo	FA Cup	Third Round	1/19/2005	A	Exeter City	NaN	9'	NaN	Paul Scholes
13	ronaldo	Premier League	24	1/22/2005	H	Aston Villa	NaN	8'	Right-footed shot	Louis Saha
14	ronaldo	Premier League	25	2/1/2005	A	Arsenal	RW	54'	Left-footed shot	Ryan Giggs
15	ronaldo	Premier League	25	2/1/2005	A	Arsenal	RW	58'	Tap-in	Ryan Giggs
16	ronaldo	FA Cup	Fifth Round	2/19/2005	A	Everton	NaN	58'	Tap-in	Paul Scholes
17	ronaldo	FA Cup	Sixth Round	3/12/2005	A	Southampton	NaN	45'+1	Left-footed shot	Ruud van Nistelrooy
18	ronaldo	Premier League	30	3/19/2005	H	Fulham	NaN	21'	Right-footed shot	Roy Keane
19	ronaldo	FA Cup	Semi-Finals	4/17/2005	A	Newcastle	RW	76'	Right-footed shot	Ruud van Nistelrooy
20	ronaldo	Champions League Qualifying	3rd round	8/9/2005	H	Debrecen	NaN	63'	Right-footed shot	Paul Scholes
21	ronaldo	Premier League	11	10/29/2005	A	Middlesbrough	NaN	90'	Header	Paul Scholes
22	ronaldo	EFL Cup	Round of 16	11/30/2005	H	West Brom	RW	12'	Penalty	NaN
23	ronaldo	Premier League	20	12/31/2005	H	Bolton	NaN	68'	Right-footed shot	Wayne Rooney
24	ronaldo	Premier League	20	12/31/2005	H	Bolton	NaN	90'	Left-footed shot	Ruud van Nistelrooy
25	ronaldo	Premier League	25	2/4/2006	H	Fulham	NaN	14'	Direct free kick	NaN
26	ronaldo	NaN	NaN	NaN	NaN	NaN	NaN	87'	Right-footed shot	NaN
27	ronaldo	Premier League	26	2/11/2006	A	Portsmouth	RW	38'	Left-footed shot	NaN
28	ronaldo	NaN	NaN	NaN	NaN	NaN	NaN	45'	Right-footed shot	Wayne Rooney
29	ronaldo	EFL Cup	Final	2/26/2006	H	Wigan	RW	59'	NaN	Louis Saha
```
## Nilai gol
jika pemain mencetak lebih dari satu gol pada permainan hanya min dan type yang terisi
```python
df.columns
```

```python
df['comp']=df['comp'].ffill()
df['date']=df['date'].ffill()
df['round']=df['round'].ffill()
df['venue']=df['venue'].ffill()
df['opp']=df['opp'].ffill()
df.info()
```

```python
df['min']=df['min'].apply(lambda x:x.replace("'",''))
df['min']=df['min'].apply(lambda x:x.replace("+",''))
df['min'].unique()
```

## Memanipulasi
```python
df.info()
```

```python
df['min']=pd.to_numeric(df['min'])
df['time_class']=df['min'].apply(lambda x:'first_half' if x<=45 else ( 'secound_half' if 45<x<=90 else 'extra_time'))
df.head(10)
```

```python
df['assist']=df['assisted'].fillna(0)
df['solo']=df['assist'].apply(lambda x:'solo' if x==0 else 'assisted')
df.head()
```

```python
from datetime import date
df['date']=pd.to_datetime(df['date'])
#== 
L = ['year', 'month', 'day', 'dayofweek', 'dayofyear', 'weekofyear', 'quarter']
df = df.join(pd.concat((getattr(df['date'].dt, i).rename(i) for i in L), axis=1))
```

```python
df['dayofweek']=pd.to_numeric(df['dayofweek'])
df['dayofweek']=df['dayofweek'].apply(lambda x:x+1)
df['dayofweek'].unique()
df['goal']=df['goal']=1
```

## Gol
Jumlah seluruh gol yang telah dicetak kedua pemain dan perbandingan solo gol dengan assist
```python
df['player'].value_counts()
```

```python
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
```

### Gol dalam satu pertandingan
Gol yang dicetak dalam satu match, bisa terjadi 5 kemungkinan yaitu, single goal, barce, hattrick, haul, glut
```python
r_goal=pd.DataFrame(df_ronaldo['date'].value_counts().sort_values(ascending=False))
r_goal['nick']=r_goal['date'].apply(lambda x:'hatrick' if x==3 else ('haul' if x==4 else ('glut' if x==5 else ('brace' if x ==2 else 'single goal'))))
r_goal.head()
```

```python
m_goal=pd.DataFrame(df_messi['date'].value_counts().sort_values(ascending=False))
m_goal['nick']=m_goal['date'].apply(lambda x:'hatrick' if x==3 else ('haul' if x==4 else ('glut' if x==5 else ('brace' if x ==2 else 'single goal'))))
r_goal['player']='ronaldo'
m_goal['player']='messi'
#=== 
all_goal = r_goal.append(m_goal).reset_index()
all_goal.rename(columns={'date':'goal_count'},inplace=True)
```

```python
fig = px.box(all_goal, x="player", y='goal_count')
fig.show()
```

```python
plt.figure(figsize=(10,7))
sns.countplot(data=all_goal,x='nick',hue='player',palette='magma').set_title('Cristano Vs Messi (Goals in one Match)');
```

## Kandang & Tandang gol
Perbandingan gol laga home dan away kedua pemain
```python
plt.figure(figsize=(10,7))
sns.countplot(data=df,x='player',hue='venue',palette="Paired").set_title('Cristano Vs Messi (Home & Away)');
```

### Tipe gol
Tipe-tipe gol yang dicetak mereka, meliputi Left-footed shot, Right-footed shot, Tap-in, Header, Penalty, Direct free kick, Penalty rebound, Solo run, Long distance kick, Counter attack goal, Deflected shot on goal, dan Chest.
```python
plt.figure(figsize=(25,7))
sns.countplot(data=df,x='type',hue='player',palette="hls").set_title('Cristano Vs Messi (Goal Type)');
```

```python
plt.figure(figsize=(25,7))
sns.countplot(data=df,x='pos',hue='player',palette="cubehelix").set_title('Cristano Vs Messi (Goalposition)');
```

### Sahabat untuk Cristiano & Messi
Kontribusi sahabat masing-masing pemain maupun kontribusi kedua pemain ini kepada sahabat mereka.
```python
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
```

```python
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
```

### Lawan Favorit
Lawan-lawan yang sering dijebol atau menjadi lumbung gol kedua pemain ini.
```python
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
```

```python
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
```

## Waktu mencetak gol
Waktu atau durasi yang dibutuhkan kedua pemain untuk mencetak gol. Disajikan juga beberapa atribute berupa babak, antara lain : extra_time, first_hal, second_half. Serta dibeberapa kompetisi seperti, Laliga, Copa Del Rey, FA Cup, Champions League, Premier League, Club Worl Cup, UEFA Super Cup, dsb.
```python
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
```

```
	Ronald_min	count
0	90	18
1	23	14
2	45	14
3	89	13
4	76	13
5	70	13
6	82	12
7	26	11
8	68	10
9	59	10
```

```python
min_messi
```

```
	messi_min	count
0	55	13
1	87	12
2	78	12
3	45	12
4	63	11
5	82	11
6	86	11
7	90	11
8	75	11
9	16	10
```

```python
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
```

```python
plt.figure(figsize=(14,7))
sns.kdeplot(min_values, shade = True)
sns.kdeplot(min_values_messi, shade = True)
plt.legend(['Cristiano','Messi'])
plt.xlabel('Home Factor')
```

```python
df_stack = pd.pivot_table(df, values='goal', index=['player'],
                    columns=['time_class'], aggfunc=np.sum).reset_index()
df_stack
```

```
time_class	player	extra_time	first_half	secound_half
0	messi	32	276	336
1	ronaldo	27	284	345
```

```python
sns.set_style("darkgrid")
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=False)
fig.suptitle('Cristiano Vs Messi/TimeClass')

sns.barplot(ax=axes[0], x=df_stack.player, y=df_stack.first_half,palette='icefire')
axes[0].set_title('First Half')
sns.barplot(ax=axes[1], x=df_stack.player, y=df_stack.secound_half,palette='icefire')
axes[1].set_title('Secound Half')
sns.barplot(ax=axes[2], x=df_stack.player, y=df_stack.extra_time,palette='icefire')
axes[2].set_title('Extra Time')
```

```python
df['comp'].unique()
```

## Gol UEFA
Jumlah gol yang telah dicetak di gelaran UEFA Champions League
```python
df_champ=df.loc[df['comp']=='Champions League']
#==== 
df_champ['player'].value_counts()
```

```
ronaldo    134
messi      118
Name: player, dtype: int64
```

## Perlombaan Gol untuk setiap musim - 2020
Dihitung saat mereka memulai debut kompetitifnya
```python
from IPython.core.display import HTML
HTML('''<div class="flourish-embed flourish-bar-chart-race" data-src="visualisation/4882308" data-url="https://flo.uri.sh/visualisation/4882308/embed"><script src="https://public.flourish.studio/resources/embed.js"></script></div>''')
```