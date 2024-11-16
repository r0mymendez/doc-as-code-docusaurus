# main.tf

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "s3_docusaurus" {
  bucket = "doc-as-code-docusaurus"

  tags = {
    Name        = "s3-doc-as-code-docusaurus"
    Environment = "documentation"
    Tool        = "docusaurus"
  }
}
