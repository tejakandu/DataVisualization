import matplotlib.pyplot as plt

x_values = list(range(1,1000))

y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=200,edgecolors='none',c= y_values,cmap=plt.cm.Blues)


plt.title("square numbers",fontsize = 24)
plt.xlabel("values",fontsize = 14)
plt.ylabel("square values",fontsize = 14)
plt.tick_params(axis='both',which = 'minor',labelsize = 14)
plt.axis([0,1100,0,1100000])
plt.savefig('square_plot.png',aa= 'tight')
# plt.plot


