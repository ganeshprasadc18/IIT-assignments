import matplotlib
import matplotlib.pyplot as plt

#graph to display time taken to generate/sort records
record_count= [1000,100000,10000000]
generation_time= {'real': [12.699, 330.109, 4274.4], 'user': [9.277, 236.217, 2590.8], 'sys': [3.053, 84.562, 1039.8] }

#sorting time data
#sorting_time= {'real': [0.014, 0.138, 3.242], 'user': [0.005, 0.100, 2.126], 'sys': [0.003, 0.018, 0.240]}

fig, axis = plt.subplots()

for label, data in generation_time.items():
	axis.plot(record_count, data, label=label)
	
#use this for - sorting time graph
#for label, data in sorting_time.items():
#	axis.plot(record_count, data, label=label)
	
axis.legend()	
axis.set(xlabel='Record Count', ylabel='Time (s)', title='Time for Generating Records')
axis.grid()


fig.savefig("Py_graph.png")
plt.show()
