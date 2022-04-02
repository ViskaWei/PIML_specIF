import os
from abc import ABC, abstractmethod
from baseIF.gateway.baseloaderIF import DictLoaderIF, ObjectLoaderIF
from spec.crust.data.basespec import StellarSpec

class SpecLoaderIF(DictLoaderIF):
    """ class for loading Spec. """
    def load(self):
        flux = self.load_arg("flux")
        wave = self.load_arg("wave")
        return StellarSpec(wave, flux)

class SkyLoaderIF(DictLoaderIF):
    def load(self, arm, res):
        name = f"{arm}_R{res}"
        sky = self.load_arg(name)
        return sky