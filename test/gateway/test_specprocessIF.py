

import numpy as np
from unittest import TestCase
from specIF.gateway.specprocessIF import StellarSpecProcessIF

class TestBaseSpecProcessIF(TestCase):
        
    def test_BaseSpecProcessIF(self):
        pass

    def test_StellarSpecProcessIF(self):
        PARAMS = {
            "data"
        }
            MODEL = {
        "ResTune" : {"type": "Alex", "param": {"step": 10, "res":10000}},
        }
    PARAM = {"arm": "RedM"}
    DATA  = {"wavesky": "/home/swei20/PIML/PIML_spec/test/testdata/wavesky.npy"}

        PIF = StellarSpecProcessIF()
        PIF.setup(PARAMS)
        # self.assertIsNone(np.testing.assert_array_equal(checkWave, self.D.wave))
        self.assertIsNotNone(testSpec.wave)
        self.assertIsNotNone(testSpec.flux)



    

