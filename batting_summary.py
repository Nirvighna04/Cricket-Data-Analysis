import pandas as pd
import json

with open('t20_json_files/t20_wc_batting_summary.json') as f:
    data=json.load(f)

    all_records=[]
    for rec in data:
        all_records.extend(rec['battingSummary'])

df_batting=pd.DataFrame(all_records)

df_batting["out/not_out"]=df_batting.dismissal.apply(lambda x: "out" if len(x) > 0 else "not_out")
# drop the dismissal column
df_batting.drop(columns=['dismissal'],inplace=True)
print(df_batting)