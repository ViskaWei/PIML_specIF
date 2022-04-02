

import numpy as np
from unittest import TestCase
from specIF.gateway.specprocessIF import StellarSpecProcessIF

class TestBaseSpecProcessIF(TestCase):
        
    def test_BaseSpecProcessIF(self):
        pass

    def test_StellarSpecProcessIF(self):
        PARAMS = 
        
        PIF = StellarSpecProcessIF()
        PIF.setup(PARAMS)
        # self.assertIsNone(np.testing.assert_array_equal(checkWave, self.D.wave))
        self.assertIsNotNone(testSpec.wave)
        self.assertIsNotNone(testSpec.flux)



    
