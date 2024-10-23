provider "aws" {
    access_key = var.ACCESS_KEY
    secret_key = var.SECRET_KEY
    region = "ap-northeast-1"
}

terraform {
  required_version = ">=0.12"
}