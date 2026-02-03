# exemplu de test pentru cand o sa folosesc fixture-ul de (logged_context)
from pages.login.login_page import LoginPage

def test_dashboard(logged_context):
    # logged_context este deja logat
    logged_context.driver.get(logged_context.base_url + "/secure")
    
    page = LoginPage(logged_context)
    message = page.get_message()
    
    assert "You logged into a secure area!" in message
