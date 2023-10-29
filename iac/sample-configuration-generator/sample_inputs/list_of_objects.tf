variable "list_of_objects" {
  type = list(object({
      inner_list = list(string)
      a_number = optional(number, 666)
    })
)
}
