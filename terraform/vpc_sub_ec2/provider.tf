provider "aws" {
    access_key = var.ACCESS_KEY
    secret_key = var.SECRET_KEY
    region = var.AWS_REGION
}

terraform {
  required_version = ">=0.12"
}