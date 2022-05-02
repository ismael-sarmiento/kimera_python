import os

KIMERA_PROJECT = "kimera_core"
TEST_FOLDER = "test"
RESOURCES = "resources"


def resources_path():
    resources = os.path.join(os.getcwd().split(KIMERA_PROJECT)[0], KIMERA_PROJECT, TEST_FOLDER, RESOURCES)
    return resources


def get_resource_file(filename: str):
    resource_file = os.path.join(resources_path(), filename)
    return resource_file
