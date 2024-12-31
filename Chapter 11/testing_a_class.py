# NOTE: A variety of Assertions
# When writing a test, you can make any claim that can be expressed as a
# conditional statement. If the condition is true as expected, your 
# assumption about how that part of your program behaves will be
# confirmed.

# NOTE: Examples of assertions
# assert a == b ; Assert that two values are equal
# assert a != b ; Assert that two values are not equal
# assert a ; Assert that a evaluates to True 
# assert not a ; Assert that a evaluates to False
# assert element in list ; Assert that an element is in a list
# assert element not in list ; Assert that an element is not in a list

# NOTE: Anything that can be expressed as a conditional statement can be
# included in a test.

# NOTE: A class to Test
# survey.py
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
        
    def show_question(self):
        """Show the survey question."""
        print(self.question)
        
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"-{response}")

# NOTE: Testing the AnonymousSurvey Class

# NOTE: By default, running the commandc pytest with no arguments will
# run all the tests that pytest discovers in the current directory. To
# focus on the tests in one file, pass the name of the test file you
# want to run.

# NOTE: Using Fixtures
# In testing, a fixture helps set up a test environment. This means 
# creating a resource that's u8sed by more than one test. We create a
# fixture in pytest by writinga function with the decorator
# @pytest.fixture.

# NOTE: A decorator is a directive placed just before a function 
# definition; Python applies this director to the function before it
# runs, to alter how the function code behaves.

# NOTE: When a parameter in a test function matches the name of a
# function with the @pytest.fixture decorator, the fixture will be run
# automatically and the return value will be passed to the test
# function.