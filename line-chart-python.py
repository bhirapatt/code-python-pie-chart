import pandas as pd
import matplotlib.pyplot as plt

svday_temp = { "day" : ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],
          "temp" : [6,8,6,8,10,8,6]
        }
df = pd.DataFrame(svday_temp) #สร้าง dataframe จากข้อมูล

X = df["day"]
Y = df["temp"]

plt.title("Weather in One Weeks")
plt.plot(X,Y,color="#4fe4ff", ls="-.",marker="o")
plt.show()
