from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup(903830)
condition = lookup.condition

temp = condition.temp
print(temp)

blockTime = -2.4 * temp + 54.0

if temp > 10:
  print("Block heater should be off.")

