import unittest,itertools
from dependency_outage_cutset import run
class DomainTests(unittest.TestCase):
 def test_redundancy_cut_requires_both(self):
  r=run({'root':'r','nodes':[{'id':'r','kind':'any','children':['a','b']},{'id':'a','kind':'component'},{'id':'b','kind':'component'}]});self.assertEqual(r['minimal_cutsets'][0]['components'],['a','b'])
 def test_shared_cause_not_double_counted(self):
  r=run({'root':'r','nodes':[{'id':'r','kind':'any','children':['a','b']},{'id':'a','kind':'all','children':['power','x']},{'id':'b','kind':'all','children':['power','y']},*[{'id':s,'kind':'component'} for s in ('power','x','y')]]});self.assertEqual({tuple(x['components']) for x in r['minimal_cutsets']},{('power',),('x','y')})
 def test_empty_redundancy_is_always_down(self):self.assertTrue(run({'root':'r','nodes':[{'id':'r','kind':'any','children':[]}]})['root_failed_under_observation'])
 def test_empty_all_is_always_up(self):self.assertFalse(run({'root':'r','nodes':[{'id':'r','kind':'all','children':[]}]})['root_failed_under_observation'])
 def test_cycle_rejected(self):
  with self.assertRaises(ValueError):run({'root':'r','nodes':[{'id':'r','kind':'all','children':['r']}]})
