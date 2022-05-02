import unittest
from unittest.mock import patch

from kimera_cloud.components.aws.services.storage.s3 import S3Service


class TestAWStorageS3(unittest.TestCase):

    def setUp(self) -> None:
        self.s3_service = S3Service()
        self.object = "OBJECT_MOCK"
        self.bucket = "BUCKET_MOCK"
        self.key = "KEY_MOCK"

    def tearDown(self) -> None:
        print(self.shortDescription())

    @patch('boto3.s3.transfer.S3Transfer.upload_file')
    def test_given_parameters_input_when_call_upload_file_mock_then_this_mock_method_has_called_once(self, upload_file_mock):
        self._testMethodDoc = "I - test_given_parameters_input_when_call_upload_file_mock_then_this_mock_method_has_called_once"

        self.s3_service.upload_file(self.object, self.bucket, self.key)

        self.assertTrue(upload_file_mock.called)
        upload_file_mock.assert_called_once()

    @patch('boto3.s3.transfer.S3Transfer.download_file')
    def test_given_parameters_input_when_call_download_file_mock_then_this_mock_method_has_called_once(self, download_file_mock):
        self._testMethodDoc = "II - test_given_parameters_input_when_call_download_file_mock_then_this_mock_method_has_called_once"

        self.s3_service.download_file(self.object, self.bucket, self.key)

        self.assertTrue(download_file_mock.called)
        download_file_mock.assert_called_once()
