class TestData:
    CHROME_EXECUTABLE_PATH = r"C:\mygit-hub_projects\trello\driver\chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = r"C:\mygit-hub_projects\trello\driver\geckodriver.exe"

    BASEURL ='https://trello.com'
    Email = 'adidokania08+01@gmail.com'
    Password = 'Test12345'
    BoardTitle ='Test'
    ListName = 'List1'
    CardName = 'Hello'


#behave --no-capture Features/createCard.feature
#behave --format=allure_behave.formatter:AllureFormatter -o Reports
#allure generate C:\mygit-hub_projects\trello\Reports --clean -o allure-report