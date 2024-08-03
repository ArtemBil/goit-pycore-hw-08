from helpers.addr_book import AddressBook, Record;
from helpers.birthday import get_upcoming_birthdays;
from helpers.decorators import input_error;
from helpers.utils import parse_input;


@input_error
def add_contact(args: list, book: AddressBook):
  name, phone, *_ = args;

  record: Record = book.find(name);

  if record and phone is not None:
    is_override_approved = input('The record with such name already exists. Would you like to add a new phone (yes, no)? ');
    command, *args = parse_input(is_override_approved);

    if command == 'yes':
      record.add_phone(phone);
      return 'Contatct has successfully been updated.';
  else:
    record = Record(name);
    record.add_phone(phone);
    book.add_record(record);
    
    return 'Contatct has successfully been added.';

  return f'The contact has not been added due to rejection of adding new phone.';

@input_error
def add_birthday(args: list, book: AddressBook):
  name, birthday, *_ = args;

  record: Record | None = book.find(name);

  if record:
      record.add_birthday(birthday);
  else:
      return f'Failed to add birthday. Contact with name {name} does not exist.'

  return "Birthday has been added.";

@input_error
def show_birthday(args: list, book: AddressBook):
  name, *_ = args;

  record: Record | None = book.find(name);

  if record:
      return record.birthday.value;
  else:
      return f'Failed to show. Contact with name {name} does not exist.'

@input_error
def get_birthdays(args: list, book: AddressBook):
  return get_upcoming_birthdays(book.data);


@input_error
def update_contact(args, contacts: AddressBook):
    name, old_phone, new_phone = args
    record: Record | None = contacts.find(name);
    
    if record:
      record.edit_phone(old_phone, new_phone);
    else:
      return f'Failed to update. Contact with name {name} does not exist.'

    return "Contact has been updated.";

@input_error
def show_contact(args, contacts):
  name, *args = args;
  
  return contacts[name];

def show_all(contacts):
  for key, value in contacts.items():
    print('Contact Name: ', key, '\n');
    print('Contact Phone: ', value);
    print('--------------');
