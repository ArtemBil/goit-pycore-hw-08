from helpers.utils import parse_input, load_data, save_data;
from helpers.command_functions import (
  add_contact,
  add_birthday,
  show_all,
  show_birthday,
  show_contact,
  get_birthdays,
  update_contact
  );

def main():
  contacts = load_data();
  print('Welcome to the assistant bot!');
  
  try:
    while True:
      user_input = input('Enter a command: ').strip().lower();
      command, *args = parse_input(user_input);
    
      if command in ['close', 'exit']:
        print('Saving data...');
        save_data(contacts);
        print('Saved succefully. Good bye!');
        break;
      elif command == 'hello':
        print('How can I help you?');
      elif command == 'add':
        print(add_contact(args, contacts));
      elif command == 'change':
        print(update_contact(args, contacts));
      elif command == 'phone':
        print(show_contact(args, contacts));
      elif command == 'add-birthday':
        # Ex: 08.08.2024
        print(add_birthday(args, contacts));
      elif command == 'show-birthday':
        print(show_birthday(args, contacts));
      elif command == 'birthdays':
        print(get_birthdays(args, contacts));
      elif command == 'all':
        show_all(contacts);
      else:
        print('Invalid command');
  except KeyboardInterrupt as e:
    print('Saving data...');
    save_data(contacts);
    print('Saved succefully. Good bye!');

if __name__ == '__main__':
  main();