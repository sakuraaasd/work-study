resource "aws_security_group" "allow_ssh_2413618" {
    vpc_id = aws_vpc.main_2413618.id
    name = "allow_ssh_2413618"
    description = "security group that allow ssh and all egress traffic"
    egress { 
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
      ipv6_cidr_blocks = []  # 必须字段
      prefix_list_ids = []   # 必须字段
      description = "Allow all outbound traffic"
    }

    ingress { 
      from_port = 22
      to_port = 22
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      ipv6_cidr_blocks = []  # 必须字段
      description = "Allow SSH access from anywhere"
    }

    tags = {
      name = "allow_ssh"
    }
}

