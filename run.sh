#!/bin/bash
pytest -s -v -m "sanity" testCases/ --browser chrome --alluredir allure-results
allure serve allure-results
