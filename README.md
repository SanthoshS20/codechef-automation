# codechef-automation



## Setup Pytest Selenium GitHub Pipeline:

1. Create python GitHub pipeline
2. Setup pipeline to install python verion
3. Install all dependencies from requirements.txt file
4. Install geckodriver 
5. Setup geckodriver path 
    
        import os
        os.environ['PATH'] += ':/driver/geckodriver'

6. Setup webdriver to run in headless mode

        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)



## How to run pytest tests in vscode
1. Clone the remote repository into your local machine
2. Launch vscode application
3. Open the folder in the vscode 
4. Click the Testing icon bar
5. Click configure Python tests button
6. Select the pytest framework
7. Select the directory where your tests resides 
8. A file (settings.json) should be created


        //command line arguments should be given in the pytestArgs values
        
        {
            "github.copilot.editor.enableCodeActions": true,
            "python.testing.pytestArgs": [
                "tests",
        		"--browser_name=chrome"
            ],
            "python.testing.unittestEnabled": false,
            "python.testing.pytestEnabled": true
        }

9. In the Testing activity bar, you will be able to see the complete tests

    ```pytest -v -m "login" --browser_name chrome --html reports/testing.html tests/test_login_page/test_login_page.py```


Note: To debug, add the breakpoint and click debug test on any of the test file.






1. Install pip & python
2. Add python path to the PATH env variable. So that the terminal knows where the python exists in.
3. Install firefox - https://ftp.mozilla.org/pub/firefox/releases/99.0b8/linux-x86_64/en-GB/
4. Set the firefox executable path to PATH variable
5. Install geckodriver
6. Set the geckodriver executable path to PATH variable
7. Check the pip, python, firefox and geckodriver version
8. Now you will be able to run the selenium tests


Documentation:

https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/


https://dev.to/eugenedorfling/installing-the-firefox-web-driver-on-linux-for-selenium-d45


https://gist.github.com/stephenharris/90bb468bf80e7f7b02e8b8afe694de4f


https://ftp.mozilla.org/pub/firefox/releases/99.0b8/linux-x86_64/en-GB/




## Link 

https://pytest-with-eric.com/introduction/how-to-run-pytest-in-vscode/#Setting-Up-Pytest-In-VS-Code

https://stackoverflow.com/questions/60785825/how-to-pass-command-line-arguments-to-pytest-tests-running-in-vscode
