import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    filenames = [
        './data/sofia_temps.csv', './data/varna_temps.csv',
        './data/vidin_montana_temps.csv', './data/veliko_tarnovo_temps.csv',
        './data/kardzhali_temps.csv'
    ]

    dataframes = []
    for file in filenames:
        df_temp = pd.read_csv(file)
        dataframes.append(df_temp)

    df_all = pd.concat(dataframes, ignore_index=True)
    
    city_mapping = {
        'Sofia': 'София',
        'Varna': 'Варна',
        'Vidin_Montana': 'Видин за Монтана',
        'Veliko_Tarnovo': 'Велико Търново',
        'Kardzhali': 'Кърджали'
    }
    df_all['City'] = df_all['City'].replace(city_mapping)
    df_all['Date'] = pd.to_datetime(df_all['Date'])
    plt.figure(figsize=(14, 8))
    sns.lineplot(data=df_all,
                 x='Date',
                 y='Temperature',
                 hue='City',
                 marker='o',
                 palette='tab10',
                 linewidth=2)

    plt.title(
        'Сравнение на температурите (Април/Октомври) на водата в язовири в 5 български региона (2003-2025)',
        fontsize=16)
    plt.xlabel('Година', fontsize=12)
    plt.ylabel('Температура (°C)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='Град', title_fontsize='12', fontsize='11')

    plt.show()

if __name__ == '__main__':
    main()