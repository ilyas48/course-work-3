from func import  get_all_operation, get_operation_data, get_operation_by_date, reformat_data


def main():
    data = get_all_operation()
    data = get_operation_data(data)
    data = get_operation_by_date(data)
    data = reformat_data(data)

    for row in data:
        print(row)


if __name__ == "__main__":
    main()


