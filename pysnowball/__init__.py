import codecs
import os

__version__ = codecs.open(os.path.join(
    os.path.dirname(__file__), 'VERSION.txt')).read()
__author__ = 'Yang Yu'

"""
for finance data
"""
from pysnowball.finance import (cash_flow)



from pysnowball.token import (get_token,set_token)