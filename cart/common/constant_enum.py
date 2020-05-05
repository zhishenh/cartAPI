from enum import Enum, unique


@unique
class Message(Enum):
    GET_SUCCESS = "Get cart items Successfully"
    UPDATE_SUCCESS = "Update Item Successfully"
    UPDATE_ERROR = "Fail to update item"
    PARAMS_ERROR = "Parameters Error"
    DELETE_SUCCESS = "Delete item Successfully"
    DELETE_ERROR = "Fail to delete item . No item"


@unique
class StatusCode(Enum):
    SUCCESS = 1
    FAIL = 2

