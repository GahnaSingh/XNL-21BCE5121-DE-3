import pandas as pd

# Sample transaction data
data = {
    "transaction_id": [1, 2, 3, 4, 5],
    "timestamp": ["2025-03-14 10:05:00", "2025-03-14 10:10:00", "2025-03-14 10:15:00", "2025-03-14 10:20:00", "2025-03-14 10:25:00"],
    "amount": [500, 1500, 250, 3000, 100],
    "location": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Hyderabad"],
    "status": ["Approved", "Fraud", "Approved", "Fraud", "Approved"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("transactions.csv", index=False)

print("✅ transactions.csv has been created successfully!")
