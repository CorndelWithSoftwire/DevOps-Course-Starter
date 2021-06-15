variable "prefix" {
  description = "The prefix used for all resources in this environment"
}
variable "location" {
  description = "The Azure location where all resources in this deployment should be created"
}
variable "client_id" {
  description = "The client ID"
  default = "7b45e6f82314a24eae60"
}