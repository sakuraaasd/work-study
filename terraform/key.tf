#EC2密钥对 (aws_key_pair)
#当你创建一个EC2实例并指定一个密钥对时，AWS会使用这个密钥对的公钥来加密实例的登录信息（如SSH密钥）。
#用户需要相应的私钥才能解密这些信息并通过SSH安全登录到实例。
#在EC2中，公钥一般会上传到AWS，通过AWS管理并于自己的账号关联
resource "aws_key_pair" "mykeypair_2413618" {
    key_name = "mykeypair"
    public_key = file(var.PATH_TO_PUBLIC_KEY)
  
}