Feature: Time functionality
    As a user
    I want to manage my timesheet
    So that I can track my working hours

    Background:
      Given User is logged in

    Scenario: Navigate to Time page
      When User clicks on "Time" menu item
      Then "Time" page is displayed

    Scenario: Log time in timesheet
      Given User is on "Time" page
      When Select personal timesheets
    #   And Log "<hours>" time against "<project>" and submit
    #   Then Success message is displayed
    #   And Timesheet entry is visible

    # Scenario Outline: Validate timesheet input
    #   Given User is on "Time" page
    #   When User enters "<hours>" hours
    #   Then "<message>" is displayed

    #   Examples:
    #     | hours | message                    |
    #     | -5    | Hours must be positive     |
    #     | 25    | Cannot exceed 24 hours     |
    #     | 8     | Time saved successfully    |  