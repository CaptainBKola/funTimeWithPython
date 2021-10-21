import sys

def display(personality_type):
    print(f"Your personality type is -> {personality_type}")
def run():
    questions: list = [
        """
Question 1:
a.expend energy, enjoy groups or
b.conserve energy, enjoy one-on-one
""",
        """
Question 2:
a.more outgoing, think out loud or
b.more reserved, think to yourself
""",
        """
Question 3:
a.seek many tasks, public activities, interaction with others
b.seek private, solitary activities with quiet to concentrate
""",
        """
Question 4:
a.external, communicative, express yourself or
b.internal, reticent, keep to yourself
""",
        """
Question 5:
a.active, initiate or
b.reflective, deliberate
""",
        """
Question 6:
a.interpret literally or
b.look for meaning and possibilities
""",
        """
Question 7:
a.practical, realistic, experiential or
b.imaginative, innovative, theoretical
""",
        """
Question 8:
a.standard, usual, conventional or
b.different, novel, unique
""",
        """
Question 9:
a.focus on here-and-now or
b.look to the future, global perspective, “big picture”
""",
        """
Question 10:
a.facts, things, “what is” or
b.ideas, dreams, “what could be,” philosophical
""",
        """
Question 11:
a.logical, thinking, questioning or
b.empathetic, feeling, accommodating
""",
        """
Question 12:
a. candid, straight forward, frank or
b. tactful, kind, encouraging
""",
        """
Question 13:
a.firm, tend to criticize, hold the line or
b.gentle, tend to appreciate, conciliate
""",
        """
Question 14:
a.tough-minded, just or
b.tender-hearted, merciful
""",
        """
Question 15:
a.matter of fact, issue-oriented or
b.sensitive, people-oriented, compassionate
""",
        """
Question 16:
a. organized, orderly or
b. flexible, adaptable
""",
        """
Question 17:
a. plan, schedule or
b. unplanned, spontaneous
""",
        """
Question 18:
a.regulated, structured or
b.easygoing, “live” and “let live”
""",
        """
Question 19:
a.preparation, plan ahead or
b.go with the flow, adapt as you go
""",
        """
Question 20:
a.control, govern or
b.latitude, freedom
"""
    ]

    count_of_a: int = 0
    count_of_b: int = 0
    personality_dichotomy: str = ''
    count = 0

    for question in questions:
        answer = ''
        while not (answer == 'A' or answer == 'B'):
            count_of_a = 0
            count_of_b = 0
            try:
                answer = input(question).upper()
                if not (answer == 'A' or answer == 'B'):
                    raise ValueError("Invalid input")
            except ValueError as error:
                print(error)
            else:
                if answer == 'A':
                    count_of_a = count_of_a + 1
                if answer == 'B':
                    count_of_b = count_of_b + 1
                count = count + 1

        if count == 5:
            if count_of_a > count_of_b:
                personality_dichotomy = personality_dichotomy + 'E '
            else:
                personality_dichotomy = personality_dichotomy + 'I '
        else:
            if count == 10:
                if count_of_a > count_of_b:
                    personality_dichotomy = personality_dichotomy + 'S '
                else:
                    personality_dichotomy = personality_dichotomy + 'N '
            else:
                if count == 15:
                    if count_of_a > count_of_b:
                        personality_dichotomy = personality_dichotomy + 'T '
                    else:
                        personality_dichotomy = personality_dichotomy + 'F '
                else:
                    if count == 20:
                        if count_of_a > count_of_b:
                            personality_dichotomy = personality_dichotomy + 'J '
                        else:
                            personality_dichotomy = personality_dichotomy + 'P '

    display(personality_dichotomy)


def exit_application():
    print("Exiting application...")
    sys.exit(0)


def main():
    user_input = input("""
    Welcome to the Meyers Briggs Personality Test
    Press 1  to take test
    Press 2 to exit application -> """)
    try:
        if not (user_input == "1" or user_input == "2"):
            raise ValueError("Invalid input")
    except ValueError as error:
        print(error)
    else:
        switcher = {
            "1": run,
            "2": exit_application
        }
        return switcher.get(user_input)()


if __name__ == "__main__":
    main()