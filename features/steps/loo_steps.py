from behave import given, when, then

from src.loo.adventure import Adventure


@when("I start the game")
def step_start_the_game(context):
    context.adventure = Adventure()
    context.last_response = context.adventure.begin()


@given("I am on the loo")
def step_i_am_on_the_loo(context):
    step_start_the_game(context)
    assert "on the loo" in context.last_response.lower()


@when('I say "{command}"')
def step_i_say(context, command):
    context.last_response = context.adventure.tell(command)


@when("I ask for help")
def step_i_ask_for_help(context):
    context.last_response = context.adventure.tell("help")


@when("I look around")
def step_i_look_around(context):
    context.last_response = context.adventure.tell("look around")


@then('I see "{text}"')
def step_i_see(context, text):
    assert text.lower() in context.last_response.lower(), context.last_response


@then("I see hints for interactable objects")
def step_i_see_hints(context):
    assert "<mark>" in context.last_response, context.last_response
