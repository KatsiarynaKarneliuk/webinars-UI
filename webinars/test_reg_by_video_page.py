
from .pages.reg_by_video_page import RegByVideoPage

def test_user_can_reg(browser):
    link = "https://video.dev.online.vertera.org/ru/sign-in/lending_o_biznese/11"
    page = RegByVideoPage(browser)
    page.open(link)
    name = "testt"
    phone = "+79523215465"
    email = "1234@email.com"
    page.should_be_reg_form()
    page.reg_by_video(name,phone,email)

