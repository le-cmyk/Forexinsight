import csv
from datetime import datetime


from Functions.Class.entry import Entry

class DataImports:
    @staticmethod
    def import_price_data():
        entries = []
        with open('Exness_XAUUSDm_2021.csv') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # skip header row
            for row in reader:
                if row:
                    entry = Entry(row[0], row[1], datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S'), float(row[3]), float(row[4]))
                    entries.append(entry)
        entries.sort(key=lambda x: x.timestamp())
        return entries
    
    @staticmethod
    def extract_data(entries, start, duration):
        filtered_entries = [entry for entry in entries if entry.timestamp() >= start and entry.timestamp() <= start + datetime.timedelta(seconds=duration)]
        return filtered_entries
