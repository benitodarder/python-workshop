variable "oneString" {
  type = string
}

variable "complexOne" {
  type = object({
    aString = string
    aNumber = number
  })
}
