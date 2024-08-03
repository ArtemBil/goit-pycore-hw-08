import datetime;

def get_upcoming_birthdays(users: dict):
  today = datetime.datetime.today().date();
  modified_users = users.values();
  upcoming_birthdays_result = [];

  for user in modified_users:
    birthday_this_year = datetime.datetime(today.year, user.birthday.value.month, user.birthday.value.day).date();
    
    if birthday_this_year >= today and birthday_this_year - today <= datetime.timedelta(days=7):
      day_name = birthday_this_year.strftime("%A");
      
      match day_name:
        case 'Saturday':
          birthday_this_year += datetime.timedelta(days=2);
        case 'Sunday':
          birthday_this_year += datetime.timedelta(days=1);
        case _:
          pass;

      upcoming_birthdays_result.append({'name': user.name.value, 'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')});

  return upcoming_birthdays_result;