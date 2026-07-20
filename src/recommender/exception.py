"""
1. Exception   

An exception is a runtime error that occurs while a program is executing. 
If it is not handled properly, it interrupts the normal execution of the program.

2. Difference between Syntax Error and Exception

| Syntax Error                       | Exception                                 |
| ---------------------------------- | ----------------------------------------- |
| Occurs before the program runs     | Occurs while the program is running       |
| Code cannot start executing        | Program starts, then encounters a problem |
| Must be fixed by changing the code | Can often be handled using `try`/`except` |


3. What is sys?

sys is a built-in Python module that gives us information about the Python interpreter.


4. sys.exc_info() returns three pieces of information:

    i) Exception type
   ii) Exception object
  iii) Traceback
"""


import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = (
        f"Error occurred in Python script: [{file_name}]"
        f"at line number [{exc_tb.tb_lineno}]"
        f"with error message: [{str(error)}]"
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message,
            error_detail
        )

    def __str__(self):
        return self.error_message

