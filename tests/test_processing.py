import pytest
from src.process_data import classify_player

def test_classification():
    assert classify_player(600, 100) == "All-Rounder"
    assert classify_player(700, 20) == "Batsman"
    assert classify_player(400, 10) == "Bowler"
    assert classify_player(None, None) == None
