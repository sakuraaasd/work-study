resource "aws_instance" "example_2413618" {
    ami = "ami-04ef3193cda2ac9d4"
    instance_type = "t2.micro"

    subnet_id = aws_subnet.main_pub_1_2413618.id

    vpc_security_group_ids = [ aws_security_group.allow_ssh_2413618.id ]

    key_name = aws_key_pair.mykeypair_2413618.key_name
}
