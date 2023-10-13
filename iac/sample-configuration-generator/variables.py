class Variable(object):
  def __init__(self, name, variable_type, fields, default):
    self.name = name
    self.variable_type = variable_type
    self.fields = fields
    self.default = default

  def __str__(self):
    return f"{self.name}/{self.variable_type}/[{self.fields}]"

  def __repr__(self):
    return self.__str__()
