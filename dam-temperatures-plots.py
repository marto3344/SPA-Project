import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def line_plot(df: pd.DataFrame, region, file_name):
     plt.figure(figsize=(14, 8))
     sns.lineplot(data=df,
                  x='Date',
                  y='Temperature',
                  marker='o',
                  linewidth=2)

     title = f'Сравнение на температурите (Април/Октомври) на водата в язовири в региона {region} (2003-2025)'
     plt.title(title, fontsize=16)
     plt.xlabel('Година', fontsize=12)
     plt.ylabel('Температура (°C)', fontsize=12)
     plt.grid(True, linestyle='--', alpha=0.7)
     plt.savefig(file_name)
     plt.close()

def main():
    filenames = [
        './data/sofia_temps.csv', './data/varna_temps.csv',
        './data/vidin_montana_temps.csv', './data/veliko_tarnovo_temps.csv',
        './data/kardzhali_temps.csv'
    ]

    city_mapping = {
        'Sofia': 'София',
        'Varna': 'Варна',
        'Vidin_Montana': 'Видин за Монтана',
        'Veliko_Tarnovo': 'Велико Търново',
        'Kardzhali': 'Кърджали'
    }

    for file in filenames:
        df = pd.read_csv(file)
        city  = df.loc[0, "City"]
        region = city_mapping[city]
        df['City'] = df['City'].replace(city_mapping)
        df['Date'] = pd.to_datetime(df['Date'])
        line_plot(df, region, f'./images/{city}.png')

if __name__ == '__main__':
    main()