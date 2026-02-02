Feature: Login functionality
    Ca user al aplicației
    Vreau să pot face login
    Pentru a accesa zona securizată

    Scenario Outline: Login with different credentials
      Given I am on the login page
      When I login with username "<username>" and password "<password>"
      Then I should see the message "<message>"

      Examples:
        | username    | password              | message                              |
        | tomsmith    | SuperSecretPassword!  | You logged into a secure area!       |
        | invaliduser | anypassword           | Your username is invalid!            |
        | tomsmith    | wrongpassword         | Your password is invalid!            |
      