from baseconverter.converter import convert

ASK_FOR_ORIGINAL_BASE = "What is the original base?"
ASK_FOR_TARGET_BASE = "What is the target base?"
ASK_FOR_VALUE = "What is the value ?"

class User:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.original_base = None
        self.target_base = None
        self.value = None

    def get_response(self, text):
        if self.original_base is None:
            if text.isdigit():
                self.original_base = int(text)
                return ASK_FOR_TARGET_BASE
            else:
                return ASK_FOR_ORIGINAL_BASE


        elif self.target_base is None:
            if text.isdigit():
                self.target_base = int(text)
                return ASK_FOR_VALUE
            else:
                return ASK_FOR_TARGET_BASE


        elif self.value is None:
            self.value = text
            answer = self.calculate_answer()
            self.reset()
            return answer

    def calculate_answer(self):
        return convert(self.original_base, self.target_base, self.value)
