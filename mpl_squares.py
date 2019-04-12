import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
square = [1,4,9,16,25]

plt.plot(input_values,square,linewidth = 5)

plt.title("square number",fontsize = 24)
plt.xlabel("values")
plt.ylabel("square values")
plt.tick_params(axis='both',labelsize = 14)

plt.show()