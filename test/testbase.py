


from unittest import TestCase


class TestBase(TestCase):


    
    MODEL = {
        "ResTune" : {"type": "Alex", "param": {"step": 10, "res":10000}},
        }
    PARAM = {"arm": "RedM"}
    DATA  = {"wavesky": "/home/swei20/PIML/PIML_spec/test/testdata/wavesky.npy"}
