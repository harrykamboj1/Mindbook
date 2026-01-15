import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("SUPABASE_API_URL") or not os.getenv("SUPABASE_SECRET_KEY"):
    raise ValueError(
        "SUPABASE_API_URL and SUPABASE_SECRET_KEY must be set in .env file"
    )

if not os.getenv("CLERK_SECRET_KEY") or not os.getenv("DOMAIN"):
    raise ValueError("CLERK_SECRET_KEY and DOMAIN must be set in .env file")


# if (
#     not os.getenv("S3_BUCKET_NAME")
#     or not os.getenv("AWS_REGION")
#     or not os.getenv("AWS_SECRET_ACCESS_KEY")
#     or not os.getenv("AWS_ACCESS_KEY_ID")
# ):
#     raise ValueError(
#         "S3_BUCKET_NAME, AWS_REGION, AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY must be set in .env file"
#     )

if (
    not os.getenv("R2_ACCESS_KEY")
    or not os.getenv("R2_SECRET_KEY")
    or not os.getenv("R2_BUCKET")
    or not os.getenv("R2_ACCOUNT_ID")
):
    raise ValueError(
        "R2_ACCESS_KEY, R2_SECRET_KEY, R2_BUCKET, and R2_ACCOUNT_ID must be set in .env file"
    )

if not os.getenv("REDIS_URL"):
    raise ValueError("REDIS_URL must be set in .env file")

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY must be set in .env file")

if not os.getenv("SCRAPING_DO_API_KEY"):
    raise ValueError("SCRAPING_DO_API_KEY must be set in .env file")

if not os.getenv("TAVILY_API_KEY"):
    raise ValueError("TAVILY_API_KEY must be set in .env file")


appConfig = {
    "supabase_api_url": os.getenv("SUPABASE_API_URL"),
    "supabase_secret_key": os.getenv("SUPABASE_SECRET_KEY"),
    "clerk_secret_key": os.getenv("CLERK_SECRET_KEY"),
    "domain": os.getenv("DOMAIN"),
    "r2_access_key": os.getenv("R2_ACCESS_KEY"),
    "r2_secret_key": os.getenv("R2_SECRET_KEY"),
    "r2_bucket": os.getenv("R2_BUCKET"),
    "r2_account_id": os.getenv("R2_ACCOUNT_ID"),
    "redis_url": os.getenv("REDIS_URL"),
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "scraping_do_api_key": os.getenv("SCRAPING_DO_API_KEY"),
    "tavily_api_key": os.getenv("TAVILY_API_KEY"),
}
