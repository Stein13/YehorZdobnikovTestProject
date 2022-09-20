from constants import Constants


def test_simple(page, email_for_test):
    page.top_bar.my_account_click()
    page.top_bar.registration_click()
    assert page.registration.page_header_text() == 'Register Account'
    page.registration.first_name_input(Constants.first_name)
    page.registration.last_name_input(Constants.last_name)
    page.registration.email_input(email_for_test)
    page.registration.phone_input(Constants.phone_number)
    page.registration.password_input(Constants.passwod)
    page.registration.confirm_password_input(Constants.passwod)
    page.registration.privacy_policy_checkbox_click()
    page.registration.submit_btn_click()
    assert page.registration.page_header_text() == 'Your Account Has Been Created!'
    page.top_bar.my_account_click()
    assert page.top_bar.my_account_cell_in_dropdown().is_displayed()
    page.top_bar.my_account_click()
    page.top_bar.hover_to_mp3_players()
    page.top_bar.show_all_mp3_player_click()
    assert page.mp3_players.page_header_text() == 'MP3 Players'
    page.mp3_players.ipod_classic_click()
    assert page.mp3_players.product_header_text() == 'iPod Classic'
    page.mp3_players.add_to_cart_btn_click()
    page.top_bar.cart_btn_click()
    assert page.top_bar.product_in_cart_text() == 'iPod Classic'
