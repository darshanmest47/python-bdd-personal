
Feature: Personal Portofolio automation
  Scenario: To Check the title of the page
    Given user is successfully landed on the page
    When user reloads the webpage
    Then the title of the webpage should match exactly with the test title

  Scenario: To Scroll up to the page
    Given user is successfully landed on the page
    When user scrolls upto the top of the page
    And user hovers the mouse over projects
    And user hovers the mouse over contact
    Then hovering action must take place

  Scenario Outline: To enter and check multiple datas
    Given user is successfully landed on the page
    When user scrolls to the react-quiz section
    And user enters the frame containing react-quiz and performs some scrolling
    And user enters multiple values <firstname> <lastname> <email> <password>
    Then values must get entered

    Examples:
      | firstname | lastname | email | password |
      | Darshan   | Mesta    | darshanmesta33@gmail.com | Test1234 |
      | Suraj   | Mesta    | surajmesta47@gmail.com | Test12345 |


