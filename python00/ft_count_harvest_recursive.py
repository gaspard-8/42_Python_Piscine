def ft_count_harvest_recursive(max_days = int(input("Days until harvest: ")), day = 1) :
	if (day <= max_days):
		print("Day ", day)
		ft_count_harvest_recursive(max_days, day + 1)
	else :
		print("Harvest time!")
