# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask

from iifl.holding import get_iifl_client, iiflholdings

home = Flask(__name__)


@home.route("/")
def hello():
    return "hellloedea world"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    home.run(debug=True)
    #get_iifl_client()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
