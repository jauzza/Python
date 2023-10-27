def is_valide_studentnaam(studentnaam):
    namen1 = ['danny', 'sean', 'thomas', 'marc', 'thijmen', 'maurits', 'bram', 'dean', 'soufyan', 'conrad', 'stef', 'ross', 'sylvie', 'mathieu', 'steven', 'sebastiaan', 'kaj', 'michelle']
    namen2 = ['thijmen', 'maureen', 'owen', 'demi', 'imran', 'jabir', 'casper', 'stijn', 'niels', 'norma', 'jayden', 'ahsen', 'adil', 'jesse', 'isis', 'garon']
    namen = namen1 + namen2
    for naam in namen:
        if naam==studentnaam.lower(): 
            return True
    return False





