def greet_user(name):
    print(f"Hello, {name}! Welcome back.")

def get_favourite_subject():
    subject = input("What is your favourite subject? ")
    return subject

def print_summary(name, subject):
    print(f"{name}'s favourite subject is {subject}.")

def check_python(subject):
    if subject.lower() == "python":
        print("Great choice! Python is awesome!")

if __name__ == "__main__":
    name = input("What is your name? ")
    greet_user(name)
    favourite_subject = get_favourite_subject()
    print_summary(name, favourite_subject)
    check_python(favourite_subject)


from datetime import date

def days_between(date1, date2):
    d1 = date(*date1)
    d2 = date(*date2)
    delta = d2 - d1
    return delta.days

sample_dates = (2014, 7, 2), (2014, 7, 11)
result = days_between(*sample_dates)
print(result, "days")








