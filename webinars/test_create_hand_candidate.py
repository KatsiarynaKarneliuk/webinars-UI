from .pages.handCandidateCreate_page import handCandidateCreatePage
from .pages.candidates_page import CandidatesPage
from .pages.webinar_page import WebinarPage
import time


def test_can_create_hand_candidate( browser,open_login_page):
    open_login_page.login_by_email("tcekrqytb@emlpro.com", "123456")
    WebinarPage(browser).should_go_to_candidates_page()
    time.sleep(3)
    CandidatesPage(browser).check_previous_amount_candidates()
    time.sleep(3)
    CandidatesPage(browser).should_be_button_create_candidate()
    CandidatesPage(browser).should_go_to_candidate_create_page()
    time.sleep(3)
    handCandidateCreatePage(browser).should_be_handCandidateCreate_page()
    handCandidateCreatePage(browser).can_fill_create_form()
    time.sleep(10)
    handCandidateCreatePage(browser).save_hand_candidate()
    CandidatesPage(browser).check_next_amount_candidates()
    CandidatesPage(browser).compare_previous_next_amount_candidates('previous_value', 'next_value')



