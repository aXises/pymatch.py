"""Matches the user with potential partners based on inputs from user

The user will input values when prompted to.
Based on the values from the user, the program will attempt to match the inputs received from the user to partners
retrieved from a database.
Inputs must be numbers which will be validated by a additional function.

Algorithm:
    1: Prompt user for inputs
    2: Validate each input by passing the inputs through a function which checks if the input is within the specified
    range and is not a string
    3: Convert the inputs in to strings that matches the database
    4: Passes the converted inputs in to the match function
    5: The match function will match the user inputs exactly with the database and sort the partners personality
    difference from the user's personality value, from least to greatest.
    6: The main function will return the first element from the first list, returned from the match function.

"""

import partners


def match(gender, genderpref, height, heightpref, user_value):
    """Matches inputs from user to potential partners from database.txt.

    Args:
        gender(str): User gender input.
        genderpref(str): User preferred gender input.
        height(str): User height input.
        heightpref(str): User preferred height input.
        user_value(str/int): User personality value, generated from input_questions.

    Returns:
        list: A list of all possible partners which match the arguments from user inputs.

    Raises:
        IndexError: when data retrieved from database is greater than expected value
    """
    potential_partners = partners.Partners()
    partner_name = []
    partner_gender = []
    partner_gender_preference = []
    partner_height = []
    partner_height_preference = []
    partner_score = []
    partners_possible_list = []

    partners_loaded = 0
    while potential_partners.available():
        partners_loaded += 1
        partner_name.append(potential_partners.get_name())
        partner_gender.append(potential_partners.get_gender())
        partner_gender_preference.append(potential_partners.get_sexual_pref())
        partner_height.append(potential_partners.get_height())
        partner_height_preference.append(potential_partners.get_height_pref())
        partner_score.append(potential_partners.get_personality_score())

    # print("There are", partners_loaded, "partners loaded")
    x = 0
    y = 0
    z = 0
    while x < partners_loaded:
        partner_list = [partner_name[x],
                        partner_gender[x],
                        partner_gender_preference[x],
                        partner_height[x],
                        partner_height_preference[x],
                        partner_score[x]]
        x += 1
        # print(partner_list)
        # print(x)
        if partner_list[1] == genderpref \
                and partner_list[2] == gender \
                and partner_list[3] == heightpref \
                and partner_list[4] == height:
            y += 1
            partners_possible = partner_list
            # print("match", y)
            # print("partner",x,"was matched")
            partners_possible_list.append(partners_possible)

    while len(partners_possible_list) > z:
        partner_value = partners_possible_list[z][5]
        difference = int(user_value) - int(partner_value)
        del partners_possible_list[z][5]
        partners_possible_list[z].append(abs(difference))
        # print(partners_possible[x])
        z += 1
    partners_possible_list.sort(key=lambda x: x[5])
    return partners_possible_list


def converter(gender, genderpref, height, heightpref):
    """Converts user inputs from numbers to its associated string

    Args:
        gender(str): User gender input.
        genderpref(str): User preferred gender input.
        height(str): User height input.
        heightpref(str): User preferred height input.

    Returns:
        list: A list of the user inputs, converted from numbers to strings

    """
    if gender == "1":
        input_gender = "male"
    elif gender == "2":
        input_gender = "female"
    elif gender == "3":
        input_gender = "other"

    if genderpref == "1":
        input_gender_pref = "male"
    elif genderpref == "2":
        input_gender_pref = "female"
    elif genderpref == "3":
        input_gender_pref = "other"

    if height == "1":
        input_height = "tall"
    elif height == "2":
        input_height = "medium"
    elif height == "3":
        input_height = "short"

    if heightpref == "1":
        input_height_pref = "tall"
    elif heightpref == "2":
        input_height_pref = "medium"
    elif heightpref == "3":
        input_height_pref = "short"

    converted_list = [input_gender, input_gender_pref, input_height, input_height_pref]
    return converted_list


def input_validator(user_inputs, typeof_question):
    """Validates user inputs to ensure that the input is valid

    Args:
        user_inputs(int): The user input.
        typeof_question(str): The type of question that will be validated.

    Returns:
        int: Returns the user's original input if the input is valid.

    """
    if typeof_question == "std":
        if str.isdigit(user_inputs) and 0 < int(user_inputs) < 3:
            validated_input = user_inputs
            return validated_input
        else:
            while not str.isdigit(user_inputs) or 0 >= int(user_inputs) or 3 < int(user_inputs):
                user_inputs = input("Please enter a valid value:")
                validated_input = user_inputs
                if str.isdigit(user_inputs) and 0 < int(user_inputs) < 3:
                    return validated_input

    elif typeof_question == "personality":
        if str.isdigit(user_inputs) and 0 < int(user_inputs) < 5:
            validated_input = user_inputs
            return validated_input
        else:
            while not str.isdigit(user_inputs) or 0 >= int(user_inputs) or 5 < int(user_inputs):
                user_inputs = input("Please enter a valid value:")
                validated_input = user_inputs
                if str.isdigit(user_inputs) and 0 < int(user_inputs) < 5:
                    return validated_input


def main():
    """Main function of the program. Called to start the program.

    Args:
        This function does not accept any arguments.

    Returns:
        str: The name of the potential partner according to the user inputs.

    """
    input_name = input("Please enter your name: ")
    print("\nHi", input_name + ".")
    input_gender = input("What is your gender?"
                         "\n1) male\n2) female\n3) other\n"
                         "Please enter your answer: ")

    input_gender = input_validator(input_gender, "std")

    input_gender_preference = input("\nWhat is your gender preference?"
                                    "\n1) male\n2) female\n3) other\n"
                                    "Please enter your answer: ")

    input_gender_preference = input_validator(input_gender_preference, "std")

    input_height = input("\nWhat is your height?"
                         "\n1) tall\n2) medium\n3) short\n"
                         "Please enter your answer: ")

    input_height = input_validator(input_height, "std")

    input_height_preference = input("\nWhat is your height preference?"
                                    "\n1) tall\n2) medium\n3) short\n"
                                    "Please enter your answer: ")

    input_height_preference = input_validator(input_height_preference, "std")

    print("\nWe will now ask you some questions to try to determine your personality type.\n")

    input_question1 = input("Do you find it easy to introduce yourself to other people?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question1 = int(input_validator(input_question1, "personality"))

    input_question2 = input("\nDo you usually initiate conversations?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question2 = int(input_validator(input_question2, "personality"))

    input_question3 = input("\nDo you often do something out of sheer curiosity?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question3 = int(input_validator(input_question3, "personality"))

    input_question4 = input("\nDo you prefer being out with a large group of "
                            "friends rather than spending time on your own?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question4 = int(input_validator(input_question4, "personality"))

    user_value = (input_question1 + input_question2 + input_question3 + input_question4) * 2
    # totalinput = [input_gender, input_gender_preference, input_height, input_height_preference, personality_value]

    converted = converter(input_gender, input_gender_preference, input_height, input_height_preference)
    # print(converted)
    final_partner = match(converted[0], converted[1], converted[2], converted[3], user_value)
    # print("your possible partners are", partners_possible)

    print("\nThank you for answering all the questions. We have found your best"
          "match from our database and hope that you enjoy getting to know"
          "each other. Your best match is:")
    if len(final_partner) == 0:
        print("none")
        return "none"
    else:
        print(final_partner[0][0])
        return final_partner[0][0]


main()
