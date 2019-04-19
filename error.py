class Error:
    errorMessage = ''
    def isPlayerAmountValid(self, amount):
        isValid = amount > 0 and amount <= 4 
        if not isValid: 
            Error.errorMessage = 'Player Amount is Not Valid'
        return isValid

# errorHandle = Error()