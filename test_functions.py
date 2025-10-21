import pandas as pd
import functions as fun 


def test_similar_pair():
    information = pd.DataFrame([{
        "name_1": "Michael",
        "name_2": "Michael",
        "c1": 1.0,
        "c3.1": 1.0,
        "c3.2": 1.0,
        "c4": True,
        "c5": True
    }])
    
    output = fun.filter_pairs(information, 0.7, 0.03)
    assert not output.empty
    output_value = output.iloc[0]["bal_value"]
    assert output_value == (1.0 * 4 + 1.0 * 2 + 1.0 * 2 + 1.0 + 1.0) / 10
    
def test_different_pair():
    information = pd.DataFrame([{
        "name_1": "Vivienne",
        "name_2": "Pedro",
        "c1": 0.1,
        "c3.1": 0.1,
        "c3.2": 0.1,
        "c4": False,
        "c5": False
    }]) 
    
    output = fun.filter_pairs(information, 0.7, 0.03)
    assert output.empty
    
def test_almost_similar_pair():
    information = pd.DataFrame([{
        "name_1": "Vivianne",
        "name_2": "Viviane",
        "c1": 0.9,
        "c3.1": 0.8,
        "c3.2": 0.0,
        "c4": True,
        "c5": False
    }])
    
    output_a = fun.filter_pairs(information, 0.7, 0.03)
    assert output_a.empty
    
    output_b = fun.filter_pairs(information, 0.6, 0.03)
    assert not output_b.empty
    output_b_value = output_b.iloc[0]["bal_value"]
    assert output_b_value == (0.9 * 4 + 0.8 * 2 + 0.0 * 2 + 1.0 + 0.0) / 10
    
    
    
    