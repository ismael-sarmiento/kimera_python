import os

KIMERA_DB = "kimera_db"
TEST_FOLDER = "test"
RESOURCES = "resources"


def resources_path():
    resources = os.path.join(os.getcwd().split(KIMERA_DB)[0], KIMERA_DB, TEST_FOLDER, RESOURCES)
    return resources


def get_resource_file(filename: str):
    resource_file = os.path.join(resources_path(), filename)
    return resource_file
