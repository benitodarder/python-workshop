variable "object_with_objects_and_lists" {
  type = object({
    a_string = str
    inner_object = object({
      inner_inner_list = list(string)
      a_number = optional(number, 666)
    })
  })
}
