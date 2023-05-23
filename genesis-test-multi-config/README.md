
### Prerequisite
#### 1.Set python env
+ Install python3.8(https://www.python.org/downloads/)
+ Install a virtualenv
    ```
    pip install virtualenv
    ```
#### 2.Preparing the project runtime environment
+ Go to the project root folder,
    ```
    cd genesis-test
    virtualenv env
    ```
+ Start the virtual environment  
  Win10:
    ```
    cd venv / Script
    Note: Go directly to the directory where activate is located and use .activate
    ```
    Mac:
    ```
    command:source venv/bin/activate
    ```
+ install the dependency packages
    ```
    pip install -r requirements.txt
    ```
#### 3.Modify local configuration file.
+ Go to the project's conf directory and modify the default.cfg file.A few of the main configurations, for instance:
    ```
    platform = windows #windows
    browser.type = edge #firefox,edge,chrome
    path = /Users/cloudzhao/Desktop/jenkins/staging.properties
    ```
    staging.properties or int.properties.You can ask SRE or Other tester for help.
#### 4.Download the corresponding version of the browser driver for your local computer and replace it.
+ Chrome：<http://chromedriver.storage.googleapis.com/index.html>  
+ Firfox:<https://github.com/mozilla/geckodriver/releases/>  
+ Edge:<https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>  
Download and copy to the genesis-test/driver folder to overwrite.
Note: Please ignore the local added driver file when submitting the code.
#### 5.Run
+ Run a case individually.For instance:
    ```
    python runner.py -t test_no_login_visit_tutorial 
    ```
+ Run multiple test cases at once.For instance:
    ```
    python runner.py -f learn
    ```