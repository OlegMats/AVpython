import pytest

from app.application import Application


@pytest.mark.parametrize("brand, model",
                         [("Audi", "100"), ("Bentley", "Continental GT"), ("Citroen", "C2"), ("Lexus", "RX"),
                          ("Volvo", "XC90")])
def test_search(driver, get_logger, brand, model):
    app = Application(driver, get_logger)
    app.search_page.go_to_search_with_params()
    app.search_params_form.search_for_brand(brand)
    app.search_params_form.search_for_model(model)
    app.search_params_form.show_results()
    assert brand and model in app.search_results_page.get_first_search_result(), "Wrong search results"
