import math
import logging

logging.basicConfig(filename='LineComparison_logs.log', encoding='utf-8', level=logging.DEBUG)


class Line:

    def __init__(self, line_dictionary):
        self.x1 = line_dictionary.get("x1")
        self.y1 = line_dictionary.get("y1")
        self.x2 = line_dictionary.get("x2")
        self.y2 = line_dictionary.get("y2")
        self.line_length_dict = {}

    def line_length(self):
        """
        Function to calculate line length
        """
        try:
            length = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

            self.line_length_dict.update()
            return length
        except Exception as e:
            print(e)
            logging.exception(e)

    def __eq__(self, line_object):
        return self.line_length() == line_object.line_length()

    def __gt__(self, line_object):
        return self.line_length() > line_object.line_length()

    def __lt__(self, line_object):
        return self.line_length() < line_object.line_length()


def add_line():
    """
    Function to add line
    """
    try:
        print("Enter first co-ordinates x1,y1 separated by space : ", end="")
        x1, y1 = map(int, input().split())

        print("Enter second co-ordinates x2,y2 separated by space : ", end="")
        x2, y2 = map(int, input().split())

        print("Co-ordinates of the line are (x1, y1): ({}, {}), (x2, y2): ({}, {})".format(x1, y1, x2, y2))

        line_dict = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
        line_object = Line(line_dict)

        return line_object
    except Exception as e:
        print(e)
        logging.exception(e)


if __name__ == "__main__":
    try:
        print("Enter co-ordinates of first line")
        first_line_object = add_line()
        print("Enter co-ordinates of second line")
        second_line_object = add_line()

        if first_line_object == second_line_object:
            print("Both the lines are of equal size")
        elif first_line_object > second_line_object:
            print("First line is greater than second line")
        else:
            print("Second line is greater than first line")
    except Exception as err:
        print(err)
        logging.exception(err)
