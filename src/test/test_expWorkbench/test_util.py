'''
Created on 22 nov. 2012

.. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
'''
import os
import unittest

from expWorkbench import  ema_logging
import numpy as np

from expWorkbench.util import save_results, load_results

def setUpModule():
    global cwd 
    cwd = os.getcwd()
    dir_of_module = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dir_of_module)

def tearDownModule():
    os.chdir(cwd)

class Save_ResultsTestCase(unittest.TestCase):
    def test_save_results(self):
        # test for 1d
        # test for 2d
        # test for 3d
        # test for very large
        
        nr_experiments = 10000
        experiments = np.recarray((nr_experiments,),
                               dtype=[('x', float), ('y', float)])
        outcome_a = np.random.rand(nr_experiments,1)
        
        results = (experiments, {'a': outcome_a})
    
        fn = r'../data/test.tar.gz'
        
        save_results(results, fn)
        os.remove(fn)
        ema_logging.info('1d saved successfully')
        
        nr_experiments = 10000
        nr_timesteps = 100
        experiments = np.recarray((nr_experiments,),
                               dtype=[('x', float), ('y', float)])
        outcome_a = np.zeros((nr_experiments,nr_timesteps))
        
        results = (experiments, {'a': outcome_a})
        save_results(results, fn)
        os.remove(fn)
        ema_logging.info('2d saved successfully')
     
     
        nr_experiments = 10000
        nr_timesteps = 100
        nr_replications = 10
        experiments = np.recarray((nr_experiments,),
                               dtype=[('x', float), ('y', float)])
        outcome_a = np.zeros((nr_experiments,nr_timesteps,nr_replications))
         
        results = (experiments, {'a': outcome_a})
        save_results(results, fn)
        os.remove(fn)
        ema_logging.info('3d saved successfully')
        
        nr_experiments = 500000
        nr_timesteps = 100
        experiments = np.recarray((nr_experiments,),
                               dtype=[('x', float), ('y', float)])
        outcome_a = np.zeros((nr_experiments,nr_timesteps))
        
        results = (experiments, {'a': outcome_a})
        save_results(results, fn)
        os.remove(fn)
        ema_logging.info('extremely long saved successfully')
    
class Load_ResultsTestCase(unittest.TestCase):
    def test_load_results(self):
        # test for 1d
        # test for 2d
        # test for 3d
    
        nr_experiments = 10000
        experiments = np.recarray((nr_experiments,),
                               dtype=[('x', float), ('y', float)])
        outcome_a = np.zeros((nr_experiments,1))
        
        results = (experiments, {'a': outcome_a})
        
        save_results(results, r'../data/test.tar.gz')
        experiments, outcomes  = load_results(r'../data/test.tar.gz')
        
        logical = np.allclose(outcomes['a'],outcome_a)
        
        os.remove('../data/test.tar.gz')
        
        if logical:
            ema_logging.info('1d loaded successfully')
        
        nr_experiments = 1000
        nr_timesteps = 100
        nr_replications = 10
        experiments = np.recarray((nr_experiments,),
                               dtype=[('x', float), ('y', float)])
        outcome_a = np.zeros((nr_experiments,nr_timesteps,nr_replications))
         
        results = (experiments, {'a': outcome_a})
        save_results(results, r'../data/test.tar.gz')
        experiments, outcomes = load_results(r'../data/test.tar.gz')
        
        logical = np.allclose(outcomes['a'],outcome_a)
        
        os.remove('../data/test.tar.gz')
        
        if logical:
            ema_logging.info('3d loaded successfully')
    
class ExperimentsToCasesTestCase(unittest.TestCase):
    pass

class MergeResultsTestCase(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()