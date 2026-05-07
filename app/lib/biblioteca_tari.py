# Configuratie globala a proiectului

#from app.lib import biblioteca_<tara_mea> as prescurtare_tara_mea 
from app.lib import biblioteca_belgia as belg

TARI = {
    'belgia': {
        'nume': 'Belgia',
    },
    #adauga  'tara_mea': { 'nume': 'Nume Tara Mea'}

}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'belgia': belg,
     #adauga 'tara_mea': prescurtare_tara_mea
}


