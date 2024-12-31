# NOTE: The pytest library is a collection of tools that helps in
# writing tests quickly and simply, while supporting your your tests as
# they grow in complexity along with projects.

# NOTE: While Python includes a lot of functionality in the standard
# library, developers also depend heavily on third-party packages. A
# third-party package is a library that's developed outside the core 
# Python language.

# NOTE: Pip is used to install third-party packages. It helps install
# packages from external resources, it's updated often to address
# potential security issues.

# NOTE: python -m pip install --upgrade pip
# The first part of this command: python -m pip, tells Python to run the
# module pip. The second part, install --upgrade, tells pip to update a
# package that's already been installed. The last part, pip, specifies
# which third-party package should be updated.

# NOTE: Syntax for upgrading packages: python -m pip install --upgrade 
# package_name

# NOTE: The --user flag of pip install tells Python to install a package
# for the current user only.

# NOTE: Syntax for installing packages for the current user:
# python -m pip install --user package_name

# NOTE: Testing a function

# name_function.py
# from name_function import get_formatted_name : used when importing
# from external files

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

# names.py
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")

# NOTE: A unit test verifies that one specicific aspect of a function's
# behavior is correct.

# NOTE: A test case is a collection of unit tests that together prove
# that a function behaves as it's supposed to, within the full range of
# situations you expect it to handle.

# NOTE: A good test case considers all the possible kinds of input a
# function could receive and includes tests to represent each of these
# situations. A test case with full coverage includes a full range of 
# unit tests covering all the possible ways you can use a function.

# NOTE: A test function will call the function to be tested, and it will
# make an assertion about the value that's returned. If the assertion is
# correct, the test will pass. IF the assertion is incorrect, the test
# will fail.

# NOTE: The name of the test file must always start with test_. Pytest 
# will always look for any files that begins with test_, and run all the
# tests it finds in that file.

# NOTE: Test functions need to start with the word test followed by an
# underscore, same with the test file. Any function that starts with
# test_ will be discovered by pytest, and will be run as part of the
# testing process.

# NOTE: Test function names should be long enough that if you see the
# function name in a test report, you'll have a good sense of what
# behavior was being tested.

# NOTE: An assertion is a claim about a condition.

# NOTE: When a test fails, don't change the test. If you change the
# test, it will pass but any code that calls the function like the test
# does will stop working. Instead, fix the code that's causing the test 
# to fail. Examine the changes made to the function, and figure out how
# those changes broke the desired behavior.