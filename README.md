### Cucumber Framework
_This is a base for mobile automation using Python and Appium + cucumber._

#### Prerequisites:
#### Install:
* [Python](https://www.python.org/downloads/)
* [Appium](https://appium.io/docs/en/about-appium/getting-started/?lang=en)
* [Cucumber - behave](https://behave.readthedocs.io/en/stable/install.html)
####  Libraries:
* [Appium python client](https://pypi.org/project/Appium-Python-Client/) 
* [Unidecode](https://pypi.org/project/Unidecode/) 
* [Allure - behave](https://pypi.org/project/allure-behave/)

#### Structure
* features: _it contains all the requirements and the configuration for the environment._
* helper: _it contains all methods needed for actions_
* reports: _after running the tests, a new report is created by current date and time_
* screenshots: _in case of a failure, a screenshot is taken and saved in this location_  
* steps: _it contains all the calls for the actions_

#### How to run the project?
```
 sh features/suite.sh
```