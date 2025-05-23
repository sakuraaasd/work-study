#group definition
resource "aws_iam_group" "administrators" {
    name = "administrators"
}

resource "aws_iam_policy_attachment" "administrators_attach" {
    name = "administrators_attach"
    groups = [aws_iam_group.administrators.name]
    policy_arn = "arn:aws:iam:aws:policy/AdministratorAccess"
}

#user
resource "aws_iam_user" "admin1" {
    name = "admin1"
}

resource "aws_iam_user" "admin2" {
    name = "admin2"
}

resource "aws_iam_group_membership" "administrators_users" {
    name = "administrators-users"
    users = [ 
        aws_iam_user.admin1.name,
        aws_iam_user.admin2.name
    ]
    group = aws_iam_group.administrators.name
}