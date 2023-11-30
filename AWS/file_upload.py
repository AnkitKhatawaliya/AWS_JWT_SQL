from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
import boto3
import tempfile
import os

app = FastAPI()


def upload_to_aws(bucket_name: str, image_name: str, file_path: str):
    s3 = boto3.client(
        's3',
        region_name='ap-south-1',
        aws_access_key_id='Insert by creating an iam user',
        aws_secret_access_key='Insert by creating an iam user'
    )
    try:
        s3.upload_file(file_path, bucket_name, image_name)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post('/image/')
async def upload_image(image: UploadFile = File(...), name: str = ""):
    file_path = f"{name}"
    try:
        with open(file_path, "wb") as f:
            f.write(image.file.read())
        upload_to_aws("test-first1", name, file_path)
        os.remove(file_path)
        return {"Uploaded to AWS": "Success"}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


def download_from_aws(bucket_name: str, image_name: str, local_file_path: str):
    s3 = boto3.client(
        's3',
        region_name='ap-south-1',
        aws_access_key_id='Insert by creating an iam user',
        aws_secret_access_key='Insert by creating an iam user'
    )
    try:
        with open(local_file_path, 'wb') as f:
            s3.download_fileobj(bucket_name, image_name, f)
    except Exception as e:
        raise e


@app.get('/image/{name}')
async def send_image(name: str):
    try:
        # Download the image from AWS S3 to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        download_from_aws("test-first1", name, temp_file.name)

        # Return the image as a FastAPI FileResponse
        return FileResponse(temp_file.name, media_type='image/jpeg')
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post('/image/{name}')
async def UploadFile(name: str, image: UploadFile = File(...)):
    print(name)
    print(image.filename)
    return {"Working"}
