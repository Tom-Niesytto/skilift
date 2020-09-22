import skilift
import pytest

def test_line_take():
    line = skilift.Line(5)
    res = line.take(7)
    assert res == 5
    assert line.num_people == 0

def test_lift_one_bench():
    line = skilift.Line(5)
    lift = skilift.Lift(10, skilift.Quad)
    res = lift.one_bench(line)
    assert res == {'loaded': 4,'num_benches': 1, 'unloaded': 0}

@pytest.mark.parametrize('x', [
    ([]),
    (None),
    ('10')
])
def test_line_bad(x):
    line = skilift.Line(x)
    with pytest.raises(TypeError):
        res = line.take(7)


@pytest.mark.parametrize('line_size, take_num, result, remaining', [
    (0,5,0,0),
    (5,2,2,3),
    (10,0,0,10)
])
def test_line_sizes(line_size, take_num, result, remaining):
    line = skilift.Line(line_size)
    res = line.take(take_num)
    assert res == result
    assert line.num_people == remaining
