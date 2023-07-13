import requests
import json
import os
from loggers import get_logger
from dotenv import load_dotenv
from errors import errors
from utils import login, response_data, headerfile_details, proxy_ids, get_cookie
import sys
import re
load_dotenv()
logger = get_logger("VOTER")

url = os.getenv("get_details")
origin = os.getenv("origin")
referer = os.getenv("referer")

def get_details(request):
    try:
        req = eval(request.data)  # the data we send in postman

        try:
            if "epic" in req and "txnid" in req and "captcha" in req and "cookies"in req and "id" in req:
                epic = req["epic"]
                epic = epic.upper()
                txnid = req["txnid"]
                captcha = req["captcha"]
                # captcha = captcha
                cookies = req["cookies"]
                # cookies= cookies.upper()
                id = req["id"]
                # id = id.upper()
            else:
                logger.error("...field not found(check for epic and txnid)...")
                return response_data(errors["FIELD_NOT_FOUND"])

        except Exception:
            logger.error("%s  epic field not found %s",txnid,epic)
            return response_data(errors["FIELD_NOT_FOUND"])

        try:
            proxies = proxy_ids()

            print("proxy ip address", type(proxies))

            # validations for epic
            if str(req["epic"]) == "":
                logger.error("%s enter voter number... %s", txnid, epic)
                return response_data(errors["INVALID_VOTER_NUMBER"])

            v = "^[a-zA-Z]{3}[0-9]{7}$"
            if re.match(v, epic):
                logger.error(" %s is a valid voter number", epic)
            else:
                logger.error("%s voter regex dosen't match: %s", txnid, epic)
                return response_data(errors["INVALID_VOTER_NUMBER"])

            payload = json.dumps({"epic": epic, "serviceName": "loginService"})
            try:
                cookie = get_cookie()
                logger.info("%s -cookie generated: %s", txnid, cookie)
                headers = headerfile_details(cookie, origin, referer)

                try:
                    response = requests.request(
                        "GET", url, headers=headers, data=payload
                    )
                    res = response.json()
                    logger.info(
                        "%s -First api request sent successfully: %s", txnid, res
                    )

                    data = dict({"id": ""}) 

                    try:
                        # captcha = res["captcha"]
                        Id = res["id"]
                        data["id"] = Id
                        data.update({"cookies": cookie})
                        # data.update({"captcha" : captcha})
                        data.update({"txnid": txnid})
                        logger.info("%s success transaction of first api:", txnid)
                        return response_data(errors["SUCCESS"], data)
                    except Exception:
                        
                        error_type = res["messages"][0]["desc"]
                        print("exceed", error_type)

                        if error_type == "Exceeded limit" or len(error_type) > 50:
                            logger.error(
                                "%s: -error at login api: %s, %s",
                                txnid,
                                error_type,
                                sys.exc_info(),
                            )
                            return response_data(
                                {"respcode": 411, "respdesc": error_type}
                            )
                        else:
                            logger.error(
                                "%s -error at login api: %s", txnid, sys.exc_info()
                            )
                            return response_data(
                                {"respcode": 411, "respdesc": error_type}
                            )                            

                except Exception:
                    logger.error(
                        "%s login api request sent error: %s", txnid, sys.exc_info()
                    )
                    return response_data(errors["INTERNAL_ERROR"])
            except Exception:
                logger.error(
                    "%s internal error at cookie generation: %s", txnid, sys.exc_info()
                )
                return response_data(errors["INTERNAL_ERROR"])
        except Exception:
            logger.error("%s invalid details at login api: %s", txnid, sys.exc_info())
            return response_data(errors["INVALID_DETAILS"])
    except Exception:
        logger.error("%s bad request at login api: %s", txnid, sys.exc_info())
        return response_data(errors["EMPTY_REQUEST_BODY"])
