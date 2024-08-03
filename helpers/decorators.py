from helpers.field_exception import InvalidFieldValueException;

def input_error(func):
  def inner(*args, **kwargs):
    try:
      return func(*args, **kwargs);
    except InvalidFieldValueException as e:
      return f'Field Error: {e}'
    except ValueError as e:
      return 'ValueError: Give me name and phone please.'
    except KeyError:
      return 'KeyError: The contact does not exist.'
    except IndexError:
      return 'IndexError: The contact does not exist.'
    
  return inner;