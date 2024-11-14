provider "aws" {
    access_key = var.AEECSS_KEY
    secret_key = var.SECRET_KEY
    region = var.REGION
  
}

terraform {
  required_version = ">=0.12"
}