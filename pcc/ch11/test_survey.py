import unittest
from survey import AnonymousSurvey

class test_AnonymousSurvey(unittest.TestCase):
    """test for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a sngle response is sotred properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assertIn('English', my_survey.responses)
        

unittest.main()