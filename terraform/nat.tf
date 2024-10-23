# 创建一个弹性 IP（EIP），用于 NAT 网关
resource "aws_eip" "nat_2413618" {
  vpc = true
}

# 创建 NAT 网关，分配到公共子网
resource "aws_nat_gateway" "nat_gw_2413618" {
  allocation_id = aws_eip.nat_2413618.id
  subnet_id     = aws_subnet.main_pub_1_2413618.id
  depends_on    = [aws_internet_gateway.main_gw_2413618]
}

# # 为 3 号子网创建路由表，路由通过 NAT 网关
# resource "aws_route_table" "main_private_3_2413618" {
#   vpc_id = aws_vpc.main_2413618.id
# }

# # 为 3 号子网添加路由，通过 NAT 网关访问互联网
# resource "aws_route" "default_route_1" {
#   route_table_id         = aws_route_table.main_private_3_2413618.id
#   destination_cidr_block = "0.0.0.0/0"
#   nat_gateway_id         = aws_nat_gateway.nat_gw_2413618.id
# }



# # 为 2 号子网创建路由表，不关联互联网网关（仅VPC内路由）
# resource "aws_route_table" "main_private_2_2413618" {
#   vpc_id = aws_vpc.main_2413618.id
# }

# # 将 2 号子网与路由表关联
# resource "aws_route_table_association" "main_private_2_a_2413618" {
#   subnet_id      = aws_subnet.main_pri_2_2413618.id
#   route_table_id = aws_route_table.main_private_2_2413618.id
# }


#VPC set up for NAT
resource "aws_route_table" "main_private_1_2413618" {
    vpc_id = aws_vpc.main_2413618.id
    route {
      cidr_block     = "0.0.0.0/0"
      nat_gateway_id = aws_nat_gateway.nat_gw_2413618.id
    }
    
    tags = {
      Name = "main-private-1"
}
    
}

resource "aws_route_table" "main_private_2_2413618" {
    vpc_id = aws_vpc.main_2413618.id
  
}

#route association private
resource "aws_route_table_association" "main_private_1_a_2413618" {
    subnet_id      = aws_subnet.main_pri_1_2413618.id
    route_table_id = aws_route_table.main_private_1_2413618.id
}

resource "aws_route_table_association" "main_private_2_a_2413618" {
    subnet_id      = aws_subnet.main_pri_2_2413618.id
    route_table_id = aws_route_table.main_private_2_2413618.id
}


