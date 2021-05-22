from scrappers import get_generali_quotes, get_nn_quotes, get_investors_quotes

nn = [
    'NN (L) Obligacji Plus (dawniej NN (L) Krótkoterminowych Obligacji Plus)',
    'ING Pakiet Ostrożny'
]

investors = [
    'Investor Oszczędnościowy',
    'Investor Quality',
    'Investor Top 25 Małych Spółek'
]

generali = [
    'Generali Akcji: Megatrendy',
    'Generali Korona Dochodowy'
]

print(get_nn_quotes(nn))
print(get_investors_quotes(investors))
print(get_generali_quotes(generali))