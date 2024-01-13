import unittest
from factories.profile_factory import ProfileFactory


class TestProfileFactory(unittest.TestCase):
    def test_create_profile(self):
        profile = ProfileFactory.create()
        self.assertIsNotNone(profile)
        
    def test_bulk_create_profiles(self):
        profiles = ProfileFactory.create_batch(size=5)
        self.assertEqual(len(profiles), 5)

if __name__ == '__main__':
    unittest.main()