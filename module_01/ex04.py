# Seconds of My Life

user_age = int(input("Enter your age: "))

# 1 year = 365 days
# 1 day = 24 hours
# 1 hour = 60 mins
# 1 min = 60 seconds

days = user_age * 365
hours = days * 24
mins = hours * 60
seconds = mins * 60

print(f"You have been alive for {days}days or {hours}hours or {mins}mins or {seconds}seconds.")

# Which assumptions does your calculation make?
# It asuumes that there is no leap year and the use's age is exactly the number they put in
# meaning 25 and 10 days old would be still 25 years old.
