# WARNING - PRE ALPHA. CODE MIGHT NOT EVEN BE WRITTEN!

# Block-heater
Temp and timer function for the block heater using a RPi and relays. Temp/time based on [Energimyndighetens recommendations](https://energiradgivningen.se/system/tdf/anvand_motorvarmare_ratt.pdf?file=1).

# Dependencies
[weather-api](https://pypi.org/project/weather-api/)
```
pip install weather-api
```

# Theory
* 10°C = 30 min
* -15°C = 90 min

* y = -2.4 x + 54.0

* Never run above 10 and never for longer then 90 mins.
