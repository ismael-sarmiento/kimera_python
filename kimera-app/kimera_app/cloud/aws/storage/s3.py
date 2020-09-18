import os
from pathlib import Path

from kimera_cloud.components.aws.services.storage.s3 import S3Service

if __name__ == '__main__':
    # -------------------------------------------------------------------
    # ------------------------- EXAMPLES --------------------------------
    # -------------------------------------------------------------------

    os.environ['AWS_PROFILE'] = 'bender-administrator'

    source_path = Path('.')
    file_path = source_path / 'resources' / 'file.txt'

    # Upload File To S3
    S3Service().upload_file(str(file_path), "bender-private", file_path.name)

    # Download File From S3
    S3Service().download_file(str(file_path), "bender-private", file_path.name)

    # Delete Remote Object From S3
