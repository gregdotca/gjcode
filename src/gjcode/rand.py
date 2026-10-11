import random

default_options = 2
default_rolls = 100000
default_details = 0


def rand(options=default_options, rolls=default_rolls, details=default_details):
    """Run the main randomizer program (Return Value)"""
    sorted_results = get_sorted_results(options, rolls)

    if details:
        result_return = get_full_details(options, rolls, sorted_results)
    else:
        result_return = sorted_results[0][0]

    return result_return


def get_headers(options, rolls):
    """Get the headers"""
    headers = f"Options: {options:,}\n"
    headers += f"Rolls: {rolls:,}"
    return headers


def get_results(options, rolls):
    """Get the results"""
    count = 0
    results = {}

    while count < rolls:
        selection = random.randint(1, options)
        if selection in results:
            results[selection] += 1
        else:
            results[selection] = 1
        count += 1

    return results


def sort_results(unsorted_results):
    """Sort the results"""
    return sorted(unsorted_results.items(), key=lambda x: x[1], reverse=True)


def get_sorted_results(options, rolls):
    """Get the sorted results"""
    unsorted_results = get_results(options, rolls)
    return sort_results(unsorted_results)


def get_details(rolls, sorted_results):
    """Get the formatted details"""
    result = ""
    row_count = 0

    for each in sorted_results:
        percent = f"{each[1] * 100 / rolls:.2f}"
        row = "#" + str(each[0]) + " - " + f"{each[1]:,}" + " (" + percent + "%)"
        result += row + " -- WINNER!\n" if row_count == 0 else row + "\n"
        row_count += 1

    return result[:-1]


def get_full_details(options, rolls, sorted_results):
    """Get the full formatted details"""
    full_details = get_headers(options, rolls) + "\n\n"
    full_details += get_details(rolls, sorted_results)
    return full_details
