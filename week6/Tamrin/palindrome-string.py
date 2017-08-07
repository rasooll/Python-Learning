# Type your code here
def _is_palindrome_sample_(sample_string):
    if str(sample_string).lower() == str(sample_string)[::-1].lower():
        return True
    else:
        return False