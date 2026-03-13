import pandas as pd

df = pd.read_csv("event_log.csv")

print("Event Log Data:")
print(df)

df['timestamp'] = pd.to_datetime(df['timestamp'])

df['next_time'] = df.groupby('case_id')['timestamp'].shift(-1)

df['duration'] = df['next_time'] - df['timestamp']

print("\nActivity Duration:")
print(df[['activity','duration']])