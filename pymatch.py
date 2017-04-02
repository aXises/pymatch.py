"""Matches the user with potential partners based on inputs from user
The user will input values when prompted to.
Based on the values from the user, the program will attempt to match the
inputs received from the user to partners retrieved from a database.
Inputs must be numbers which will be validated by a additional function.

Algorithm:
    1: Prompt user for inputs
    2: Validate each input by passing the inputs through a function which
    checks if the input is within the specified
    range and is not a string.
    3: The validated input format will be the same as the database format.
    4: Passes the converted inputs in to the match function
    5: The match function will match the user inputs with the database and
    sort the partners personality
    difference from the user's personality value, from least to greatest.
    If there are multiple personality values which  are the name, the height
    and height preference will then be matched.
    6: The main function will return the first element from the first list,
    returned from the match function. None if the list is empty.
"""

import partners


def match(gender, genderpref, height, heightpref, user_value):
    """Matches inputs from user to potential partners from database.txt.
       Args:
           gender(str): User gender input.
           genderpref(str): User preferred gender input.
           height(str): User height input.
           heightpref(str): User preferred height input.
           user_value(str/int): User personality value, generated
           from input_questions.
       Returns:
           list: A list of all possible partners eligible according
           to the user inputs.
       Raises:
           IndexError: when data retrieved from database is greater
           than expected value
   """
    # Element position for partner attributes
    PARTNER_GENDER = 1
    PARTNER_GENDER_PREF = 2
    PARTNER_HEIGHT = 3
    PARTNER_HEIGHT_PREF = 4
    PARTNER_PERSONALITY_VALUE = 5
    # Function variables
    potential_partners = partners.Partners()
    partner_name = []
    partner_gender = []
    partner_gender_preference = []
    partner_height = []
    partner_height_preference = []
    partner_score = []
    partners_possible_list = []
    partners_equal_personality = []
    secondary_partner = []
    lowest_difference = 0
    partners_loaded = 0
    # Counter variables
    x = 0
    y = 0
    z = 0
    a = 0
    b = 0
    while potential_partners.available():
        partners_loaded += 1
        partner_name.append(potential_partners.get_name())
        partner_gender.append(potential_partners.get_gender())
        partner_gender_preference.append(potential_partners.get_sexual_pref())
        partner_height.append(potential_partners.get_height())
        partner_height_preference.append(potential_partners.get_height_pref())
        partner_score.append(potential_partners.get_personality_score())

    while x < partners_loaded:
        partner_list = [partner_name[x],
                        partner_gender[x],
                        partner_gender_preference[x],
                        partner_height[x],
                        partner_height_preference[x],
                        partner_score[x]]
        x += 1
        if partner_list[PARTNER_GENDER] == genderpref and partner_list[
           PARTNER_GENDER_PREF] == gender:
            y += 1
            partners_possible = partner_list
            partners_possible_list.append(partners_possible)

    while len(partners_possible_list) > z:
        partner_value = partners_possible_list[z][PARTNER_PERSONALITY_VALUE]
        difference = int(user_value) - int(partner_value)
        del partners_possible_list[z][5]
        partners_possible_list[z].append(abs(difference))
        z += 1

    partners_possible_list.sort(key=lambda x: x[PARTNER_PERSONALITY_VALUE])

    if len(partners_possible_list) > 0:
        lowest_difference = partners_possible_list[0][PARTNER_PERSONALITY_VALUE]

    if len(partners_possible_list) >= 2:
        while len(partners_possible_list) > a:
            if partners_possible_list[a][
                PARTNER_PERSONALITY_VALUE] == lowest_difference:
                partners_equal_personality.append(partners_possible_list[a])
            a += 1

    if len(partners_equal_personality) > 0:
        while len(partners_equal_personality) > b:
            if partners_equal_personality[b][PARTNER_HEIGHT] == heightpref:
                secondary_partner.append(partners_equal_personality[b])
                return secondary_partner
            elif partners_equal_personality[b][PARTNER_HEIGHT_PREF] == height:
                secondary_partner.append(partners_equal_personality[b])
                return secondary_partner
            else:
                return 0
            b += 1

    return partners_possible_list


def input_validator(user_inputs, typeof_question):
    """Validates user inputs to ensure that the input is valid
        Args:
            user_inputs(int): The user input.
            typeof_question(str): The type of question that will be validated.
        Returns:
            int: Returns the user's original input if the input is valid.
    """
    if typeof_question == "character":
        if str.isdigit(user_inputs) and 0 < int(user_inputs) <= 3:
            validated_input = user_inputs
            return validated_input
        else:
            while not str.isdigit(user_inputs) or 0 >= int(user_inputs) \
                    or 3 < int(user_inputs):
                user_inputs = input("Please enter a valid value:")
                validated_input = user_inputs
                if str.isdigit(user_inputs) and 0 < int(user_inputs) <= 3:
                    return validated_input

    elif typeof_question == "personality":
        if str.isdigit(user_inputs) and 0 < int(user_inputs) <= 5:
            validated_input = user_inputs
            return validated_input
        else:
            while not str.isdigit(user_inputs) or 0 >= int(user_inputs) \
                    or 5 < int(user_inputs):
                user_inputs = input("Please enter a valid value:")
                validated_input = user_inputs
                if str.isdigit(user_inputs) and 0 < int(user_inputs) <= 5:
                    return validated_input


def characteristics_question(question, answer1, answer2, answer3, answer4,
                             answer5):
    """Prompts the user for inputs
        Args:
            question(str) : The type of question that will be asked.
            answer1(str) : One possible answer to the question asked.
            answer2(str) : One possible answer to the question asked.
            answer3(str) : One possible answer to the question asked.
            answer4(str) : One possible answer to the question asked
            (personality questions only).
            answer5(str) : One possible answer to the question asked
            (personality questions only).
        Returns:
            str: Returns the answer selected by the user.
    """
    input_val = 0
    if question == "height preference":
        input_val = input("\nWhat height do you prefer your partner to be?"
                          "\n1) " + answer1 + "\n2) " + answer2 + "\n3) " +
                          answer3 + "\n"
                          "Please enter your answer: ")
        validated_input = input_validator(input_val, "character")
        return validated_input

    if answer4 == 0 and answer5 == 0:
        input_val = input("\nWhat is your " + question + "?"
                          "\n1) " + answer1 + "\n2) " + answer2 + "\n3) " +
                          answer3 + "\n"
                          "Please enter your answer: ")
        validated_input = input_validator(input_val, "character")
        if question == "gender" or question == "gender preference":
            if validated_input == "1":
                return "male"
            elif validated_input == "2":
                return "female"
            elif validated_input == "3":
                return "other"
        elif question == "height" or question == "height preference":
            if validated_input == "1":
                return "tall"
            elif validated_input == "2":
                return "medium"
            elif validated_input == "3":
                return "short"
    else:
        if question == "q1":
            input_val = input("\nDo you find it easy to introduce"
                              "yourself to other people?"
                              "\n1) " + answer1 + "\n2) " + answer2 + "\n3) "
                              + answer3 + "\n4) " + answer4 + "\n5) "
                              + answer5 + "\nPlease enter your answer: ")
        if question == "q2":
            input_val = input("\nDo you usually initiate conversations?"
                              "\n1) " + answer1 + "\n2) " + answer2 + "\n3) "
                              + answer3 +
                              "\n4) " + answer4 + "\n5) " + answer5 +
                              "\nPlease enter your answer: ")
        if question == "q3":
            input_val = input(
                "\nDo you often do something out of sheer curiosity?"
                "\n1) " + answer1 + "\n2) " + answer2 + "\n3) "
                + answer3 +
                "\n4) " + answer4 + "\n5) " + answer5 +
                "\nPlease enter your answer: ")
        if question == "q4":
            input_val = input("\nDo you prefer being out with a large group of"
                              "friends rather than spending time on your own?"
                              "\n1) " + answer1 + "\n2) " + answer2 + "\n3) "
                              + answer3 +
                              "\n4) " + answer4 + "\n5) " + answer5 +
                              "\nPlease enter your answer: ")
        validated_input = input_validator(input_val, "personality")
        return validated_input


def main():
    """Main function of the program. Called to start the program.
        Args:
            This function does not accept any arguments.
        Returns:
            str: The name of the potential partner according to the user inputs.
    """
    # Element positions for user attributes
    PARTNER_NAME = 0
    FIRST_PARTNER = 0
    USER_GENDER = 0
    USER_GENDER_PREF = 1
    USER_HEIGHT = 2
    USER_HEIGHT_PREF = 3
    PERSONALITY_VALUE = 4
    # Function variables
    input_gender = 0
    input_gender_preference = 0
    input_height = 0
    input_height_preference = 0
    question_list = ["gender", "gender preference", "height",
                     "height preference", "personality"]
    personality_question_list = ["q1", "q2", "q3", "q4"]
    personality_values = []
    # Counter variables
    x = 0
    y = 0

    print("Welcome to PyMatch")
    input_name = input("Please enter your name: ")
    print("\nHi", input_name + ".")

    #Main loop
    while len(question_list) > x:
        question_type = question_list[x]
        x += 1
        if question_type == "gender" or question_type == "gender preference":
            answer1 = "male"
            answer2 = "female"
            answer3 = "other"
            answer4 = 0
            answer5 = 0
            if question_type == "gender":
                input_gender = characteristics_question(question_type, answer1,
                                                        answer2, answer3,
                                                        answer4, answer5)
            if question_type == "gender preference":
                input_gender_preference = characteristics_question(
                    question_type, answer1, answer2, answer3, answer4,
                    answer5)

        if question_type == "height" or question_type == "height preference":
            answer1 = "tall"
            answer2 = "medium"
            answer3 = "short"
            answer4 = 0
            answer5 = 0
            if question_type == "height":
                input_height = characteristics_question(question_type, answer1,
                                                        answer2, answer3,
                                                        answer4, answer5)
            if question_type == "height preference":
                input_height_preference = characteristics_question(
                    question_type, answer1, answer2, answer3, answer4,
                    answer5)

        if question_type == "personality":
            print(
                "\nWe will now ask you some questions to try to determine your "
                "personality type.\n")
            while len(personality_question_list) > y:
                question_type = personality_question_list[y]
                y += 1
                answer1 = "Yes"
                answer2 = "Most of the time"
                answer3 = "Neutral"
                answer4 = "Some times"
                answer5 = "No"
                input_personality = characteristics_question(question_type,
                                                             answer1, answer2,
                                                             answer3, answer4,
                                                             answer5)
                personality_values.append(input_personality)

    total_inputs = [input_gender,
                    input_gender_preference,
                    input_height,
                    input_height_preference,
                    personality_values]

    user_pvalue = int(total_inputs[PERSONALITY_VALUE][0]) + \
                  int(total_inputs[PERSONALITY_VALUE][1]) + \
                  int(total_inputs[PERSONALITY_VALUE][2]) + \
                  int(total_inputs[PERSONALITY_VALUE][3])

    final_partner = match(total_inputs[USER_GENDER],
                          total_inputs[USER_GENDER_PREF],
                          total_inputs[USER_HEIGHT],
                          total_inputs[USER_HEIGHT_PREF], user_pvalue * 2)

    print("\nThank you for answering all the questions. We have found your best"
          "match from our database and hope that you enjoy getting to know"
          "each other. Your best match is:")

    if len(final_partner) == 0 or final_partner == 0:
        print("none")
        return "none"
    else:
        print(final_partner[FIRST_PARTNER][PARTNER_NAME])
        return final_partner[FIRST_PARTNER][PARTNER_NAME]


main()
