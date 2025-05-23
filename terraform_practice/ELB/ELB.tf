resource "aws_elb" "my_elb_2413618" {
    name = "my_elb_2413618"
    subnets = [ aws_subnet.main_pub_1_2413618.id,aws_subnet.main_pub_2_2413618.id ]
    listener {
      instance_port = 80
      instance_protocol = "http"
      lb_port = 80
      lb_protocol = "http"
    }
    health_check {
      healthy_threshold = 2
      unhealthy_threshold = 2
      timeout = 3
      target = "HTTP:80/"
      interval = 30
    }

    cross_zone_load_balancing = true
    connection_draining = true
    connection_draining_timeout = 400
    
    tags = {
      Name = "my_elb"
    }
  
}