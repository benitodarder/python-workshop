variable "sample_string_map" {
  type        = map(string)
  description = "Information"
  default     = {
    key01      = 123456789101112
    key02      = 1314
    key03      = "Value 03"
    key04      = "Value 04"
  }
}
