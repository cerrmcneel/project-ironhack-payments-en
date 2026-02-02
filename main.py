import pandas as pd

#cash = pd.read_csv("project_dataset/extract - cash request - data analyst.csv")
#print(cash.info())
fees = pd.read_csv("project_dataset/extract - fees - data analyst - .csv")

fees["cash_request_id"] = fees["cash_request_id"].astype("Int64")

fees_date = ["created_at", "updated_at", "paid_at", "from_date", "to_date"]


for col in fees_date:
    fees[col] = pd.to_datetime(fees[col], errors="coerce")

print(fees.info())
print(fees.head())    



#lexique = pd.read_excel("project_dataset/Lexique - Data Analyst.xlsx")
#print(lexique.info())