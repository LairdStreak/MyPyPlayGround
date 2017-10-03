"""
Assuming this is file mymodule.py, then this string, being the
first statement in the file, will become the "mymodule" module's
docstring when the file is imported.
"""
#import hackernews
import WHEmisaryScraper as wh

def main():
    """The method's docstring"""
    wh.main()

if __name__ == "__main__":
    main()
   