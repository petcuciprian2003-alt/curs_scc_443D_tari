from app.lib.biblioteca_serbia import descriere_tara, descriere_capitala, descriere_limbi, descriere_populatie

def test_descriere_tara():
    result = descriere_tara()
    expected_result = "Serbia,oficial Republica Serbia, este o țară situată în Peninsula Balcanică, cunoscută pentru istoria sa bogată și pentru peisajele deosebite, de la campiile din nord la muntii de sud fiind astfel un important hub cultural si istoric ."
    assert result == expected_result

def test_descriere_capitala():
    result = descriere_capitala()
    expected_result = "Capitala Serbiei este Belgrad, unul dintre cele mai vechi orașe din Europa."
    assert result == expected_result

def test_descriere_limbi():
    result = descriere_limbi()
    expected_result = "Limba oficială a Serbiei este sârba, scrisă atât cu alfabetul chirilic, cât și cu cel latin."
    assert result == expected_result

def test_descriere_populatie():
    result = descriere_populatie()
    expected_result = "Serbia are o populație de aproximativ 6.8 milioane de locuitori."
    assert result == expected_result
