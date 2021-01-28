from edc_constants.choices import NO


class Eligibility:

    def __init__(self, citizenship=None, legally_married=None,
                 marriage_certificate=None, literacy=None, minor=None):
        """checks if participant is eligible otherwise
            error message is the reason for eligibility test failed."""

        self.reasons_ineligible = []
        if citizenship == NO and legally_married == NO and marriage_certificate == NO:
            self.reasons_ineligible.append('one has to be a citizen , if not must be married to a Motswana with '
                                           'documents')
        if literacy == NO:
            self.reasons_ineligible.append('Must be literate or have a witness available')
        if minor == NO:
            self.reasons_ineligible.append('Should not be a minor')

        self.is_eligible = False if self.reasons_ineligible else True
