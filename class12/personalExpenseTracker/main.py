expenses=[1000,2500,1500,1200]
transaction_count=len(expenses)
def add_expense(expenses: list[float], amount: float) -> None:
       global transaction_count
       expenses.append(amount)
       transaction_count+=1
       return expenses
print(add_expense(expenses,5000))      
def total_expense(expenses: list[float]) -> float:
       total=0
       total+=sum(expenses)
       return total
# print(total_expense(expenses)) 
def highest_expense(expenses: list[float]) -> float:
       highest=max(expenses)
       return highest
# print(highest_expense(expenses))
def average_expense(expenses: list[float]) -> float:
       avg=total_expense(expenses)/len(expenses)
       return avg
# print(average_expense(expenses))
def expense_summary(expenses: list[float]) -> dict[str, float]:
      return {
             "total":total_expense(expenses),
             "average":average_expense(expenses),
             "highest":highest_expense(expenses),
             "transaction":transaction_count

      }
print(expense_summary(expenses))