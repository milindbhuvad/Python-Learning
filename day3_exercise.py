def calculate_hike(current_salary,hike_percentage):
    hike_amount = (current_salary * hike_percentage) / 100
    return hike_amount

current_salary = 50000
hike = calculate_hike(current_salary, 20)
new_salary = current_salary + hike

print(f"Hike: {hike:.0f}")
print(f"New Salary: {new_salary:.0f}")