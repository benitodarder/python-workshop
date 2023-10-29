import pprint
import re
import sys


from variables import Variable
from variables import VariableType

VARIABLE_START = r'.*variable\s*"(.*)"'
CURLY_BRACE_OPEN = r'{'
CURLY_BRACE_CLOSE = r'}'
TYPE_START = 'type'
TYPE_END = '=\s*(' + str(VariableType.types_regex()) + ')(|\(' + str(VariableType.types_regex()) +')'
TYPE_DEFINITION = r'.*' + TYPE_START + '\s*' + TYPE_END
OBJECT_START = r'\({'
OBJECT_END = r'\})'

def generate_variables_dictionary(filename):
  curly_braces_count = 0
  error_found = False
  variables_dictionary = {}
  with open(filename, "r", newline="") as input_file:
    line = input_file.readline()
    while line:
      variable_extracted = False
      while line and not variable_extracted:
        variable_line = re.search(VARIABLE_START, line)
        if variable_line:
          variable_name = variable_line.group(1)
          print(f"New variables: {variable_name}; curly braces count: {curly_braces_count}")
          if curly_braces_count != 0:
            raise Exception("Error, new variable start found while processing one")
          elif variable_name in variables_dictionary:
            raise Exception("Error, duplicated variable")           
          else:
            variables_dictionary[variable_name] = []
            current_list = variables_dictionary[variable_name]
        curly_braces_open = re.search(CURLY_BRACE_OPEN, line)
        if curly_braces_open:
          curly_braces_count = curly_braces_count + 1
        curly_braces_close = re.search(CURLY_BRACE_CLOSE, line)
        if curly_braces_close:
          curly_braces_count = curly_braces_count - 1
          if curly_braces_open == 0:
            variable_extracted = True
            curly_braces_count = 0
        current_list.append(line.strip())
        line = input_file.readline()
  return variables_dictionary

def get_type_string(lines: list) -> str:
  for line in lines:
    simple_type = re.search(TYPE_DEFINITION, line)
    complex_type = re.search(TYPE_END, line)
    if simple_type:
      return simple_type.group(1)
    elif complex_type:
      return complex_type.group(1)
  raise Exception('Could not get variable type')

def genera_variable(variable_name: str, lines: list):
  
  return Variable(variable_name, VariableType[get_type_string(lines)], [], None)



def main(args):
  try:
    print("Testing... Testing...")
    one_variable = Variable('var name', VariableType['string'], [], None)
    print("We create a variable... This one: ")
    print(one_variable)
    another_variable = Variable('var name too', VariableType['number'], [], None)
    variables = [one_variable, another_variable]
    print("Several variables in a list...")
    print(variables)
    another_variable_too = Variable('That''s a big one...', VariableType['bool'], variables, None)
    print("Let's see a variable with fields...")
    print(another_variable_too)
    print("Reset the list...")
    print(f"Valid types: {str(VariableType.types_regex())}")
    print(f"Type regex: {TYPE_DEFINITION}'")
    variables = []
    print(variables)
    if len(args) > 1:
      variables_dictionary = generate_variables_dictionary(args[1])
      print("Variables in dictionary...")
      print(variables_dictionary)
      variables = []
      for key in variables_dictionary:
        variables.append(genera_variable(key, variables_dictionary[key]))
      print("Variables...")
      print(variables)
    print("That's all...")
  except Exception as e:
    if hasattr(e, 'message'):
        msg = e.message
    else:
        msg = e
    print(f"Unexpected exception: {msg}")
  return 0

if __name__ == '__main__':
  sys.exit(main(sys.argv))


