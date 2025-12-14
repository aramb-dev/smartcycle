print("Welcome to the Module 1 Smartcycle Data Processing Application!")

# init values
distances = [24.5, 31.2, 27.8,45.6,62.4,38.9]
battery = [48,55,61,52,47,59,'24']

if len(distances) != 7:
    print("Distance data is incomplete.")
    missed_day = int(input("Which day is missing distance data? Use a number (e.g. 1, 2, 3, 4, 5, 6, 7) > "))
    new_distance = float(input(f"Please enter the distance for day {missed_day} > "))
    distances.insert(missed_day - 1, new_distance)
elif len(battery) != 7:
    print("Battery data is incomplete.")
    missed_day = int(input("Which day is missing battery data? Use a number (e.g. 1, 2, 3, 4, 5, 6, 7) > "))
    new_battery = int(input(f"Please enter the battery percentage for day {missed_day} > "))
    battery.insert(missed_day - 1, new_battery)


for day in range(len(distances)):
    if distances[day] >=20 and distances[day] <=80:
        return
    else:
        print(f"Data for day {day + 1} seems off: Distance = {distances[day]}, Battery = {battery[day]}")
        corrected_distance = float(input(f"Please enter the correct distance for day {day + 1} > "))
        distances[day] = corrected_distance

for day in range(len(battery)):
    if battery[day] >=40 and battery[day] <=60:
        return
    else:
        print(f"Data for day {day + 1} seems off: Distance = {distances[day]}, Battery = {battery[day]}")
        corrected_battery = int(input(f"Please enter the correct battery percentage for day {day + 1} > "))
        battery[day] = corrected_battery

# check for corrupted distance entries, which is everything but floats and ints

for day in range(len(distances)):
    if not (type(distances[day]) is float or typeof(distances[day]) is int):
        print(f"Data for day {day + 1} seems off: Distance = {distances[day]}, Battery = {battery[day]}")
        corrected_distance = float(input(f"Please enter the correct distance for day {day + 1} > "))
        distances[day] = corrected_distance

# check for currupted battery entries, which is everything but integers
for day in range(len(battery)):
    if not type(battery[day]) is int:
        print(f"Data for day {day + 1} seems off: Distance = {distances[day]}, Battery = {battery[day]}")
        corrected_battery = int(input(f"Please enter the correct battery percentage for day {day + 1} > "))
        battery[day] = corrected_battery
    
# search for any outliers in distance data (e.g., values below 20 or above 80) only dryruning
for day in range(len(distances)):
    if distances[day] < 20 or distances[day] > 80:
        print(f"Outlier detected for day {day + 1}: Distance = {distances[day]}")
    
# slide end of week data from day 5 to 7 and output a report based on driving
day5_to7_distances = distances[4:7]
day5_to7_battery = battery[4:7]
total_distance = sum(day5_to7_distances)
average_battery = sum(day5_to7_battery) / len(day5_to7_battery)
print(f"From day 5 to 7, the total distance driven was {total_distance} m.")
print(f"The average battery percentage from day 5 to 7 was {average_battery}%.")

# concatenate distance and battery data into a single report for the week
weekly_report = []
for day in range(len(distances)):
    weekly_report.append({
        "day": day + 1,
        "distance": distances[day],
        "battery": battery[day]
    })
print("Weekly Report:")
for entry in weekly_report:
    print(f"Day {entry['day']}: Distance = {entry['distance']} m, Battery = {entry['battery']}%")

# display an ascii bar graph
# each day 1 '#' is equal to 5 miles. 

print("Distance Bar graph for each day:")
print("Each '#' represents 5 miles.")
for day in range(len(distances)):
    hashes = int(distances[day]/5)
    print(f"Day {day+1}: "+"#"*hashes)
    print("\n")
    print("end of report.")

print("This is the end of the Module 1 program.")