from collections import UserDict
from datetime import datetime;
from helpers.field_exception import InvalidFieldValueException;

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    IS_REQUIRED = True
    
    def __init__(self, value):
         if self.IS_REQUIRED and (value is None or value == ''):
             raise InvalidFieldValueException('Field Name is required');
         
         super().__init__(value);
              
class Phone(Field):
    IS_REQUIRED = True;
    REQURIED_LENGTH = 10;

    def __init__(self, value):
            if self.IS_REQUIRED and (value is None or value == ''):
                raise InvalidFieldValueException('Field Phone is required');
            
            if len(value) != self.REQURIED_LENGTH:
                raise InvalidFieldValueException(f'Field Phone must contain exactly {self.REQURIED_LENGTH} numbers');
            
            super().__init__(value);
            
class Birthday(Field):
  def __init__(self, value):
    
        try:
            birthday_date = datetime.strptime(value, '%d.%m.%Y').date();
            super().__init__(birthday_date);
        except ValueError:
            raise InvalidFieldValueException('Invalid date format. Use DD.MM.YYYY');
      
class Record:
    def __init__(self, name):
        self.name = Name(name);
        self.phones = [];
        self.birthday = None;

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}";
    
    def add_phone(self, phone):
           self.phones.append(Phone(phone));
    
    def remove_phone(self, target):
           self.phones = list(filter(lambda phone: phone.value != target, self.phones));

    def find_phone(self, phone):
           if phone in self.phones:
                return phone;

    def edit_phone(self, phone, new_phone):
          if phone in self.phones:
              self.phones[self.phones.index(phone)] = new_phone;
    
    def add_birthday(self, birthday):
      self.birthday = Birthday(birthday);

class AddressBook(UserDict):
       def add_record(self, record):
              self.data[record.name.value] = record;
              
       def find(self, name: str):
         return self.data.get(name);

       def delete(self, name: str):
            self.data.pop(name);