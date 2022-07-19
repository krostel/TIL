resource "aws_s3_bucket" "source_bucket" {
  bucket        = var.source_bucket_name
  force_destroy = true
}

resource "aws_s3_bucket" "destination_bucket" {
  bucket        = var.destination_bucket_name
  force_destroy = true
}

resource "aws_s3_bucket_notification" "bucket_terraform_notification" {
  bucket = aws_s3_bucket.source_bucket.id
  lambda_function {
    lambda_function_arn = aws_lambda_function.s3_copy_function.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_terraform_bucket]
}

data "archive_file" "my_lambda_function" {
  source_dir  = "${path.module}/lambda_handler/"
  output_path = "${path.module}/lambda.zip"
  type        = "zip"
}

data "aws_iam_policy_document" "lambda_policy" {
  version = "2012-10-17"

  statement {
    effect = "Allow"
    actions = [
      "s3:ListBucket",
      "s3:GetObject",
      "s3:CopyObject",
      "s3:HeadObject"
    ]
    resources = [
      aws_s3_bucket.source_bucket.arn,
      "${aws_s3_bucket.source_bucket.arn}/*"
    ]
  }

  statement {
    effect = "Allow"
    actions = [
      "s3:ListBucket",
      "s3:PutObject",
      "s3:PutObjectAcl",
      "s3:CopyObject",
      "s3:HeadObject"
    ]
    resources = [
      aws_s3_bucket.destination_bucket.arn,
      "${aws_s3_bucket.destination_bucket.arn}/*"
    ]
  }

  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "lambda_policy" {
  name = "s3-source-to-destination"

  policy = data.aws_iam_policy_document.lambda_policy.json
}

resource "aws_iam_role" "s3_copy_function" {
  name               = "copy_lambda_zip"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "terraform_lambda_iam_policy_basic_execution" {
  role       = aws_iam_role.s3_copy_function.id
  policy_arn = aws_iam_policy.lambda_policy.arn
}

resource "aws_lambda_permission" "allow_terraform_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.s3_copy_function.arn
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.source_bucket.arn
}

resource "aws_lambda_function" "s3_copy_function" {
  filename         = "lambda.zip"
  source_code_hash = data.archive_file.my_lambda_function.output_base64sha256
  function_name    = "copy_lambda_zip"
  role             = aws_iam_role.s3_copy_function.arn
  handler          = "index.handler"
  runtime          = "python3.6"

  environment {
    variables = {
      DST_BUCKET = aws_s3_bucket.destination_bucket.id,
      REGION     = "us-east-1"
    }
  }
}

