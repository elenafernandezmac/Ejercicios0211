import pandas as pd
"""import seaborn as sns"""
import matplotlib.pyplot as plt

data = ({
   'weather' == ["Sunny", "Sunny", "Sunny", "Cloudy", "Cloudy", "Rainy", "Rainy", "Rainy", "Rainy", "Cloudy", "Rainy", "Snowy", "Snowy", "Cloudy"],
   'twoWeeks' == ["day1","day2", "day3", "day4", "day5", "day6", "day7", "day8", "day9", "day10", "day11", "day12", "day13", "day14",]
   })
df = pd.DataFrame(data)
"""sns.lineplot(data=dataFrame, x= "weather", y= "twoWeeks")"""
plt.plot(df['weather'],df['twoWeeks'])
plt.xlabel('weather')
plt.ylabel('frecuency')
plt.title("Weather over two weeks")
plt.show()