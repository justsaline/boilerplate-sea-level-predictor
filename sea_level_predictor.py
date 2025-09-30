import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, color='red')

    # Create second line of best fit
    recent_df = df[df['Year']>= 2000]
    recent_res = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    x_pred_rec = pd.Series(range(2000,2051))
    y_pred_rec = recent_res.slope * x_pred_rec + recent_res.intercept
    ax.plot(x_pred_rec, y_pred_rec, color='green')
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()