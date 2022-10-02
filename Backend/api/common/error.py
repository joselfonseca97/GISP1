def buildErrorResponse(message="Unknown error", status_code=400):
    return {
               "error": message,
               "status": status_code
           }, status_code


class CustomError(Exception):
    def __init__(self, message="Unknown error", status_code=400):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def buildErrorResponse(self):
        return {
                   "error": self.message,
                   "status": self.status_code
               }, self.status_code
