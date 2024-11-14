#VPC
resource "aws_vpc" "main_2413618" {
    cidr_block         = "10.0.0.0/16"
    instance_tenancy   = "default"
    enable_dns_support = "true"
    enable_dns_hostnames = "true"
    tags = {
      Name = "main_vpc"
    }
}
#Subnet
resource "aws_subnet" "main_pub_1_2413618" {
    vpc_id = aws_vpc.main_2413618.id
    cidr_block = "10.0.1.0/24"
    map_public_ip_on_launch = "true"
    availability_zone = "ap-northeast-3a"

    tags = {
      Name = "main-pub-1"
    }
  
}
resource "aws_subnet" "main_pub_2_2413618" {
    vpc_id = aws_vpc.main_2413618.id
    cidr_block = "10.0.2.0/24"
    map_public_ip_on_launch = "true"
    availability_zone = "ap-northeast-3b"

    tags = {
      Name = "main-pub-2"
    }
  
}
resource "aws_subnet" "main_pri_1_2413618" {
    vpc_id = aws_vpc.main_2413618.id
    cidr_block = "10.0.4.0/24"
    map_public_ip_on_launch = "true"
    availability_zone = "ap-northeast-3a"

    tags = {
      Name = "main-pri-1"
    }
  
}
resource "aws_subnet" "main_pri_2_2413618" {
    vpc_id = aws_vpc.main_2413618.id
    cidr_block = "10.0.5.0/24"
    map_public_ip_on_launch = "true"
    availability_zone = "ap-northeast-3b"

    tags = {
      Name = "main-pri-2"
    }
  
}

#internet GW
resource "aws_internet_gateway" "main_gw_2413618" {
    vpc_id = aws_vpc.main_2413618.id

    tags = {
      Name = "main_gw"
    }
  
}

#route tables
resource "aws_route_table" "main_public_2413618" {
    vpc_id = aws_vpc.main_2413618.id

    tags = {
      Name = "main_public_1"
    }
  
}
#route associations public
resource "aws_route_table_association" "main_pub_1_a" {
    subnet_id = aws_subnet.main_pub_1_2413618.id
    route_table_id = aws_route_table.main_public_2413618.id
  
}

resource "aws_route_table_association" "main_pri_1_a" {
    subnet_id = aws_subnet.main_pri_1_2413618.id
    route_table_id = aws_route_table.main_public_2413618.id
  
}

#在resource进行设定的时候，就已经自动创建了很多类似vpc的id（属性类的内容
#缩进内容中编写的其实就是他们的つながり，写一些相关性的东西，描述各个服务之间如何进行连接