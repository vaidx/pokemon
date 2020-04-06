import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

'''
Columns are Name, Type1, Type2,  Total, HP, Attack,
Defense, Sp.Atk, Sp. Def, Speed, Generation and Legendary
'''
pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

pkmn = pd.read_csv(r"F:\Data Science\Datasets\pokemon.csv")

#Default Scaterplot
#fit_reg=False removes the regression line
#hue sets color by evolution stage
#sns.lmplot(x='Attack', y='Defense', data=pkmn, fit_recleg=False, hue='Generation')

#boxplot
pkmn = pkmn.drop(['Total', 'Generation', 'Legendary'], axis=1)
sns.boxplot(data=pkmn)

#Violin Plot and change of theme (Used to visualize Distributions)
sns.set_style('whitegrid')
sns.violinplot(x='Type 1', y='Attack', data=pkmn)

#Swarm Plot (to show each data point)
sns.swarmplot(x='Type 1', y='Attack', data=pkmn, palette=pkmn_type_colors)

#Overlaying Violin and Swarm Plots
# Set figure size with matplotlib
plt.figure(figsize=(10,6))
 
# Create plot
sns.violinplot(x='Type 1',
               y='Attack', 
               data=pkmn, 
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)
 
sns.swarmplot(x='Type 1', 
              y='Attack', 
              data=pkmn, 
              color='k', # Make points black
              alpha=0.8) # and slightly transparent
 
# Set title with matplotlib
plt.title('Attack by Type')

#Heat Maps (visualize matrix-like data)
#pkmn = pkmn.drop(['Total', '#', 'Generation', 'Legendary'], axis=1)
corr = pkmn.corr()
sns.heatmap(corr)
plt.show()

#Histogram (allows to plot distribution of numeric variables)
sns.distplot(pkmn.Attack)
plt.show()


#Bar Plot(to visualize the distribution of categorical variables)

sns.countplot(x='Type 1', data=pkmn, palette=pkmn_type_colors)
plt.xticks(rotation=-45)
plt.show()


#Factor Plot (separate plots by categorical classes)
pkmn = pkmn[pkmn.Generation < 4]
g = sns.factorplot(x='Type 1', 
                   y='Attack', 
                   data=pkmn, 
                   hue='Generation',  # Color by stage
                   col='Generation',  # Separate by stage
                   kind='swarm') # Swarmplot
 
# Rotate x-axis labels
g.set_xticklabels(rotation=-45)
plt.show()

