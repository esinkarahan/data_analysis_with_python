import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = df['weight']/((df['height']/100)**2)
df['overweight'] = 1.*(bmi>25)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def norm(x):
  if x==1:
    x=0
  else:
    x=1
  return x
df['gluc'] = df['gluc'].apply(norm)
df['cholesterol'] = df['cholesterol'].apply(norm)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    df_cat = pd.melt(df,value_vars=['active','alco','cholesterol', 'gluc', 'overweight','smoke'], id_vars=['cardio'])
    df_cat=df_cat.astype({'value': 'int64'},copy=False)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = None

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(data=df_cat, 
                      x='variable', hue='value',
                      col='cardio',kind='count', 
                      ci=None)

    g.set_axis_labels("variable","total");
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

draw_cat_plot()


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heatmap = df[
    (df['ap_lo'] <= df['ap_hi'])
      & (df['height'] >= df['height'].quantile(0.025))
      & (df['height'] <= df['height'].quantile(0.975))
      & (df['weight'] >= df['weight'].quantile(0.025))
      & (df['weight'] <= df['weight'].quantile(0.975))
    ]


    # Calculate the correlation matrix
  corr = df_heatmap.corr()

    # Generate a mask for the upper triangle
  mask = np.zeros_like(corr)
  mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(8, 8))

    # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr, mask=mask, 
                     annot=True,square=True,
                     linewidths=.5,fmt='.1f',vmax=0.25, vmin=-0.1
                    )


    # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig

draw_heat_map()

