from enum import Enum

class VariableType(Enum):
  
  string = 'string'
  number = 'number'
  boolean = 'bool'
  list = 'list'
  set = 'set'
  map = 'map'
  object = 'object'
  tuple = 'tuple'
  
  @classmethod
  def types_regex(self) -> str:
    string = ""
    for currentType in VariableType:
      string = string + currentType.value + '|'
    return string[:-1]

  @classmethod
  def types_regex_primitives(self) -> str:
    string = ""
    for index, currentType in enumerate(VariableType):
      if index < 3:
        string = string + currentType.value + '|'
    return string[:-1]

  @classmethod
  def types_regex_collections(self) -> str:
    string = ""
    for index, currentType in enumerate(VariableType):
      if index > 2:
        string = string + currentType.value + '|'
    return string[:-1]


class Variable(object):
  
  def __init__(self, name: str, variable_type: VariableType, default_value):
    self.name = name
    self.variable_type = variable_type
    self.default_value = default_value

  def __str__(self):
    return f"{self.name}/{self.variable_type.value}/{self.default_value}"

  def __repr__(self):
    return self.__str__()
    
class VariableString(Variable):
  
  def __init__(self, name: str, default_value: str):
    super(VariableString, self).__init__(name, VariableType['string'], default_value)

class VariableBoolean(Variable):
  
  def __init__(self, name: str, default_value: bool):
    super(VariableBoolean, self).__init__(name, VariableType['boolean'], default_value)

class VariableNumeric(Variable):
  
  def __init__(self, name: str, default_value: float):
    super(VariableNumeric, self).__init__(name, VariableType['number'], default_value)

class VariableCollection(Variable):
  
  def __init__(self, name: str, variable_type: VariableType, default_value, variable_stored):
    super(VariableCollection, self).__init__(name, variable_type, default_value)    
    self.variable_stored = variable_stored
    
  def __str__(self):
    return f"{self.name}/{self.variable_type.value}({self.variable_stored.value})/{self.default_value}"    
    
class VariableList(VariableCollection):
  
  def __init__(self, name: str,  default_value: list, variable_stored: VariableType):
    super(VariableList, self).__init__(name, VariableType['list'], default_value, variable_stored)

class VariableMap(VariableCollection):
  
  def __init__(self, name: str, default_value: dict, variable_stored: VariableType):
    super(VariableList, self).__init__(name, VariableType['map'], default_value, variable_stored)

class VariableTuple(VariableCollection):
  
  def __init__(self, name: str, default_value: tuple, variable_stored: list):
    super(VariableTuple, self).__init__(name, VariableType['tuple'], default_value, variable_stored)

  def __str__(self):
    return f"{self.name}/{self.variable_type.value}({self.variable_stored})/{self.default_value}" 

class VariableObject(VariableCollection):
  
  def __init__(self, name: str, default_value: dict, fields: list[Variable]):
    super(VariableList, self).__init__(name, VariableType['object'], default_value, None)
    self.fields = fields
