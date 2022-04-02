from abc import abstractmethod
from spec.crust.data.spec import StellarSpec
from spec.crust.process.specprocess import StellarSpecProcess
from baseIF.gateway.baseprocessIF import ProcessIF
from .specloaderIF import SpecLoaderIF, WaveSkyLoaderIF


class BaseSpecProcessIF(ProcessIF):
    """ Base class for process interface for Spec object only. """
    @abstractmethod
    def interact_on_Spec(self, param, Spec: StellarSpec):
        pass

class StellarSpecProcessIF(BaseSpecProcessIF):
    def __init__(self) -> None:
        super().__init__()
        self.Loader   = SpecLoaderIF()
        self.Process  = StellarSpecProcess()
        self.Storer   = None

    def set_data(self, DATA_PARAM):
        self.wavesky  = WaveSkyLoaderIF(DATA_PARAM["wavesky"])
        self.OP_DATA  = {"wavesky": self.wavesky}

    def set_param(self, OP_PARAM):
        self.OP_PARAM = self.paramIF(OP_PARAM)
    
    def set_model(self, MODEL_PARAM):
        self.OP_MODEL = MODEL_PARAM

    def interact_on_Spec(self, PARAMS, Spec: StellarSpec):
        self.setup(PARAMS)
        self.interact_on_Object(Spec)

    def paramIF(self, PARAMS):
        #TODO create class later
        return PARAMS

