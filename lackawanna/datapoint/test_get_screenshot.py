__author__ = 'allyjweir'
from web_import import get_screenshot

def main():
    file = get_screenshot("http://google.com")
    print file

main()
