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
  default = "$variables_client_id"
}
variable "client_secret"  {
  description = "The client secret"
  default = "$variables_client_secret"
}
variable "variables_client_secret" {
  description = "Variables client secret"
  default = "be07d5d4c655bf1d6765b061d3f32358aa560042"
}
variable "variables_client_id" {
  description = "Client ID"
  default = "7b45e6f82314a24eae60"
}