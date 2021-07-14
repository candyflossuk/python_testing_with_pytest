# python_testing_with_pytest
A follow along from the "Python Testing With PyTest" book - with relevant notes and interesting code samples

# What is Pytest?
- Python Testing Tool
- Software test framework
    - Finds the tests written
    - Runs the tests
    - Reports the results
    
# Why PyTest over some other framework?
- Simple tests (that are simple to write)
- Easy to read
- Get started quickly
- Use assert to fail a test 
- Use pytest to run tests written for unittest or nose

# Test Strategy ( Definitions )
- Unit Test: A test that checks a small bit of code, like a function or class in isolation from the complete system.
  

- Integration Test: A test that checks a larger bit of code - several classes or subsystem. A label for something larger than a unit test yet smaller than a system test


- System test (end to end): A test that checks all the system under test- in an environment as close to production as possible.


- Functional test: A test that checks a single bit of functionality in a system.


- Subcutaneous test: A test that does not run against the final end user interface but one just below the surface.

# Possible outcomes from a test function

- PASSED (.) - The test was successful

- FAILED (F) -  The test did not run successfully (or XPASS + strict)

- SKIPPED(s) - The test was skipped  

- xfail (x): The test was not supposed to pass, ran and failed

- XPASS (X): The test was not supposed to pass, ran and passed

- ERROR (E): An exception happened outside of the test function in the fixture or hook function
