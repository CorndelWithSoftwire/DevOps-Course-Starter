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
  default = "7b45e6f82314a24eae60"
}
variable "client_secret"  {
  description = "The client secret"
  default = "be07d5d4c655bf1d6765b061d3f32358aa560042"
}