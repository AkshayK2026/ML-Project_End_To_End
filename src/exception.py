import sys
import logging

def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script [{0}], line [{1}], message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_detail)

    def __str__(self):
        return self.error_message
if __name__ == "__main__":
    try:
        raise Exception("This is a test exception")
    except Exception as e:
        exc = CustomException(e, sys)
        print(exc)
        print(str(exc))
        print(repr(exc))
