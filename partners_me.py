import partners

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

#print("There are", partners_loaded, "partners loaded")


def match(gender, genderpref, height, heightpref):
    x = 0
    y = 0
    while x < partners_loaded:
        partner_list = [partner_name[x],
                        partner_gender[x],
                        partner_gender_preference[x],
                        partner_height[x],
                        partner_height_preference[x],
                        partner_score[x]]
        x += 1
        #print(partner_list)
        #print(x)
        if partner_list[1] == genderpref \
                and partner_list[2] == gender \
                and partner_list[3] == heightpref \
                and partner_list[4] == height:
            y += 1
            partners_possible = partner_list
            #print("match", y)
            #print("partner",x,"was matched")
            partners_possible_list.append(partners_possible)
    return partners_possible_list


def personality_match(user_value, partners_possible):
    x = 0
    while len(partners_possible) > x:
        partner_value = partners_possible[x][5]
        difference = int(user_value) - int(partner_value)
        del partners_possible[x][5]
        partners_possible[x].append(abs(difference))
        # print(partners_possible[x])
        x += 1
    partners_possible.sort(key=lambda x: x[5])
    return partners_possible


def conversion(gender, genderpref, height, heightpref):
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


def main():
    input_name = input("Please enter your name: ")
    print("\nHi", input_name + ".")
    input_gender = input("What is your gender?"
                         "\n1) male\n2) female\n3) other\n"
                         "Please enter your answer: ")
    
    input_gender_preference = input("\nWhat is your gender preference?"
                                    "\n1) male\n2) female\n3) other\n"
                                    "Please enter your answer: ")
    
    input_height = input("\nWhat is your height?"
                         "\n1) tall\n2) medium\n3) short\n"
                         "Please enter your answer: ")
    
    input_height_preference = input("\nWhat is your height preference?"
                                    "\n1) tall\n2) medium\n3) short\n"
                                    "Please enter your answer: ")

    print("\nWe will now ask you some questions to try to determine your personality type.\n")

    input_question1 = input("Do you find it easy to introduce yourself to other people?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question2 = input("\nDo you usually initiate conversations?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question3 = input("\nDo you often do something out of sheer curiosity?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    input_question4 = input("\nDo you prefer being out with a large group of "
                            "friends rather than spending time on your own?"
                            "\n1) Yes"
                            "\n2) Most of the time"
                            "\n3) Neutral"
                            "\n4) Some times"
                            "\n5) No\n"
                            "Please enter your answer: ")

    user_value = (int(input_question1) + int(input_question2) + int(input_question3) + int(input_question4)) * 2
    #totalinput = [input_gender, input_gender_preference, input_height, input_height_preference, personality_value]

    converted = conversion(input_gender, input_gender_preference, input_height, input_height_preference)
    #print(converted)
    partners_possible = match(converted[0], converted[1], converted[2], converted[3])
    #print("your possible partners are", partners_possible)
    sorted_partners = personality_match(user_value, partners_possible)
    #print(sorted_partners)
    print("\nThank you for answering all the questions. We have found your best"
          "match from our database and hope that you enjoy getting to know"
          "each other. Your best match is:")
    if len(sorted_partners) == 0:
        print("none")
        return "none"
    else:
        print(sorted_partners[0][0])
        return sorted_partners[0][0]

main()
