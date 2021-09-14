import pytest

from app.application import Application


@pytest.mark.parametrize("email, password, username", [("letmeshadowfiend@gmail.com", "Oleg5969396!", "Олег")])
def test_login(driver, get_logger, email, password, username):
    app = Application(driver, get_logger)
    app.main_page.go_to_other()
    app.other_page.go_to_login_form()
    app.login_page.login_into_app_by_email(email, password)

    assert username in app.other_page.get_username(), f"expected username:{username}"
