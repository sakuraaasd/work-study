terraform {
  required_version = ">=0.12"
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.80.0"
    }
  }
}
provider "aws" {
    access_key = var.ACCESS_KEY
    secret_key = var.SECRET_KEY
    region = var.AWS_REGION
}