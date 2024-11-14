resource "aws_db_subnet_group" "mariadb_subnet_2413618" {
    name = "mariadb_subnet"
    description = "RDS subnet group"
    subnet_ids = [ aws_subnet.main_pri_1_2413618.id,aws_subnet.main_pri_2_2413618 ]  
}

resource "aws_db_parameter_group" "mariadb_parameters_2413618" {
    name = "mariadb-parameters"
    family = "mariadb10.1"
    description = "Mariadb parameter group"

    parameter {
      name = "max_allowed_packet"
      value = "16777216"
    }
}

resource "aws_db_instance" "mariadb" {
    allocated_storage = 100
    engine = "mariadb"
    engine_version = "10.1.14"
    instance_class = "db.t2.small"
    identifier = "mariadb"
    username = "root"
    password = var.RDS_PASSWORD
    db_subnet_group_name = aws_db_subnet_group.mariadb_subnet_2413618.name
    parameter_group_name = aws_db_parameter_group.mariadb_parameters_2413618.name
    multi_az = "false"
    vpc_security_group_ids = [ aws_security_group.allow_ssh_2413618 ]
    storage_type = "gp2"
    backup_retention_period = 30
    availability_zone = aws_subnet.main_pri_1_2413618.availability_zone
    skip_final_snapshot = true
    tags = {
        name = "mariadb-instance"
    }
}
