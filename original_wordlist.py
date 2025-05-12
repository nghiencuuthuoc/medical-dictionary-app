import pandas as pd

# Load file CSV
df = pd.read_csv("medical_vocabulary.csv")

# Lọc bỏ giá trị rỗng và trùng lặp
wordlist = df['original'].dropna().drop_duplicates()

# Lưu vào file wordlist.txt
wordlist.to_csv("wordlist.txt", index=False, header=False)

# print("✅ Saved wordlist.txt successfully!")
print("Saved wordlist.txt successfully!")

