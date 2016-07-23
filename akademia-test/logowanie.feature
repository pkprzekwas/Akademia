Feature:
  Logowanie do aplikacji zarejestrowaniego użytkownika.

  Background:
    Given storna logowania jest otwarta

  Scenario Outline: Logowanie jako <ktos>
    When wypenienie '<pole1>' wartoscią '<username>'
    And wypenienie '<pole2>' wartoscią '<password>'
    And kilknę Sign in
    Then Jestem zalogowany jako '<ktos>'
    Examples:
      | pole1          | pole2          | username | password | ktos  |
      | valid_username | valid_password | user     | user     | user  |
      | valid_username | valid_password | user     | admin    | admin |

  Scenario Outline:
    Given '<użytkownik>' nie jest zarejestorowany
    When wypenienie '<pole1>' wartoscią '<username>'
    And wypenienie '<pole2>' wartoscią '<password>'
    And kilknę Sign in
    Then
    Examples:
      | użytkownik     | pole1             | username   | pole2            | password    |
      | invalid_user   | invalid_username  | zly_user   | invalid_password | zle_haslo   |
      | invalid_user   | invalid_username  | pusty_user | password         | puste_haslo |