def convert_date(date_str):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    mm, dd, yyyy = date_str.split("/")
    month_name = months[int(mm) - 1]
    return f"{month_name} {int(dd)}, {yyyy}"

date_input = input("Enter the date (mm/dd/yyyy): ")
print("Date Output:", convert_date(date_input))
