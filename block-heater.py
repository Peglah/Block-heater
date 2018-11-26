from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup(903830)
condition = lookup.condition

print(condition.text)
