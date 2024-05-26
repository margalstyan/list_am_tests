# List.am Test Automation Framework

This repository contains a test automation framework for [list.am](https://www.list.am/) using `Python`, `Pytest`,
and `Selenium`.

## Project Structure

- `tests/`: Contains test cases.
- `pages/`: Contains page objects.
- `conftest.py`: Contains configuration and fixtures for `pytest`.
- `config.properties`: Contains property values.
- `pytest.ini`: Configuration file for `pytest`.
- `requirements.txt`: Lists the project dependencies.

## Setup

### Prerequisites

- Python 3.x
- `pip` package manager
- Google Chrome browser
- ChromeDriver (Make sure the version matches your installed Chrome browser version)

### Installation

1. Clone the repository:

```sh
git clone https://github.com/margalstyan/list_am_tests.git
cd list_am_tests
```

2. Install the dependencies:

```sh
pip install -r requirements.txt
```

## Running the Tests

To run the tests, use the following command:

```sh
pytest
```

## Writing Tests

1. Create a new file in the `tests` directory, e.g., `test_example.py`.

2. Import the necessary page objects and pytest.

3. Write your test cases using the pytest framework.

## Project Configuration

### 1. `conftest.py`

This file contains the setup and teardown code for the WebDriver instance:

### 2. `pytest.ini`

This file configures pytest:

### 3. `config.properties`
This file contains property values of elements (expected names, URLs, placeholders and etc.)

### 4. Page Objects

Page objects are used to abstract the interactions with the web pages.

#### `base_page.py`: This is a base class for all page objects:

#### `homepage.py`: This represents the homepage and its interactions:
