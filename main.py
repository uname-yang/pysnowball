# encoding=utf8
from pysnowball import token
import json

token.set_token("xq_a_token=ddad281339b399ec0c9388a67df7351179db4163;")

if __name__ == '__main__':
    from pysnowball import quote_detail

    qt = quote_detail("SH600104")
    print(json.dumps(qt))
