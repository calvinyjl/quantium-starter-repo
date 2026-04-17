import csv
import os

with open("./combined.csv", "w") as filew:
    writer = csv.writer(filew)
    headers = ["sales", "date", "region"]
    writer.writerow(headers)

    for file in os.listdir("./data"):
        with open(f"./data/{file}", "r") as filer:
            reader = csv.reader(filer)
            next(reader)
            for row in reader:
                product = row[0]
                price = row[1]
                quantity = row[2]
                date = row[3]
                region = row[4]

                if product == "pink morsel":
                    formatted_price = float(price[1:])
                    sale = formatted_price * int(quantity)
                    writer.writerow([sale, date, region])