import sys
from generate_captcha import get_login
from loggers import get_logger
from utils import response_data, login
from errors import errors
from verify import verify_captcha
from get_details import get_details

logger = get_logger("voter_validation")


def voter_validation_api(request):

    try:
        login_req_parms = login(request)
        if login_req_parms == False:
            return response_data(errors["INVALID_REQUEST"])

        return get_login(request)
    except Exception :
        logger.error("Global Error : %s", sys.exc_info())
        return response_data(errors["EMPTY_REQUEST_BODY"])
def captcha_verify(request):
    try:
        captcha_verify_parms = login(request)
        if captcha_verify_parms == False:
            return response_data(errors["INVALID_REQUEST"])

        return verify_captcha(request)
    except Exception :
        logger.error("Global Error : %s", sys.exc_info())
        return response_data(errors["EMPTY_REQUEST_BODY"])
def gat_details_api(request):
    try:
        gat_details_parms = login(request)
        if gat_details_parms == False:
            return response_data(errors["INVALID_REQUEST"])

        return get_details(request)
    except Exception :
        logger.error("Global Error : %s", sys.exc_info())
        return response_data(errors["EMPTY_REQUEST_BODY"])