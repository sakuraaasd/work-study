provider "aws" {
    access_key = "AKIA5ID6QB3IBENTJBK2"
    secret_key = "P/XMIuh3jFbm1bwM0hWYuhaKAf6esutQ3K1DDGec"
    region = "ap-northeast-1"
  
}
resource "aws_instance" "example" {
    ami = ""
    instance_type = "t2.micro"
  
}