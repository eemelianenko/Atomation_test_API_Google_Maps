import json
from requests import Response


"""Methods for checking responses to requests"""

class Checking():

    """Method for checking - status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Successfully! Status code = " + str(response.status_code))
        else:
            print("Wrong! Status code = " + str(response.status_code))


    """Method for checking the presence of required fields in the request response"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields are present")


    """Method for checking the values of required fields in the request response"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print("Field_name - " + field_name + " - is Right!")


    """Method for checking the values of required fields in the request response for the specified word"""

    @staticmethod
    def check_json_search_word_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("A Word - " + search_word + " - is contained!")
        else:
            print("A Word -  " + search_word + " - is not contained!")