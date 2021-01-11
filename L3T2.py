def user(name, last_name, birthday, city, email, telephone):
    print(f"name - {name}; "
          f"last_name - {last_name}; "
          f"birthday- {birthday}; "
          f"city - {city};"
          f"email - {email};"
          f"telephone - {telephone} ")


name = input('Enter name ')
last_name = input('Enter last name ')
birthday = input('Enter birthday ')
city = input('Enter city ')
email = input('Enter email ')
telephone = input('Enter telephone ')

user(name, last_name, birthday, city, email, telephone)