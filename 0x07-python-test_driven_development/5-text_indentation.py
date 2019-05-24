#!/usr/bin/python3
"""
    >>> tester.text_indentation(\"\"\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
            Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
            Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
            Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
            Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
            rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
            stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
            cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
            beatiorem! Iam ruinas videres\"\"\")
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <BLANKLINE>
    Quonam modo?
    <BLANKLINE>
    Utrum igitur tibi litteram videor an totas paginas commovere?
    <BLANKLINE>
    Non autem hoc:
    <BLANKLINE>
    igitur ne illud quidem.
    <BLANKLINE>
    Fortasse id optimum, sed ubi illud:
    <BLANKLINE>
    Plus semper voluptatis?
    <BLANKLINE>
    Teneo, inquit, finem illi videri nihil dolere.
    <BLANKLINE>
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.
    <BLANKLINE>
    Si id dicis, vicimus.
    <BLANKLINE>
    Inde sermone vario sex illa a Dipylo stadia confecimus.
    <BLANKLINE>
    Sin aliud quid voles, postea.
    <BLANKLINE>
    Quae animi affectio suum cuique tribuens atque hanc, quam dico.
    <BLANKLINE>
    Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres

"""


def text_indentation(text):
    """
    >>> tester = __import__('3-text_indentation').text_indentation

    """
    str0 = ""
    if type(text) is not str:
        raise TypeError('text must be a string')
    i = 0
    while i < (len(text)):
        if text[i] != '\n':
            str0 += text[i]
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            str0 += '\n' * 2
            i = i + 1
        i = i + 1
    print(str0, end="")
