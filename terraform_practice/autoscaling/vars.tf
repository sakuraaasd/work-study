#variable（函数名自己设置）
###############################################################
#AWS访问密钥(在AWS IAM控制台中生成)
#用于编程方式访问AWS服务，如通过AWS CLI、SDK或API。
#这些密钥对用于身份验证和授权，以允许用户执行API调用。
variable "ACCESS_KEY" {
    default = "AKIA5ID6QB3IBENTJBK2"

}
variable "SECRET_KEY" {
    default = "P/XMIuh3jFbm1bwM0hWYuhaKAf6esutQ3K1DDGec"
}
###############################################################
variable "PATH_TO_PUBLIC_KEY" {
    default = "my_key_pair.pub"
    type = string
  
}
variable "PATH_TO_PRIVATE_KEY" {
    default = "my_key_pair"
  
}
variable "AWS_REGION" {
    default = "ap-northeast-3"
}
variable "RDS_PASSWORD" {
    default = "asd_2051312"
}
variable "AMIS" {
    default = "ami-04ef3193cda2ac9d4"
}