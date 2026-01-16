import boto3
from botocore.client import Config
from src.config import appConfig

r2 = boto3.client(
    "s3",
    endpoint_url=f"https://{appConfig["r2_account_id"]}.r2.cloudflarestorage.com",
    aws_access_key_id=appConfig["r2_access_key"],
    aws_secret_access_key=appConfig["r2_secret_key"],
    config=Config(signature_version="s3v4"),
    region_name="auto",
)

s3_client = r2

def upload_file_to_r2(file_obj, filename: str, content_type: str):
    s3_client.upload_fileobj(
        file_obj,
        appConfig["r2_bucket"],
        filename,
        ExtraArgs={"ContentType": content_type},
    )
    return f"https://{appConfig["r2_account_id"]}.r2.cloudflarestorage.com/{appConfig["r2_bucket"]}/{filename}"