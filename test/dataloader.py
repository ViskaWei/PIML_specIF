# import os
# import h5py


# ROOT     = os.environ["ROOT"]
# TEST     = os.environ["TEST"]
# SPECGRID = os.environ["SPECGRID"]
# PREPNN   = os.environ["PREPNN"]



class TestDataLoader():
    def __init__(self) -> None:
        self.OBJECT= {"path": ""}
        self.MODEL = {
            "ResTune" : {"type": "Alex", "param": {"step": 10, "res":10000}},
            }
        self.OP = {"arm": "RedM"}
        self.DATA  = {"wavesky": "/home/swei20/PIML/PIML_spec/test/testdata/wavesky.npy"}

        self.PARAM = {
            "object": self.OBJECT,
            "data"  : self.DATA,
            "op"    : self.OP,
            "model" : self.MODEL,
        }