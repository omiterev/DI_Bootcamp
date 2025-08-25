# student_grades = {
#     "Alice": [88, 92, 100],
#     "Bob": [75, 78, 80],
#     "Charlie": [92, 90, 85],
#     "Dana": [83, 88, 92],
#     "Eli": [78, 80, 72]
# }
# student_averages = {}
# for student, grades in student_grades.items():
#     total_grade = 0 
#     for grade in grades:
#         total_grade=sum(grades)
#     student_averages[student] =int(total_grade/len(grades))
# print(student_averages)
# student_letter_grades={}
# for student, average in student_averages.items():
#     if average >=90:
#         student_letter_grades[student]='A'
#     elif 80<=average<=89:
#         student_letter_grades[student]='B'
#     elif 70<=average<=79:
#         student_letter_grades[student]='C'
#     elif 60<=average<=69:
#         student_letter_grades[student]='D'
#     elif average<60:
#         student_letter_grades[student]='F'
# print(student_letter_grades)
# class_average = sum(student_averages.values()) / len(student_averages)
# print("Class average:", class_average)
# for value in zip(student_averages.keys(), student_averages.values(),student_letter_grades.values()):
#     print(value)
#2
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]
total_sales_calculation={}
for customer in sales_data:
    total_sales_calculation.setdefault(customer["product"], 0)
    total_sales_calculation[customer["product"]] += customer["price"] * customer["quantity"]
# print(total_sales_calculation)

customer_spending_profile={}
for customer in sales_data:
    customer_spending_profile.setdefault(customer['customer_id'],0)
    customer_spending_profile[customer["customer_id"]]+=customer["price"] * customer["quantity"]
# print(customer_spending_profile)

customer_spending_profile={}
for customer in sales_data:
    customer['total_price'] = customer["price"] * customer["quantity"]
# print(sales_data)

high_value_transactions=sorted([customer['total_price'] for customer in sales_data if customer["total_price"]>500],reverse=True)
# for customer in sales_data:
#     if customer['total_price']>500:
#         high_value_transactions.append(customer["total_price"])
#high_value_transactions.sort(reverse=True)
print(high_value_transactions)

loyalty_identification=[customer for customer in sales_data if customer['quantity']>1]
print(loyalty_identification)

average_transaction_value = {}