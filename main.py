import re
import csv

purchases = {}
with open("purchase_log.txt", "r", encoding="utf-8") as LogFile:
  # итерация по строкам
  for String in LogFile:
    User_ID = re.search(r'"user_id": "(\w{10})"', String)
    Category = re.search(r'"category": "(\w+)"', String)
    if User_ID != None:
      if Category != None:
        purchases[User_ID.group(1)] = Category.group(1)

Output=['user_id', 'source', 'category'],
#New_String=f"user_id,source,category\n"

with open("visit_log.csv", "r", encoding="utf-8") as CSVFile: 
  #Читаем построчно лог
  reader = csv.DictReader(CSVFile)
  for row in reader:
    Row_ID = f"'{row['user_id']}'"
    if purchases.get(row['user_id']) != None:
#      New_String += f"{row['user_id']},{row['source']},{purchases.get(row['user_id'])}\n"
      Output += [row['user_id'], row['source'], purchases.get(row['user_id'])],
with open('funnel.csv', 'w') as File_Output:
  #Пишем в файл получившийся словарь
  Writer = csv.writer(File_Output)
  for Row_Out in Output:
    Writer.writerow(Row_Out)
