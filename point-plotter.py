import matplotlib.pyplot as plt

print("--- Scatter Plotter ---")

title = input("Plot Title: ")
x_name = input("X Axis Name: ")
y_name = input("Y Axis Name: ")

x_values = []
y_values = []

while True:
	new_value = input("Enter new value separated by coma (Leave blank to finish): ")
	if "," not in new_value:
		break
	try:
		coordinates = new_value.split(",")
	except:
		print("mal")
		continue
	for i in range(len(coordinates)):
		coordinates[i] = float(coordinates[i].strip())
	x_values.append(coordinates[0])
	y_values.append(coordinates[1])

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

ax.scatter(x_values, y_values)

ax.set_xlabel(x_name)
ax.set_ylabel(y_name)
ax.set_title(title)

plt.show()

