resource "aws_instance" "example_2413618" {
    ami = "ami-04ef3193cda2ac9d4"
    instance_type = "t2.micro"
    #the VPC subnet
    subnet_id = aws_subnet.main_pub_1_2413618.id
    #the security group
    vpc_security_group_ids = [ aws_security_group.allow_ssh_2413618.id ]
    #the pub SSH key
    key_name = aws_key_pair.mykeypair_2413618.key_name
    #将roles绑定到ec2上
    iam_instance_profile = aws_iam_instance_profile.s3-mybucket-role-instanceprofile.name
    #user data
    #user_data = data.template_cloudinit_config.cloudinit-example.rendered
}

resource "aws_ebs_volume" "ebs_volume_1_2413618" {
    availability_zone = "ap-northeast-3a"
    size = 20
    type = "gp2"
    tags = {
      Name = "extra a volume"
    }
}

resource "aws_volume_attachment" "ebs_volume_1_attachment_2413618" {
    device_name = "/dev/xvdh"
    volume_id = aws_ebs_volume.ebs_volume_1_2413618.id
    instance_id = aws_instance.example_2413618.id
}

