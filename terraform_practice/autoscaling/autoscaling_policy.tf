#定义了一个 Auto Scaling 策略，用于在满足某些条件时，自动增加实例的数量
resource "aws_autoscaling_policy" "cpu_policy_up_2413618" {
    name = "cpu_policy_2413618"
    autoscaling_group_name = aws_autoscaling_group.autoscaling_2413618.name
    adjustment_type = "ChangeInCapacity"
    scaling_adjustment = "1"
    cooldown = "300"
    policy_type = "SimpleScaling"
}
#定义CloudWatch来监控上面↑提到的某些条件，当超过设定的阈值时触发 Auto Scaling 策略
resource "aws_cloudwatch_metric_alarm" "cpu_alarm_up_2413618" {
    alarm_name = "cpu_alarm_up_2413618"
    alarm_description = "cpu_alarm_up_2413618"
    comparison_operator = "GreaterThanOrEqualToThreshold"
    evaluation_periods = "2"
    metric_name = "CPUUtilization"
    namespace = "AWS/EC2"
    period = "120"
    statistic = "Average"
    threshold = "30"

    dimensions = { #这里指定了监控的具体资源
      "AutoScalingGroupName" = aws_autoscaling_group.autoscaling_2413618.name
    }

    actions_enabled = true
    alarm_actions = [aws_autoscaling_policy.cpu_policy_up_2413618.arn]  
}

#定义了一个 Auto Scaling 策略，用于在满足某些条件时，自动减少实例的数量
resource "aws_autoscaling_policy" "cpu_policy_down_2413618" {
    name = "cpu_policy_down_2413618"
    autoscaling_group_name = aws_autoscaling_group.autoscaling_2413618.name
    adjustment_type = "ChangeInCapacity"
    scaling_adjustment = "-1"
    cooldown = "300"
    policy_type = "SimpleScaling"
}

#定义CloudWatch来监控上面↑提到的某些条件，当超过设定的阈值时触发 Auto Scaling 策略
resource "aws_cloudwatch_metric_alarm" "cpu_alarm_down_2413618" {
    alarm_name = "cpu_alarm_down_2413618"
    alarm_description = "cpu_alarm_down_413618"
    comparison_operator = "LessThanOrEqualToThreshold"
    evaluation_periods = "2"
    metric_name = "CPUUtilization"
    namespace = "AWS/EC2"
    period = "120"
    statistic = "Average"
    threshold = "5"

    dimensions = { #这里指定了监控的具体资源
      "AutoScalingGroupName" = aws_autoscaling_group.autoscaling_2413618.name
    }

    actions_enabled = true
    alarm_actions = [aws_autoscaling_policy.cpu_policy_down_2413618.arn]  
}