provider "aws" {
  region     = "us-west-2"
  access_key = ""
  secret_key = ""
}

resource "aws_instance" "web" {
  ami                    = "ami-075686beab831bb7f"
  instance_type          = "t2.small"
  key_name               = "django"
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y docker nginx
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo systemctl start nginx
              sudo systemctl enable nginx
              EOF

  tags = {
    Name = "django"
  }
}

resource "aws_security_group" "web_sg" {
  name        = "django_sg"
  description = "Allow SSH, HTTP, and HTTPS"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
