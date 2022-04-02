from abc import abstractmethod
from spec.crust.data.spec import StellarSpec
from spec.crust.process.specprocess import StellarSpecProcess
from baseIF.gateway.baseprocessIF import ProcessIF
from .specloaderIF import SpecLoaderIF, WaveSkyLoaderIF

class StellarSpecProcessIF(ProcessIF):
    def __init__(self) -> None:
        super().__init__()
        self.Loader   = SpecLoaderIF()
        self.Process  = StellarSpecProcess()
        self.Storer   = None

    def set_data(self, DATA_PARAM):
        self.wavesky  = WaveSkyLoaderIF(DATA_PARAM["WSKY_PATH"]).load()
        self.OP_DATA  = {"wavesky": self.wavesky}

    def set_param(self, OP_PARAM):
        self.OP_PARAM = self.paramIF(OP_PARAM)
    
    def set_model(self, MODEL_PARAM):
        self.OP_MODEL = MODEL_PARAM

    def paramIF(self, PARAMS):
        #TODO create class later
        return PARAMS

    def interact_on_Object(self, Spec: StellarSpec):
        self.Process.set_process(self.OP_PARAM, self.OP_MODEL, self.OP_DATA)
        self.Process.start(Spec)
