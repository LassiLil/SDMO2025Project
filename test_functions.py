import pandas as pd
from functions import filter_pairs

#pytest

def test_bal_calculation():
    """
    Tests the overall correctness of the filter_pairs function when calculating bal_value.
    """
    df = pd.DataFrame({
        "c1": [0.3, 0.7, 1.0],
        "c3.1": [0.05, 0.91, 0.123],
        "c3.2": [0.88, 0.1, 0.999],
        "c4": [False, True, False],
        "c5": [True, True, True]
    })
    
    result = filter_pairs(df, 0)
    
    expec_bal = (
        df["c1"] * 4 + df["c3.1"] * 2 + df["c3.2"] * 2 + df["c4"] + df["c5"]
    ) / 10
    
    print(expec_bal) #pytest -s
    print(result["bal_value"])
    
    pd.testing.assert_series_equal(
    result["bal_value"],
    expec_bal[result.index],
    check_names=False
)
    
def test_empty_df():
    """
    Tests passing an empty DataFrame to the filter_pairs function.
    """
    df = pd.DataFrame(columns=["c1", "c3.1", "c3.2", "c4", "c5"])
    
    result = filter_pairs(df, 0.7)
    assert result.empty
    assert list(result.columns) == ["c1", "c3.1", "c3.2", "c4", "c5", "bal_value"]
    
    
def test_t_value():
    """
    Tests if the threshold t filters correctly in the filter_pairs function.
    """
    df = pd.DataFrame({
        "c1": [0.3, 0.7, 1.0],
        "c3.1": [0.05, 0.91, 0.123],
        "c3.2": [0.88, 0.1, 0.999],
        "c4": [False, True, False],
        "c5": [True, True, True]
    })
    
    result = filter_pairs(df, 0.69)
    expected = [2]
    assert list(result.index) == expected
    
    
def test_fraud_type_t():
    """
    Tests the function filter_pairs when the threshold t has an invalid type.
    """
    df = pd.DataFrame({
        "c1": [0.9],
        "c3.1": [0.01],
        "c3.2": [0.111],
        "c4": [False],
        "c5": [False]
    })
    
    #with pytest.raises(TypeError): --> import pytest
    filter_pairs(df, "0,7")
    
    
def test_limit_t():
    """
    Tests the filtering ability of the threshold t in edge cases.
    """
    df = pd.DataFrame({
        "c1": [0.22, 0.1345, 0.888, 0.0041],
        "c3.1": [0.4445, 0.3, 0.91, 0.061],
        "c3.2": [1.0, 0.09, 0.777, 0.491],
        "c4": [False, False, True, False],
        "c5": [True, True, False, True]
    })
    
    result = filter_pairs(df, 0.48)
    
    expec_bal = (
        df["c1"] * 4 + df["c3.1"] * 2 + df["c3.2"] * 2 + df["c4"] + df["c5"]
    ) / 10
    
    print(expec_bal) 
    print(result["bal_value"])
    
    expected = [2]
    assert list(result.index) == expected
    
    result = filter_pairs(df, 0.213)
    
    print(result["bal_value"])
    
    expected = [0, 1, 2]
    assert list(result.index) == expected
    