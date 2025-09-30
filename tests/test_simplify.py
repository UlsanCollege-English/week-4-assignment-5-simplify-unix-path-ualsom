from src.simplify import simplify_path

def test_examples():
    assert simplify_path("/home/") == "/home"
    assert simplify_path("/a/./b/../../c/") == "/c"
    assert simplify_path("/a//b////c/d//././/..") == "/a/b/c"

def test_root_and_up_moves():
    assert simplify_path("/") == "/"
    assert simplify_path("/../") == "/"

def test_edge_many_slashes_and_trailing():
    assert simplify_path("/a///b////c///") == "/a/b/c"

def test_edge_many_parent_ups_beyond_root():
    assert simplify_path("/../../../../") == "/"

def test_long_nested_path_with_mixed_segments():
    p = "/home//user/./projects/../projects/python/./.././ds///week4/../../notes/././../"
    assert simplify_path(p) == "/home/user/projects"
