import json


def load_json(file_path: str):

    """
    This method returns json-file data in python dict format.
    * It requires file path.
    :param file_path: str
    :return: dict
    """

    return json.load(
        open(file_path, "r")
    )
