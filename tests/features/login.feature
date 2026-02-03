Feature: Login functionality
    Ca user al aplicației
    Vreau să pot face login
    Pentru a accesa zona securizată

    Scenario Outline: Login with different credentials
      Given I am on the login page
      When I login with username "<username>" and password "<password>"
      Then I should see the message "<message>"

      Examples:
        | username | password  | message             |
        | Admin    | admin123  | Dashboard           |
        | baduser  | badpass   | Invalid credentials |
        | Admin    | wrongpwd  | Invalid credentials |
      