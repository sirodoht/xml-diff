import time

def diff(left, right):
    """
    Get diff result in form of arrays.

    Accepts lines in the form of arrays.
    eg. left = ['line 1', 'line 2']

    Returns diff results in an array of tupples.
    eg. [('=', ['line 1', 'line 2']), ('+', ['line 3'])]

    Adapted from https://github.com/paulgb/simplediff
    """
    # Map that shows when each value appears on the left version.
    left_index_map = {}
    for index, value in enumerate(left):
        left_index_map.setdefault(value, []).append(index)

    overlap = {}

    substr_start_old = 0
    substr_start_new = 0
    substr_length = 0

    for index_right, value_right in enumerate(right):
        new_overlap = {}
        for index_left in left_index_map.get(value_right, []):
            # this is only for unchanged lines in the two versions
            new_overlap[index_left] = (index_left and overlap.get(index_left - 1, 0)) + 1
            if(new_overlap[index_left] > substr_length):
                # we found a new largest substring so far
                substr_length = new_overlap[index_left]
                substr_start_old = index_left - substr_length + 1
                substr_start_new = index_right - substr_length + 1
        overlap = new_overlap

    if not substr_length:
        # case when there is no overlapped string,
        # which means it's either an addition or a deletion
        return (left and [('-', left)] or []) + (right and [('+', right)] or [])
    else:
        # case when the overlapped string is unchanged,
        # so recursively diff the text before and after that string
        return diff(left[:substr_start_old], right[:substr_start_new]) + \
               [('=', right[substr_start_new: substr_start_new + substr_length])] + \
               diff(left[substr_start_old + substr_length:], right[substr_start_new + substr_length:])


def files_diff(filename_left, filename_right, print_results=False):
    """
    Given two filenames, print diff in git style.
    """
    start = time.process_time()

    with open(filename_left) as f:
        data_left = f.read()
    f.close()

    with open(filename_right) as f:
        data_right = f.read()
    f.close()

    data_left_array = data_left.split('\n')
    data_right_array = data_right.split('\n')

    diff_result = diff(data_left_array, data_right_array)

    duration = time.process_time() - start
    print('duration in ms:', duration * 1000)

    if print_results:
        for entry in diff_result:
            action = entry[0]
            lines = entry[1]
            if action == '=':
                continue
            for line in lines:
                print(action + ' ' + line)
