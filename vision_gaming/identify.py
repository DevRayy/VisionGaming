def debug_identifier(message):
    def debug_identifier_wrapped(input):
        print(message)
        return message
    return debug_identifier_wrapped
