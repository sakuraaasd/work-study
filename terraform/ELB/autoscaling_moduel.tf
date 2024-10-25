#定义auto scaling内的ec2的设置模板
resource "aws_launch_configuration" "launchconfig_2413618" {
    name_prefix = "launchconfig_2413618"
    image_id = var.AMIS
    instance_type = "t2.micro"
    key_name = aws_key_pair.mykeypair_2413618.key_name
    security_groups = [ aws_security_group.allow_ssh_2413618 ]
    #user_data = "在实例启动以后执行脚本内容"
}

#定义auto scaling的模板内容
resource "aws_autoscaling_group" "autoscaling_2413618" {
    name = "autoscaling_2413618"
    vpc_zone_identifier = [ aws_subnet.main_pub_1_2413618.id,aws_subnet.main_pub_2_2413618]
    launch_configuration = aws_launch_configuration.launchconfig_2413618.name
    min_size = 1
    max_size = 2
    health_check_grace_period = 300
    health_check_type = "ELB"
    load_balancers = [ aws_elb.my_elb_2413618.name ]
    force_delete = true

    tag {
      key = "Name"
      value = "ec2 instance"
      propagate_at_launch = true
    }
  
}