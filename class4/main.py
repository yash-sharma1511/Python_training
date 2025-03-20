# Data Pipeline Validator
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