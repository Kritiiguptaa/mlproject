# For custom exception handling.

import sys   #sys is a built-in Python module that gives access to the Python runtime environment.
# provides access to system-specific parameters and functions
from src.logger import logging
import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_message
    

#Constructor
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

#its like int main() to check if code working
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomExecption(e,sys)


#------------ Also on notion notes -------------------
# Why is sys used in your code?
# ⭐ MAIN REASON:
# To get exception details like:
# File name
# Line number
# Stack trace

# This comes from:
# sys.exc_info()

# type, value, traceback = sys.exc_info()
