import sys 
import logging

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in python script name[{0}] line number[{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    # FIX 1: This was indented too far. It's part of the function,
    # not part of the .format() call.
    return error_message
    
# FIX 2: The entire class was incorrectly indented, 
# placing it *inside* the function above.
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        # FIX 3: super() must be called with parentheses.
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message