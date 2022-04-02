


from unittest import TestCase


class TestBase(TestCase):
    def __init__(self, *arg, **kwargs) -> None:
        super().__init__(*arg, **kwargs)
        
        self.OBJECT= {"path"}
        self.MODEL = {
            "ResTune" : {"type": "Alex", "param": {"step": 10, "res":10000}},
            }
        self.PARAM = {"arm": "RedM"}
        self.DATA  = {"wavesky": "/home/swei20/PIML/PIML_spec/test/testdata/wavesky.npy"}

        self.PARAM = {
            "object": self.OBJECT,
            "data"  : self.DATA,
            "op"    : self.PARAM,
            "model" : self.MODEL,
        }

        