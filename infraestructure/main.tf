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

# S3 Bucket configuration
resource "aws_s3_bucket" "s3_docusaurus" {
  bucket = "doc-as-code-docusaurus"

  tags = {
    Name        = "s3-doc-as-code-docusaurus"
    Environment = "documentation"
    Tool        = "Docusaurus"
  }

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

# Configuration of static web site in s3 bucket 
resource "aws_s3_bucket_website_configuration" "s3_docusaurus_website" {
  bucket = aws_s3_bucket.s3_docusaurus.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}

# Disable public policy blocking on the bucket
resource "aws_s3_bucket_public_access_block" "s3_docusaurus_public_access" {
  bucket = aws_s3_bucket.s3_docusaurus.id

  block_public_acls       = false  
  block_public_policy     = false  
  ignore_public_acls      = false
  restrict_public_buckets = false
}

# Policy to allow read-only public access
resource "aws_s3_bucket_policy" "s3_docusaurus_policy" {
  bucket = aws_s3_bucket.s3_docusaurus.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.s3_docusaurus.arn}/*"
      }
    ]
  })
}
