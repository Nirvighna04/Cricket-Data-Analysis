import pandas as pd
import json

with open('t20_json_files/t20_wc_match_results.json') as f:
    data=json.load(f)

# Creating a data frame
df_match=pd.DataFrame(data[0]['matchSummary'])
print(df_match.head())

# Renaming the scorecard column to match_id
df_match.rename({'scorecard':'match_id'}, axis=1,inplace=True)
print(df_match.head())

# Creating a dictionary
match_ids_dict={}

for index,row in df_match.iterrows():
    key1 = row['team1'] + ' Vs ' + row['team2']
    key2 = row['team2'] + ' Vs ' + row['team1']

    match_ids_dict[key1] = row['match_id']
    match_ids_dict[key2] = row['match_id']

# print(match_ids_dict)


with open('t20_json_files/t20_wc_batting_summary.json') as f:
    data=json.load(f)

    all_records=[]
    for rec in data:
        all_records.extend(rec['battingSummary'])

df_batting=pd.DataFrame(all_records)

df_batting["out/not_out"]=df_batting.dismissal.apply(lambda x: "out" if len(x) > 0 else "not_out")
# drop the dismissal column
df_batting.drop(columns=['dismissal'],inplace=True)
# print(df_batting)

df_batting["match_id"] = df_batting["match"].map(match_ids_dict)
print(df_batting.head())