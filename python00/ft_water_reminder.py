def ft_water_reminder():
	elapsed_days = int(input("Days since last watering: "))
	if elapsed_days > 2 :
		print("Water the plants!")
	else :
		print("Plants are fine")
