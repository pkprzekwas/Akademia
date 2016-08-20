from behave import *

use_step_matcher("re")


@given("storna logowania jest otwarta")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("wypenienie '(?P<pole1>.+)' wartoscią '(?P<username>.+)'")
def step_impl(context, pole1, username):
    """
    :type context: behave.runner.Context
    :type pole1: str
    :type username: str
    """
    pass


@step("kilknę Sign in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Jestem zalogowany jako '(?P<ktos>.+)'")
def step_impl(context, ktos):
    """
    :type context: behave.runner.Context
    :type ktos: str
    """
    pass
