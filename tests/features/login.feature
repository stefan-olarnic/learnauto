Feature: Login functionality
    As user I want to be able to login in order to access other main application

    Scenario Outline: Login with different credentials
      Given User is on login page
      When User login with username "<username>" and password "<password>"
      Then "<message>" is displayed

      Examples:
        | username | password  | message             |
        | Admin    | admin123  | Dashboard           |
        | baduser  | badpass   | Invalid credentials |
        | Admin    | wrongpwd  | Invalid credentials |
      