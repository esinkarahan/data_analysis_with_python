import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig,ax=plt.subplots()
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],               s=5,c='steelblue',alpha=0.7)
    
    # Create first line of best fit
    result1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x1 = range(1880,2051)
    ypred1 = result1.slope*x1 + result1.intercept
    ax.plot(x1,ypred1,c='r',label = 'prediction since 1880')


    # Create second line of best fit
    result2 = linregress(df.loc[df['Year']>=2000,'Year'],df.loc[df['Year']>=2000,'CSIRO Adjusted Sea Level'])
    x2 = range(2000,2051)
    ypred2 = result2.slope*x2 + result2.intercept
    ax.plot(x2,ypred2,c='m',label = 'prediction since 2000')

    # Add labels and title
    ax.set(xlabel='Year',
            ylabel='Sea Level (inches)',              title='Rise in Sea Level');
    ax.legend();

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()