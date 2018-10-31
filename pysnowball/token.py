import os
import pysnowball.cons as cons

def get_token():
    if os.environ.get('XUEQIUTOKEN') is None:
        raise Exception(cons.NOTOKEN_ERROR_MSG)
    else:
        return os.environ['XUEQIUTOKEN']

def set_token(token):
    os.environ['XUEQIUTOKEN'] = token
    return os.environ['XUEQIUTOKEN']
