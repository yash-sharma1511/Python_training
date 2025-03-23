# Data Pipeline Validator
# **Task**: Identify the longest pipeline and return pipelines taking more than a given threshold time.
def pipe(pipeline,threshold):
    longest=max(pipeline,key=lambda x:x[1])[0]
    exceed=[name for name,time in pipeline if time>threshold]
    print("Longest Pipeline:",longest)
    print("Pipelines exceeding threshold:", exceed)

pipelines = [
    ("Data Ingestion", 30),
    ("Preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20)
]
threshold = 40

pipe(pipelines,threshold)

# Log File Parser
# **Task**: Extract unique error codes from a log file.
def code(logs):
    ans=set()
    for line in logs.split('\n'):
        if line.startswith('ERROR'):
            parts=line.split()
            if len(parts)>1:
                ans.add(parts[1].replace(":",""))
    return sorted(ans)            
    
logs = """ERROR 404: Not Found
INFO: Connection established
ERROR 500: Internal Server Error
ERROR 404: Not Found
"""

print("Unique Error Code:",code(logs))

# Config File Reader
# **Task**: Parse key-value pairs from a configuration string.
def split(config):
    return [tuple(pair.split("=")) for pair in config.split(';')]
    
config = "host=127.0.0.1;port=8080;mode=debug"
print(split(config))

# Social Media Data Cleaner
# **Task**: Extract unique hashtags from a social media post.
def clean(post):
    ans=list(set(word for word in post.split() if word.startswith("#")))
    return ans

post = "Loving the new #Python course! #Coding #Python #Learning"
print(clean(post)) 

# Secret Code Decoder
# **Task**: Extract every third character from a string.
def decode(msg):
    return msg[::3]

msg = "hweollrolwd"
print(decode(msg))

# Inventory Tracker
# **Task**: Find the product with the highest quantity.
inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
]

ans=max(inventory,key=lambda x:x[1])[0]
print(ans)

# Survey Data Analyzer
# **Task**: Extract scores from a survey string and find min/max.
data = "5,3,4,1,2"
num=list(map(int,data.split(",")))
print("Max=",max(num),"Min=",min(num))

# Access Control Manager
# **Task**: Manage user access levels using lists and tuples.
users = ["Alice", "Bob", "Charlie"]
roles = ("Admin", "Editor", "Viewer")
for i,j in zip(users,roles):
    print(f"{i} : {j}")

# Customer Support Ticket System
# **Task**: Categorize tickets based on message length.
def categorize(msg):
    val=len(msg)
    if val<20:
        return "Short"
    elif val>20 and val<60:
        return "Medium"
    else:
            return "Long"
            
msg = "My account is locked, please help!"
print("Category:",categorize(msg))            

# Product Catalog Manager
# **Task**: Find the product with the longest name.
def longest(products):
     return max(products,key=len)

products = ["Laptop", "Smartphone", "Wireless Headphones"]
print(longest(products))

# Sensor Data Analyzer
# **Task**: Extract the last 10 sensor readings and calculate the average.
def avg(reading):
   return sum(reading[-10::])/10
reading = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
print(int(avg(reading)))

# Transaction Reverser
# **Task**: Reverse the list of transactions.
transactions = [100, -50, 200, -150, 50]
print(transactions[::-1])

# Log Formatter
# **Task**: Format logs with timestamps.
logs = ["System Boot", "Network Connected", "User Login"]
timestamp = "2025-03-20"
ans=[f"{timestamp}: {log}" for log in logs ]
print(ans)

# Pattern Generator
# **Task**: Generate patterns with repetition.
symbol = "*"
count = 5
print(symbol*count) 

# Customer Feedback Analyzer
# **Task**: Count keyword occurrences.
feedback = "The product is excellent, absolutely excellent!"
ans=feedback.lower().count('excellent')
print("excellent count: ",ans)

# Sentence Index Finder
# **Task**: Find the index of the first occurrence of "error".
log = "INFO: All systems go. ERROR: Failed to start service error."
print(log.lower().index('error'))

# CSV Parser
# **Task**: Parse CSV data into lists.
data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
ans = [row.split(",") for row in data.split("\n")]
print(ans)

# Generate usernames from full names
# **Task**: Generate usernames from full names.
names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
ans = [name.split()[0][0] + name.split()[1] for name in names]
print(ans)

# Chat Log Analyzer
# **Task**: Count messages per user from chat logs.
chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]
msg={}
for log in chat_logs:
    user=log.split(":")[0]
    msg[user]=msg.get(user,0)+1
for user,msg in msg.items():
    print(f"{user}:{msg} messages")

# Data Compressor
# **Task**: Compress recurring substrings.
data = "abababababab"
pattern='ab'
count=data.count(pattern)
print(f"'{pattern}' repeated: {count} times")