

import numpy as np
from test.testbase import TestBase
from specIF.gateway.specprocessIF import StellarSpecProcessIF

class TestBaseSpecProcessIF(TestBase):
        
    def test_BaseSpecProcessIF(self):
        pass

    def test_StellarSpecProcessIF(self):

        PIF = StellarSpecProcessIF()
        PIF.setup(self.D.PARAM)
        self.assertIsNotNone(PIF.OP_DATA.keys())
        self.assertIsNotNone(PIF.OP_MODEL.keys())
        self.assertIsNotNone(PIF.OP_PARAM.keys())
        # self.assertIsNotNone(PIF.OP_OUT.keys())




    

