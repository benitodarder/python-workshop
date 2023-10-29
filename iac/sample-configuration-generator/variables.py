from enum import Enum

class VariableType(Enum):
  string = 'string'
  number = 'number'
  bool = 'bool'
  list = 'list'
  set = 'set'
  map = 'map'
  object = 'object'
  tuple = 'tuple'
  
  @classmethod
  def types_regex(self) -> str:
    string = ""
    for currentType in VariableType:
      string = string + currentType.name + '|'
    return string[:-1]


class Variable(object):
  def __init__(self, name: str, variable_type: VariableType, fields, default):
    self.name = name
    self.variable_type = variable_type
    self.fields = fields
    self.default = default

  def __str__(self):
    return f"{self.name}/{self.variable_type.value}/[{self.fields}]"

  def __repr__(self):
    return self.__str__()
