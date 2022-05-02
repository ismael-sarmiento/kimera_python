"""
AWS - Storage - S3
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
"""
from kimera_cloud.components.aws.tools.session import get_client, get_resource
from kimera_core.components.tools.utils.generic import ExceptionsUtils


class S3Service:

    def __init__(self, *args, **kwargs):
        ExceptionsUtils.raise_exception_if_module_not_exists('boto3')
        self.s3client = get_client(service_name='s3', *args, **kwargs)
        self.s3resource = get_resource(service_name='s3', *args, **kwargs)

    def upload_file(self, filename: str, bucket: str, key: str, **kwargs):
        """
            Upload a file to an S3 object.

        :param filename: The path to the file to upload.
        :param bucket:  The name of the bucket to upload to.
        :param key: The name of the key to upload to.
        :param kwargs:
                ExtraArgs (dict): Extra arguments that may be passed to the client operation.
                Callback (function): A method which takes a number of bytes transferred to be periodically called during the upload.
                Config (boto3.s3.transfer.TransferConfig): The transfer configuration to be used when performing the transfer.
        :return: None
        """
        self.s3client.upload_file(filename, bucket, key, **kwargs)

    def download_file(self, filename: str, bucket: str, key: str, **kwargs):
        """

            Download an S3 object to a file.

        :param filename: The path to the file to download to.
        :param bucket:  The name of the bucket to download from.
        :param key: The name of the key to download from.
        :param kwargs:
                ExtraArgs (dict): Extra arguments that may be passed to the client operation.
                Callback (function): A method which takes a number of bytes transferred to be periodically called during the upload.
                Config (boto3.s3.transfer.TransferConfig): The transfer configuration to be used when performing the transfer.
        :return: None
        """
        self.s3client.download_file(bucket, key, filename, **kwargs)
