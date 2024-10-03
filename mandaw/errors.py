
class MandawBasicException(Exception):
    """ Manda basic raise exception """


class MandawError(Exception):
    """ Message error for call func in SDL """
    
    def __init__(self, message: str) -> None:
        self.message: str = message
        super().__init__(message)
    
    def __repr__(self) -> str:
        return f"Mandaw error for {self.message}"


class MandawErrorType(TypeError):
    """ Error Mandaw variables types, example: Colors, InputType, etc... """
    def __init__(self, message: str) -> None:
        self.message: str = message
        super().__init__(message)
    
    def __repr__(self) -> str:
        return f"Mandaw error type for {self.message}"
