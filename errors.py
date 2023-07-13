"""
This module contains all the error responses to be sent
"""

errors = {
    "SUCCESS" : {"respcode": 200, "respdesc" : "Success"},
    "EMPTY_REQUEST_BODY" : {"respcode": 400, "respdesc" : "Bad request"},
    "INVALID_PAN_NUMBER" : {"respcode": 401, "respdesc" : "Invalid pan number"},
    "INTERNAL_ERROR" : {"respcode": 402, "respdesc" : "Internal error occurred"},
    "INVALID_DETAILS" : {"respcode": 403, "respdesc" : "Invaild details"},
    "FIELD_NOT_FOUND" : {"respcode": 404, "respdesc" : "Parameters not found"},
    "SESSION_ACTIVE": {"respcode": 405, "respdesc" : "Session already active"},
    "INTERNAL_API_ERROR": {"respcode": 406,"respdesc":"Unable to fetch internal api"},
    "CONNECTION_ERROR":{"respcode":407,"respdesc":"Connection aborted"},
    "DETAILS_NOT_PRESENT":{"respcode":408,"respdesc":"details not present"},
    "EMPTY_ACKNUM" : {"respcode": 409, "respdesc" : "not yet filed income tax return"}
    
}