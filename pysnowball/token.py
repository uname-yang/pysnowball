import os
import pysnowball.cons as cons

def get_token():
    if os.environ.get('XUEQIUTOKEN') is None:
        raise Exception(cons.NOTOKEN_ERROR_MSG)
    else:
        return os.environ['XUEQIUTOKEN']

def get_danjuan_token():
    if os.environ.get('DANJUANTOKEN') is None:
        raise Exception(cons.NOTOKEN_ERROR_MSG)
    else:
        return os.environ['DANJUANTOKEN']

def set_token(token,danjuantoken=None):
    os.environ['XUEQIUTOKEN'] = token
    if danjuantoken:
        os.environ['DANJUANTOKEN'] = danjuantoken
    else:
        os.environ['DANJUANTOKEN'] = token
    return os.environ['XUEQIUTOKEN']
