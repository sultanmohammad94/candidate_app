import unittest
from factories.candidate_factory import CandidateFactory

class TestCandidateFactory(unittest.TestCase):
    def test_create_candidate(self):
        candidate = CandidateFactory.create()
        self.assertIsNotNone(candidate)
    
    def test_bulk_create_candidates(self):
        candidates = CandidateFactory.create_batch(5)
        self.assertEqual(len(candidates), 5)

if __name__ == '__main__':
    unittest.main()
