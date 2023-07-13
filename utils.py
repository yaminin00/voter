import os
import sys

from dotenv import load_dotenv
from flask import jsonify
import requests
from loggers import get_logger
from errors import errors


load_dotenv()

logger = get_logger('VOTER')
http_ip = os.getenv('proxy_http_ip')
https_ip = os.getenv('proxy_https_ip')

a = os.getenv('a')

def headerfile(cookies,origin,referer):
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,te;q=0.8',
    'Connection': 'keep-alive',
    'Origin': origin,
    'Referer': referer,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie': cookies,
    'sn': 'loginService'
  }
  return headers



def headerfile_verify(cookies,origin,referer):
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,te;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '0',
    'Origin': origin,
    'Referer': referer,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie': cookies
  }
  return headers




def headerfile_details(cookies, origin, referer):
  headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,te;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': origin,
    'Referer': referer,
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie': cookies,
    'sn': 'loginService'
  }
  return headers




def response_data(error_code, data = None):
    """
    Returns jsonified resonse with result as key and output as value.
    """
    error_code.update({"data": data})    
    return jsonify(error_code)  



 
def login(request):
    try:
        req = request.json
        logger.info("request : %s", req)
        epic = req["epic"]
        txnid = req["txnid"]
        if txnid == "" or epic == "":
            return False
        return txnid, epic

    except Exception:
        logger.error("validating request params : %s", sys.exc_info())
        return False
    
    
# def password_req_params(request):
#     try:
#         req = request.json
#         logger.info("request : %s", req)

#         epic = req["epic"]
#         txnid = req["txnid"]
#         cookies = req["cookies"]
#         reqid = req["reqId"]
#         password = req["pass"]

#         if txnid == "" or epic == "" or cookies == "" or reqid == "" or password == "":
#             return False
        
#         return txnid, epic, cookies, reqid, password

#     except Exception:
#         logger.error("validating request params : %s", sys.exc_info())
#         return False
    
   


def get_cookie():
    try:
      session = requests.Session()          
      response = session.get('https://gateway.eci.gov.in/api/v1/elastic/search-by-epic-from-national-display')
      cookie_res = response.cookies.get_dict().items()

      new_list = []
      for x in cookie_res:
              new_list.append(x)
              return f"{new_list[0][1]}"
    except Exception:
      logger.info(session.cookies.get_dict())
      return response_data(errors["CONNECTION_ERROR"])    

def proxy_ids():
    proxies = {
        'http':http_ip,
        'https':https_ip
        }

    return proxies

