resource "aws_iam_role" "s3-mybucket-role" { #"s3-mybucket-role" 是资源的名称，在 Terraform 状态文件中唯一标识该资源。
  #定义角色名
  name = "s3-mybucket-role"
  #创建信任关系政策：定义哪些 AWS 服务或账户可以扮演该角色。(定义角色)
  assume_role_policy = <<EOF
{
  "version":"2012-10-17",
  "statement":[
    {
    "Action":"sts:AssumeRole",
    "Principal":{
      "Severvice":"ec2.amazonaws.com"
      },
      "Effect":"Allow",
      "Sid":""
    }
  ]
}
EOF

}
#为这个角色（"s3-mybucket-role"）添加权限
resource "aws_iam_role_policy" "s3-mybucket-role-policy" {
    name = "s3-mybucket-role-policy"
    role = aws_iam_role.s3-mybucket-role.id
    policy = <<EOF
{
    "Version":"2012-10-17",
    "Statement":[
        {
            "Effect":"Allow",
            "Action":[
              "S3:*"
            ],
              "Resource":[
                "arn:aws:s3:::my-bucket-sakuraaasd363",
                "arn:aws:s3:::my-bucket-sakuraaasd363/*"
            ]
        }
    ]
}

EOF
}

#定义和赋予权限以后 使用这个roles。 (aws_iam_instance_profile) 是一个容器，用于将 IAM 角色传递给 EC2 实例
resource "aws_iam_instance_profile" "s3-mybucket-role-instanceprofile" {
    name = "s3-mybucket-role"
    role = aws_iam_role.s3-mybucket-role.name
}

#commend：aws s3 cp xxx.txt s3://my-bucket-sakuraaasd363/xxx.txt
#将内容上传至s3存储桶