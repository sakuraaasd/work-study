resource "aws_s3_bucket" "b" {
    bucket = "my-bucket-sakuraaasd363"
    acl = "private"

    tags = {
      Name = "my-bucket-sakuraaasd363"
    }
}