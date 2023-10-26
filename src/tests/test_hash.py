import pytest
import polars as pl
import polars_hash

from polars.testing import assert_frame_equal


def test_sha256():
    result = pl.select(pl.lit('hello_world').stbl_hash.sha256())
    
    expected = pl.DataFrame(
    [
        pl.Series("literal", ['35072c1ae546350e0bfa7ab11d49dc6f129e72ccd57ec7eb671225bbd197c8f1'], dtype=pl.Utf8),
    ]
)
    
    assert_frame_equal(result, expected)
    

def test_xx64():
    result = pl.select(pl.lit('hello_world').stbl_hash.xx64())
    
    expected = pl.DataFrame(
    [
        pl.Series("literal", ['5654987600477331689'], dtype=pl.Utf8),
    ]
)
    
    assert_frame_equal(result, expected)
def test_wyhash():
    result = pl.select(pl.lit('hello_world').stbl_hash.wyhash())
    
    expected = pl.DataFrame(
    [
        pl.Series("literal", ['16737367591072095403'], dtype=pl.Utf8),
    ]
)
    
    assert_frame_equal(result, expected)