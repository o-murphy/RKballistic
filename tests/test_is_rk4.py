from py_ballisticcalc.generics.engine import EngineProtocol
from py_ballisticcalc.interface import Calculator
from RKballistic import RK4TrajectoryCalc


class TestIsRK4:
    def test_entry_point_loaded(self, ):
        calc = Calculator(_engine="RKballistic")
        assert isinstance(calc._calc.__class__, EngineProtocol), "Not implements EngineProtocol: %s" % calc._engine.__class__
        assert isinstance(calc._calc, RK4TrajectoryCalc), "Not is RK4TrajectoryCalc"