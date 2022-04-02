from unittest import TestCase
from .dataloader import TestDataLoader

class TestBase(TestCase):
    def __init__(self, *arg, **kwargs) -> None:
        super().__init__(*arg, **kwargs)
        self.D = TestDataLoader()
        


        