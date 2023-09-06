# Technical specifications


The dependencies manager used on this project is [Poetry](https://python-poetry.org/). It's suggested to install the projects dependencies using it, this way you can run the E2E tests. The E2E tests were developed using Chrome and Firefox as the browser used on tests.

To choose which browser you'd like to run edit the value from browser on behave.ini, the available options are firefox or chrome.

It was developed with Python 3.11.4.

And is required at least Python on version 3.11.

And also is required Docker where we run selenium-grid.

For the tests the chosen framework is [Behave](https://pypi.org/project/behave/) supported by [Selenium](https://pypi.org/project/selenium/) and [Expects](https://pypi.org/project/expects/) to a more readable assertion.


# How to run
First, clone this repository using the following command:

```
git clone https://github.com/rvmoura96/realworld.git
```

Then enter into the project directory:
```
cd integration_tests
```

All the instructions to run is assuming that you have Poetry installed and you are on inthegration_tests directory


On the inthegration_tests directory run this command to install all the projects dependencies:
```
poetry install
```

After the installation run this command to activate a virtual environment where the projects dependencies were installed on the above instruction.
```
poetry shell
```

To download selenium-grid image run the following command:
```
docker pull selenium/standalone-chrome
```

after the download execute the following command to start the selenium-grid container:
```
docker run -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome
```

Another step needed is to get the ip of the machine where its running, for unix os you can use the command *ifconfig* your local ip should be something like 192.168.X.X. after you get your IP you should update the variable local_machine_ip on behave.ini file using your IP as the value.

To run the tests use:
```
behave tests/features
```


You can change the default browser to the tests updating the browser on the behave.ini file.

You can choose between chrome or firefox.
