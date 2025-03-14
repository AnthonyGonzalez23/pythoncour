import pytest
from unittest.mock import patch
from games.chifoumi import resultat, pcChoix, moiChoix

def test_resultat():
    # Test all possible game outcomes
    # Ties
    assert resultat('pierre', 'pierre') == "Égalité!"
    assert resultat('feuille', 'feuille') == "Égalité!"
    assert resultat('ciseaux', 'ciseaux') == "Égalité!"

    # User wins
    assert resultat('pierre', 'ciseaux') == "Vous gagnez!"
    assert resultat('feuille', 'pierre') == "Vous gagnez!"
    assert resultat('ciseaux', 'feuille') == "Vous gagnez!"

    # Computer wins
    assert resultat('pierre', 'feuille') == "L'ordinateur gagne!"
    assert resultat('feuille', 'ciseaux') == "L'ordinateur gagne!"
    assert resultat('ciseaux', 'pierre') == "L'ordinateur gagne!"

def test_pc_choix():
    # Test that pcChoix returns a valid choice
    for _ in range(100):  # Run multiple times to check randomness
        choice = pcChoix()
        assert choice in ['pierre', 'feuille', 'ciseaux']

@patch('builtins.input')
def test_moi_choix_valid(mock_input):
    # Test valid inputs
    mock_input.return_value = 'pierre'
    assert moiChoix() == 'pierre'

    mock_input.return_value = 'feuille'
    assert moiChoix() == 'feuille'

    mock_input.return_value = 'ciseaux'
    assert moiChoix() == 'ciseaux'

@patch('builtins.input')
@patch('builtins.print')
def test_moi_choix_invalid_then_valid(mock_print, mock_input):
    # Test when user first enters invalid input, then valid input
    mock_input.side_effect = ['invalid', 'pierre']
    assert moiChoix() == 'pierre'
    # Verify error message was printed
    mock_print.assert_called_once()