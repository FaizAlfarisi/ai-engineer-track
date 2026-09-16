class ErrorBadRequest(Exception):
    """Error cause by request data or command from user"""
    pass

class ErrorCorruptData(Exception):
    """Error cause load file data or json encoding"""
    pass