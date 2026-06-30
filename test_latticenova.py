# test_latticenova.py
"""
Tests for LatticeNova module.
"""

import unittest
from latticenova import LatticeNova

class TestLatticeNova(unittest.TestCase):
    """Test cases for LatticeNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LatticeNova()
        self.assertIsInstance(instance, LatticeNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LatticeNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
