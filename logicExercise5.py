# python script that stores the value of three different temperatures
# in celcius, converts them to fahrenheit, and prints 
# the results

# AI solution 

celcius_temperatures = [34.2, 23.34, 56.1]

for temp in celcius_temperatures:
    farenheit = (temp*1.8)+32
    print(f"C: {temp} is F: {farenheit:.2f}")