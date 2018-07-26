import data
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# variables
data_refresh_time = 2 #second
data_refresh_size = 5 #download x minut data
data_limit_begin = 0
data_limit_end = 200

df = data.loadData(2000)
df_realtime = df[:data_limit_end]
print(df_realtime)

# create chart
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.clear()
ax1.plot(df_realtime['date_time'], df_realtime['close'])

# refresh chart data
def refreshData(i):
    global data_refresh_size
    global data_limit_begin
    global data_limit_end

    print("Refreshing chart data...")
    data_limit_begin += data_refresh_size
    data_limit_end += data_refresh_size
    df_realtime = df[data_limit_begin:data_limit_end]

    ax1.clear()
    ax1.plot(df_realtime['date_time'], df_realtime['close'])

# show chart
# ani = animation.FuncAnimation(fig, refreshData, interval = data_refresh_time * 1000)

plt.show()