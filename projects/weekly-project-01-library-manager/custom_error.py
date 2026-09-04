class ErrorCorruptData(Exception):
    """ Custom exception for handling JSONDecodeError """
    pass
     
class ErrorBadRequest(Exception):
    """ Custom exception for handling invalid user input """
    pass