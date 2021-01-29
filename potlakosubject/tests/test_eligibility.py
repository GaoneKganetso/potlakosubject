from django.test import TestCase
from edc_constants.constants import NO, YES

from ..eligibility import Eligibility


class TestEligibility(TestCase):
    """"
    Participant who are not citizens or not married to a Motswana with documents is not eligible
    """
    def test_citizenship_ineligibility(self):
        eligiblity = Eligibility(citizenship=NO)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('one has to be a citizen , if not must be married to a Motswana and have documents',
                      eligiblity.reasons_ineligible)

    """ Minors are not eligible """
    def test_minor_ineligibility(self):
        eligiblity = Eligibility(minor=YES)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('Should not be a minor', eligiblity.reasons_ineligible)

    """ Illiterate participant not eligible """
    def test_literacy_ineligibility(self):
        eligiblity = Eligibility(literacy=NO)
        self.assertFalse(eligiblity.is_eligible)
        self.assertIn('Must be literate or have a witness available',
                      eligiblity.reasons_ineligible)



