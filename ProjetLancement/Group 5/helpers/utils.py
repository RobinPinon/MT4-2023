# Evaluate user response
# @user_response : the response you want too evalute
# Convention : y = TRUE | n = FALSE
def check_user_boolean_response(user_response):
    if user_response != 'y' and user_response != 'n':
        evaluated_response = check_user_boolean_response(input("Bad response please answer y or n. [y/n] ?"))
    else:
        evaluated_response = False if user_response == 'n' else True
    return evaluated_response