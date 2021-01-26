def hour_overlap(hour):
    assert isinstance(hour, int)
    assert 1 <= hour <= 12
    mins = None
    secs = None
    angle = None

    mins = int(round(30 * hour / 5.5))
    secs = int(abs(30 * hour / 5.5 - mins) * 60)
    angle = int(6 * 30 * hour / 5.5)
    if mins >= 60:
        hour = hour + 1
        mins = mins - 60
    return {
        "hours": hour, 
        "mins": mins,
        "secs": secs,
        "min_angle": angle
    }

def test_dict_instance():
    try:
        res = hour_overlap(1)
        assert isinstance(res, dict)
    except AssertionError as e:
        print("Oh, snap! the test has failed. exception: {}").format(e)


def your_test_one():
    try:
        res = hour_overlap(1)
        assert res['mins'] == 5
        print("Test 1 is passed")
    except AssertionError as e:
        print("Test 1 has failed.")
    


def your_test_two():
    try:
        res = hour_overlap(2)
        assert res['mins'] == 11
        print("Test 2 is passed")
    except AssertionError as e:
        print('Test 2 is failed')


if __name__ == '__main__':
    for i in range(1, 12):
        print(hour_overlap(i))

    test_dict_instance()
    your_test_one()
    your_test_two()