from parsers.ExcelPricesParser import ExcelPricesParser
from counters.SimpleCounter import SimpleCounter

def main():
    # TODO: Leave parameters for arguments.
    parser = ExcelPricesParser("common.xlsx", 2, 1, 4)
    parse_results = parser.parse()

    counter = SimpleCounter()

    for parse_result in parse_results:
        print(counter.get_course_model(parse_result))

if __name__ == "__main__":
    main()