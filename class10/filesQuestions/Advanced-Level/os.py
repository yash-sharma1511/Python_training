import os
folder_path = r"C:\Users\Yash Sharma\Desktop\python_training\Python_training\class10\filesQuestions\Advanced-Level"
files = os.listdir(folder_path)
text_csv_files = [f for f in files if f.endswith('.txt') or f.endswith('.csv')]
print("Found the following .txt or .csv files:")
for file in text_csv_files:
    print(file)
