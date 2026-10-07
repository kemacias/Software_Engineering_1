def total_sales(sales_records):
    total = 0
    for record in sales_records:
        total += record['amount']
    return total

def average_sales(total, count):
    return total / count if count > 0 else 0

#def highest_sales(total):
    for record in sales_records:
            amount = record['amount']
            total += amount
            count += 1
            if amount > highest:
                highest = amount
    return highest

#def lowest_sales(total):
    def highest_sales(total):
        for record in sales_records:
            amount = record['amount']
            total += amount
        count += 1
        if amount < lowest:
            lowest = amount
    return lowest


def process_sales_data(sales_records):
    total = 0
    count = 0
    highest = float('-inf')
    lowest = float('inf')
    total = total_sales(sales_records)
    count = len(sales_records)
    #highest = highest_sales(total)
    #lowest = lowest_sales(total)
    average = average_sales(total, count)
    print("process_sales_data")
    return {"total": total, "average": average, "highest": highest, "lowest": lowest}


def process_marketing_data(marketing_records):
    total = 0
    count = 0
    highest = float('-inf')
    lowest = float('inf')
    for record in marketing_records:
        amount = record['budget']
        total += amount
        count += 1
        if amount > highest:
            highest = amount
        if amount < lowest:
            lowest = amount
    average = total / count if count > 0 else 0
    return {"total": total, "average": average, "highest": highest, "lowest": lowest}


def process_engineering_data(engineering_records):
    total = 0
    count = 0
    highest = float('-inf')
    lowest = float('inf')
    for record in engineering_records:
        amount = record['hours']
        total += amount
        count += 1
        if amount > highest:
            highest = amount
        if amount < lowest:
            lowest = amount
    average = total / count if count > 0 else 0
    print("process_engineering_data")
    return {"total": total, "average": average, "highest": highest, "lowest": lowest}

# For this challenge, do not change the following 3 lines:
sales = [{"amount": 100}, {"amount": 250}, {"amount": 75}]
marketing = [{"budget": 500}, {"budget": 300}, {"budget": 800}]
engineering = [{"hours": 40}, {"hours": 35}, {"hours": 45}]

sales_stats = process_sales_data(sales)

print("Sales Report")
print(f"  Total:   ${sales_stats["total"]:.2f}")
print(f"  Average: ${sales_stats["average"]:.2f}")
print(f"  Highest: ${sales_stats["highest"]:.2f}")
print(f"  Lowest:  ${sales_stats["lowest"]:.2f}")

marketing_stats = process_marketing_data(marketing)

print("Marketing Report")
print(f"  Total:   ${marketing_stats["total"]:.2f}")
print(f"  Average: ${marketing_stats["average"]:.2f}")
print(f"  Highest: ${marketing_stats["highest"]:.2f}")
print(f"  Lowest:  ${marketing_stats["lowest"]:.2f}")

engineering_stats = process_engineering_data(engineering)

print("Engineering Report")
print(f"  Total:   ${engineering_stats["total"]:.2f}")
print(f"  Average: ${engineering_stats["average"]:.2f}")
print(f"  Highest: ${engineering_stats["highest"]:.2f}")
print(f"  Lowest:  ${engineering_stats["lowest"]:.2f}")
