import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
import os

# Input path globally for file.
input_path = os.getcwd() + "\\ClimateChange.csv"
countries_1 = ['United States', 'United Kingdom', 'Germany']
countries_2 = ['United States', 'United Kingdom', 'Germany', 'Belgium', 'Bolivia', 'Georgia', 'Libya']


def read_file(input_file):
    first_data = pd.read_csv(input_file, skiprows=4)
    first_data = first_data.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    first_data = first_data.dropna(how='all')
    first_data = first_data.set_index('Country Name')
    second_data = first_data.T

    return first_data, second_data


def plot_1(countries):
    sns.boxplot(x='Country Name', y='2016', data=first_data.loc[countries].reset_index())
    plot.ylabel('CO2 emissions per capita (metric tons)')
    mng = plot.get_current_fig_manager()
    # mng.window.state('zoomed')
    plot.show()


def plot_2(countries):
    first_data.loc[countries, '2005':].plot()
    plot.ylabel('CO2 emissions (metric tons per capita)')
    mng = plot.get_current_fig_manager()
    # mng.window.state('zoomed')
    plot.show()

def plot_3():
    my_df = pd.read_csv('ClimateChange.csv', skiprows=4)
    my_df = my_df.drop_duplicates(subset=["Country Name"], keep='first').head(3)
    plot.plot(my_df["Country Name"], my_df["2000"])
    mng = plot.get_current_fig_manager()
    # mng.window.state('zoomed')
    plot.show()


def plot_4():
    countries = ['Antigua and Barbuda', 'Qatar', 'Romania', 'Russian Federation']
    first_data.loc[countries, '2015':].plot()
    plot.ylabel('Renewable energy consumption (% of total final energy consumption)')
    plot.show()

def plot_5():
    my_df = pd.read_csv('ClimateChange.csv', skiprows=4)
    my_df = my_df.drop_duplicates(subset=["Country Name"], keep='first').head(10)
    my_df.plot.bar(x="Country Name", y="2008", rot=70, title="Bar Graph")
    plot.show(block=True)


# two dataframes returning from function.
first_data, second_data = read_file(input_path)
print(first_data.loc[countries_1, '2014'].describe())

# Plot 1 function call
plot_1(countries_1)
# Plot 2 function call
plot_2(countries_2)
# Plot 3 function call
plot_3()
# Plot 4 function call
plot_4()
# Plot 5 function call
plot_5()