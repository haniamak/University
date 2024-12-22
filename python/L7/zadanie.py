import aiohttp
import asyncio
from prywatne import apikey1
import sys

if sys.platform.startswith("win"):
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def fetch_data(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      if response.status == 200:
        return await response.json()
      else:
        return {"error": f"Failed to fetch data. Status code: {response.status}"}

async def fetch_city_name(location_key):
  url = f"http://dataservice.accuweather.com/locations/v1/{location_key}?apikey={apikey1}&language=pl-pl"
  return await fetch_data(url)

async def main():
  location_key1 = "349727"
  url1 = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key1}?apikey={apikey1}&language=pl-pl&details=false&metric=true"
  url2 = "https://pokeapi.co/api/v2/pokemon/pikachu"
  tasks = [
    fetch_data(url1),
    fetch_city_name(location_key1),
    fetch_data(url2)
          ]

  results = await asyncio.gather(*tasks)

  daily_forecast, city_name, pokemon = results

  forecast_date = daily_forecast.get('DailyForecasts', [{}])[0].get('Date', 'Unknown')
  temperature_min = daily_forecast.get('DailyForecasts', [{}])[0].get('Temperature', {}).get('Minimum', {}).get('Value', 'Unknown')
  temperature_max = daily_forecast.get('DailyForecasts', [{}])[0].get('Temperature', {}).get('Maximum', {}).get('Value', 'Unknown')
  weather_description = daily_forecast.get('DailyForecasts', [{}])[0].get('Day', {}).get('IconPhrase', 'Unknown')

  print(f"City 1: {city_name.get('LocalizedName', 'Unknown')}")
  #print(daily_forecast)
  print(f"Weather Forecast Date: {forecast_date}")
  print(f"Min Temperature: {temperature_min}°C")
  print(f"Max Temperature: {temperature_max}°C")
  print(f"Weather Description: {weather_description}")
  print()

  pokemon_name = pokemon.get('name', 'Unknown')
  pokemon_weight = pokemon.get('weight', 'Unknown')
  pokemon_height = pokemon.get('height', 'Unknown')

  print(f"Pokemon Name: {pokemon_name}")
  print(f"Pokemon Weight: {pokemon_weight}")
  print(f"Pokemon Height: {pokemon_height}")
asyncio.run(main())
