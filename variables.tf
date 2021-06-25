variable "prefix" {
  description = "The prefix used for all resources in this environment"
  default = ""  
}
variable "location" {
  description = "The Azure location where all resources in this deployment should be created"
  default = "uk south"   
}
variable "client_id" {
  description = "The client ID"
}
variable "client_secret"  {
  description = "The client secret"
}
