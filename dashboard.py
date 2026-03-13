import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("event_log.csv")

st.title("Process Mining Dashboard")

st.subheader("Event Log Data")
st.dataframe(df)

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Calculate next activity time
df['next_time'] = df.groupby('case_id')['timestamp'].shift(-1)

# Calculate duration
df['duration'] = df['next_time'] - df['timestamp']

# Convert duration to minutes (IMPORTANT FIX)
df['duration_minutes'] = df['duration'].dt.total_seconds() / 60

# Average time per activity
activity_time = df.groupby('activity')['duration_minutes'].mean()

st.subheader("Bottleneck Detection")

fig, ax = plt.subplots()
activity_time.plot(kind='bar', ax=ax)

ax.set_xlabel("Activity")
ax.set_ylabel("Average Time (minutes)")
ax.set_title("Average Time per Activity")

st.pyplot(fig)