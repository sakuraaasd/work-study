resource "aws_key_pair" "mykeypair_2413618" {
    key_name = "mykeypair"
    public_key = file(var.PATH_TO_PUBLIC_KEY)
  
}