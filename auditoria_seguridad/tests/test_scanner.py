import unittest
from core.utils import get_severity, calculate_header_score

class TestSecurityScanner(unittest.TestCase):
   def test_get_severity(self):
     # Abbiamo testato casi estremi: punteggio alto e punteggio basso.
     self.assertEqual(get_severity(10), "INFO")
     self.assertEqual(get_severity(0), "CRITICAL")
   
   def test_calculate_header_score(self):
     # Abbiamo testato un caso con 0 intestazioni rilevate.
     self.assertEqual(calculate_header_score([]), 0)


if __name__ == '__main__':
    unittest.main()
