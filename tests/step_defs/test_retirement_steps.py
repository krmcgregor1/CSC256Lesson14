# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:10:12 2020

@author: KaiMcGregor
"""
from pytest_bdd import scenarios, parsers, when, then
from pytest import raises, fixture

import retirement

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'birthYear': int,
    'birthMonth': int,
    'ageYear': int,
    'ageMonth': int,
    'retireMonth': int,
    'retireYear': int,
}

scenarios('../features/test_retirement_age.txt', example_converters=CONVERTERS)
scenarios('../features/test_input_out_of_range.txt', example_converters=CONVERTERS)
scenarios('../features/retirement_date_rollover.txt', example_converters=CONVERTERS)

@fixture
def inputList():
    return []

@when(parsers.cfparse('the user entered "{birthYear:Number}" as their birth year', extra_types=EXTRA_TYPES))
@when('the user entered "<birthYear>" as their birth year')
def input_birthYear(inputList, birthYear):
    inputList.append(birthYear)

@when(parsers.cfparse('the user entered "{birthMonth:Number}" as their birth month', extra_types=EXTRA_TYPES))
@when('the user entered "<birthMonth>" as their birth month')
def input_birthMonth(inputList, birthMonth):
    inputList.append(birthMonth)

@when(parsers.cfparse('the user entered "{ageYear:Number}" as their age year', extra_types=EXTRA_TYPES))
@when('the user entered "<ageYear>" as their age year')
def input_ageYear(inputList, ageYear):
    inputList.append(ageYear)
    
@when(parsers.cfparse('the user entered "{ageMonth:Number}" as their age month', extra_types=EXTRA_TYPES))
@when('the user entered "<ageMonth>" as their age month')
def input_ageMonth(inputList, ageMonth):
    inputList.append(ageMonth)
    
@then('a ValueError is raised')
def catchInputError(inputList):
    with raises(ValueError):
        retirement.calculate_retirement_date(*inputList)
        
@then(parsers.cfparse('the retirement date is "{retireMonth:Number}"-"{retireYear:Number}"', extra_types=EXTRA_TYPES))
def tst_retirement_date(inputList, retireYear, retireMonth):
    assert (retireYear, retireMonth) == retirement.calculate_retirement_date(*inputList)
    
@then(parsers.cfparse('the retirement age is "{retireYear:Number}" years and "{retireMonth:Number}" months', extra_types=EXTRA_TYPES))
@then('the retirement age is "<retireYear>" years and "<retireMonth>" months')
def tst_retirement_age(inputList, retireYear, retireMonth):
    assert (retireYear, retireMonth) == retirement.calculate_retirement_age(*inputList)