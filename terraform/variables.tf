variable "aws_region" {
  description = "AWS region for infrastructure"
  type        = string
  default     = "eu-west-2"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "instance_name" {
  description = "EC2 instance Name tag"
  type        = string
  default     = "terraform-app-server"
}

variable "key_name" {
  description = "Existing AWS EC2 key pair name"
  type        = string
}
