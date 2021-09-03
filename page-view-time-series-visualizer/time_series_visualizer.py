import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv("fcc-forum-pageviews.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index(df['date'],inplace=True,drop=True)
df = df.drop(labels='date',axis=1)
# Clean data
df = df[(df['value']<=df['value'].quantile(q=0.975)) &
        (df['value']>=df['value'].quantile(q=0.025))]

def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(1,1,figsize=(10,6))
    df.plot(c='r',ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019');

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_monthly = df.groupby(by=[df.index.year, df.index.month]).mean()
    df_monthly.index.set_names(['year', 'month'],inplace=True)
    df_monthly.reset_index(inplace=True)

    # Draw bar plot
    fig,ax=plt.subplots(1,1,figsize=(6,6))
    g=sns.barplot(data=df_monthly, x='year',y='value',hue='month',palette='bright',ax=ax)
    ax.set(xlabel="Years", ylabel="Average Page Views")  
    handles, labels=g.get_legend_handles_labels()
    # replace labels
    new_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 
                  'November', 'December']
    ax.legend(handles, new_labels, loc='upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # Draw box plots (using Seaborn)
    fig,[ax1,ax2]=plt.subplots(1,2,figsize=(12,6))
    sns.boxplot(data=df_box, x='year',y='value',ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    sns.boxplot(data=df_box, x='month',y='value',ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    labs= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax2.set_xticklabels(labs);
    fig.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
