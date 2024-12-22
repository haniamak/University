import aiohttp
import asyncio
import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

if sys.platform.startswith("win"):
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def fetch_data(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      if response.status == 200:
        return await response.json()
      else:
        return {"error": f"Failed to fetch data. Status code: {response.status}"}

def save_to_csv(data, filename):
  with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Data", "Kurs"])
    for rate in data.get("rates", []): #jesli nie znajdzie rates zostanie zwrócona pusta lista
      writer.writerow([rate["effectiveDate"], rate["mid"]])

def monthly_avg(filename):
  monthly_sums = {}
  monthly_counts = {}

  with open(filename, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
      rate = float(row["Kurs"])
      date = row["Data"]
      month = datetime.strptime(date, "%Y-%m-%d").strftime("%m")
      if month not in monthly_sums:
        monthly_sums[month] = 0
        monthly_counts[month] = 0
      monthly_sums[month] += rate
      monthly_counts[month] += 1

    monthly_averages = {month: round(monthly_sums[month] / monthly_counts[month], 2) for month in monthly_sums}
  return monthly_averages

def predict_next(avg_2022, avg_2023):
  prediction = {}
  for month in avg_2022.keys():
    prediction[month] = round((avg_2022[month] + avg_2023[month]) / 2, 2)
  return prediction
    
async def main():
  url1 = "https://api.nbp.pl/api/exchangerates/rates/a/gbp/2022-01-01/2022-12-31/"
  url2 = "https://api.nbp.pl/api/exchangerates/rates/a/gbp/2023-01-01/2023-12-31/"
  url3 = "https://api.nbp.pl/api/exchangerates/rates/a/gbp/2024-01-01/2024-10-31/"
  tasks = [
    fetch_data(url1),
    fetch_data(url2),
    fetch_data(url3)
  ]
  results = await asyncio.gather(*tasks)

  kurs_gbp2022, kurs_gbp2023, kurs_gbp2024 = results

  save_to_csv(kurs_gbp2022, "kurs_gbp_2022.csv")
  save_to_csv(kurs_gbp2023, "kurs_gbp_2023.csv")
  save_to_csv(kurs_gbp2024, "kurs_gbp_2024.csv")

  print("Dane zapisane w plikach 'kurs_gbp_2022.csv', 'kurs_gbp_2023.csv', 'kurs_gbp_2024'.")

  monthly_averages_2022 = monthly_avg("kurs_gbp_2022.csv")
  monthly_averages_2023 = monthly_avg("kurs_gbp_2023.csv")
  monthly_averages_2024 = monthly_avg("kurs_gbp_2024.csv")

  print(f"Średnie miesięczne kursy w 2022 roku: {monthly_averages_2022}")
  print(f"Średnie miesięczne kursy w 2023 roku: {monthly_averages_2023}")
  print(f"Średnie miesięczne kursy w 2024 roku: {monthly_averages_2024}")

  predicted_avg_2024 = predict_next(monthly_averages_2022, monthly_averages_2023)
  print(f"Prognozowane średnie miesięczne kursy w 2024 roku: {predicted_avg_2024}")

  months = list(monthly_averages_2022.keys())
  avg_2022 = list(monthly_averages_2022.values())
  avg_2023 = list(monthly_averages_2023.values())
  avg_2024_pred = list(predicted_avg_2024.values())
  avg_2024_res = list(monthly_averages_2024.values())

  # porownanie 2022, 2023 i predykcja 2024
  plt.figure(figsize=(12, 8))
  plt.plot(months, avg_2022, label="2022", marker="o", linestyle='-', color='b')
  plt.plot(months, avg_2023, label="2023", marker="o", linestyle='-', color='r')
  plt.plot(months, avg_2024_pred, label="2024 (prognoza)", marker="o", linestyle='--', color='g')
  plt.title("Średnie miesięczne kursy GBP w latach 2022, 2023 i prognoza na 2024 rok", fontsize=14)
  plt.xlabel("Miesiąc", fontsize=12)
  plt.ylabel("Średni kurs GBP", fontsize=12)
  plt.legend()
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()

  newmonths = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]
  avg_2024_result = [monthly_averages_2024.get(month, None) for month in newmonths]
  avg_2024_predicted = [predicted_avg_2024.get(month, None) for month in newmonths]

  # Predykcja 2024 i porownanie z rzeczywistymi wynikami 2024
  plt.figure(figsize=(12, 8))
  plt.plot(newmonths, avg_2024_result, label="2024 (rzeczywiste)", marker="o", linestyle='-', color='r')
  plt.plot(newmonths, avg_2024_predicted, label="2024 (prognoza)", marker="o", linestyle='--', color='g')
  plt.title("Średnie miesięczne kursy GBP w 2024 roku (styczeń-październik) i prognoza", fontsize=14)
  plt.xlabel("Miesiąc", fontsize=12)
  plt.ylabel("Średni kurs GBP", fontsize=12)
  plt.legend()
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.show()
    

asyncio.run(main())



