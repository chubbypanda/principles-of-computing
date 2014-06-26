# unit tests for Mini-project 1 (clone of Cookie Clicker game), by k., 06/22/2014

import unittest
from mini_project1 import ClickerState
from mini_project1 import BuildInfo
from mini_project1 import simulate_clicker
from mini_project1 import strategy_cursor
from mini_project1 import strategy_cheap
from mini_project1 import strategy_expensive


class TestClass(unittest.TestCase):
    def setUp(self):
        self.clicker = ClickerState()
    def test_initialized(self):
        self.assertEqual(self.clicker.get_cookies(), 0.0)
        assert type(self.clicker.get_cookies()) == float
        self.assertEqual(self.clicker.get_cps(), 1.0)
        assert type(self.clicker.get_cps()) == float
        self.assertEqual(self.clicker.get_time(), 0.0)
        assert type(self.clicker.get_time()) == float
        self.assertEqual(self.clicker.get_history(), [(0.0, None, 0.0, 0.0)])
        assert type(self.clicker.get_history()) == list
    def test_methods(self):
        self.assertEqual(self.clicker.time_until(5), 5)
        self.assertEqual(self.clicker.time_until(1000000), 1000000.0)
        self.assertEqual(self.clicker.time_until(0), 0.0)
        assert type(self.clicker.time_until(0.0)) == float
        assert type(self.clicker.time_until(0)) == float
        self.clicker.wait(0)
        self.assertEqual(self.clicker.get_time(), 0.0)
        assert type(self.clicker.get_time()) == float
        self.assertEqual(self.clicker.get_cookies(), 0.0)
        self.clicker.wait(5)
        self.assertEqual(self.clicker.get_time(), 5.0)
        self.assertEqual(self.clicker.get_cookies(), 5.0)
        self.clicker.wait(1000000)
        self.assertEqual(self.clicker.get_time(), 1000005.0)
        self.assertEqual(self.clicker.get_cookies(), 1000005.0)
    def test_shopping(self):
        self.assertEqual(self.clicker.get_history(), [(0.0, None, 0.0, 0.0)])
        self.clicker.buy_item('Nuf', 1000.0, 101.0)
        # not enough resource to purchase it, nothing happened
        self.assertEqual(self.clicker.get_history(), [(0.0, None, 0.0, 0.0)])
        time = self.clicker.time_until(1000.0)
        self.clicker.wait(time)
        self.clicker.buy_item('Nuf', 1000.0, 101.0)
        self.assertEqual(self.clicker.get_history(), [(0.0, None, 0.0, 0.0), (time, 'Nuf', 1000.0, 1000.0)])


class TestFunction(unittest.TestCase):
    def test_simulate(self):
        out = simulate_clicker(BuildInfo(), 10000000000.0, strategy_cursor)
        # comparing (after it's been rounded) to known values provided at:
        # https://class.coursera.org/principlescomputing-001/wiki/view?page=clicker
        self.assertEqual(round(out.get_cps(), 1), 16.1)
        self.assertEqual(out.get_time(), 10000000000.0)
        self.assertEqual(round(out.get_cookies(), 1), 6965195661.5)
        # ClickerState class doesn't expose total number publicly (should be: total cookies: 153308849166.0)
    def test_strategies(self):
        out = simulate_clicker(BuildInfo(), 10000000000.0, strategy_cheap)
        self.assertEqual(round(out.get_cps(), 1), 123436706.3)
        self.assertEqual(out.get_time(), 10000000000.0)
        self.assertEqual(round(out.get_cookies(), 1), 149360255735977.9)
        # ClickerState class doesn't expose total number publicly (should be: total cookies: 1.15285935621e+18)
        out = simulate_clicker(BuildInfo(), 10000000000.0, strategy_expensive)
        self.assertEqual(round(out.get_cps(), 1), 133980795.7)
        self.assertEqual(out.get_time(), 10000000000.0)
        self.assertEqual(round(out.get_cookies(), 8), 2414.64612076)
        # ClickerState class doesn't expose total number publicly (should be: total cookies: 6.83676443443e+17)
    def test_strategy_cheap(self):
        self.assertEqual(strategy_cheap(0, 0, 0, BuildInfo()), None)
        self.assertEqual(strategy_cheap(100, 1.0, 10, BuildInfo()), 'Cursor')
        self.assertEqual(strategy_cheap(10000000, 10000.0, 10000, BuildInfo()), 'Cursor')
    def test_strategy_expensive(self):
        self.assertEqual(strategy_expensive(0, 0, 0, BuildInfo()), None)
        self.assertEqual(strategy_expensive(10, 1.0, 10, BuildInfo()), 'Cursor')
        self.assertEqual(strategy_expensive(100, 1.0, 10, BuildInfo()), 'Grandma')
        self.assertEqual(strategy_expensive(1000, 1.0, 10, BuildInfo()), 'Farm')
        self.assertEqual(strategy_expensive(10000, 1.0, 10, BuildInfo()), 'Mine')
        self.assertEqual(strategy_expensive(100000, 1.0, 10, BuildInfo()), 'Shipment')
        self.assertEqual(strategy_expensive(1000000, 1.0, 10, BuildInfo()), 'Alchemy Lab')
        self.assertEqual(strategy_expensive(10000000, 10000.0, 10000, BuildInfo()), 'Portal')
        self.assertEqual(strategy_expensive(100000000, 10000.0, 10000, BuildInfo()), 'Time Machine')
        self.assertEqual(strategy_expensive(1000000000000, 10000.0, 10000, BuildInfo()), 'Antimatter Condenser')
        

# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
