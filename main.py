from parsers.ExcelPricesParser import ExcelPricesParser
from counters.SimpleCounter import SimpleCounter
from writers import writer_summer_2019

def main():
    # TODO: Leave parameters for arguments.
    parser = ExcelPricesParser(
        filename = "xls_input/common.xlsx", 
        author_name_col = 2, 
        course_name_col = 1, 
        cost_col = 4, 
        reward_col = 6,
        birthdate_col= 9,
        passport_seria_number_col = 10,
        passport_created_location_col = 11,
        passport_created_date_col = 12,
        ITN_col = 15,
        INILA_col = 17,
        tax_start_date_col = 16,
        position_col = 18,
        bank_requisites_col = 19,
        degree_col = 21,
        address_by_pasport_col = 13,
        telephone_number_col = 14
    )
    parse_results = parser.parse()
    counter = SimpleCounter()

    for parse_result in parse_results:
        try:
            count_result = counter.count(parse_result)
        except Exception as e:
            print(str(e))
            continue
        writer_summer_2019.write_data_to_file(parse_result, count_result)
        
if __name__ == "__main__":
    main()