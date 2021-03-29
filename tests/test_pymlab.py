from src import pymlab
import pytest


@pytest.fixture
def mh() -> pymlab.MATLABHandler:
    return pymlab.MATLABHandler("MATLAB42")


def test_workspace_int(mh):
    assert mh.eval("y=42") == None
    assert mh.eval("y", nargout=1) == 42


def test_workspace_str(mh):
    assert mh.eval("y='s'") == None
    assert mh.eval("y", nargout=1) == "s"


def test_change_dir_windows(mh):
    assert mh.eval_args("cd", "'c:'") == None
    assert mh.eval("pwd", nargout=1) == "C:\\"


def test_transpose(mh):
    assert mh.eval_args("sum", "[1;2;3]'", nargout=1) == 6
    assert mh.eval_args("sum", "[1,2,3]'", nargout=1) == 6
    assert mh.eval_args("sum", "[1 2 3]", nargout=1) == 6
    assert mh.eval_args("sum", [1, 2, 3], nargout=1) == 6


def test_eval_string(mh):
    expected = "cd('c:')"
    result = mh.make_eval_string("cd", "'c:'", include_semicolon=False)
    assert expected == result
    expected = "cd('c:');"
    result = mh.make_eval_string("cd", "'c:'", include_semicolon=True)
    assert expected == result
    expected = "cd('c:');"
    result = mh.make_eval_string("cd", '"c:"', include_semicolon=True)
