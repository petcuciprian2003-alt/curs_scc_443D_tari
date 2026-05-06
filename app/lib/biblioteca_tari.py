# Configuratie globala a proiectului
from app.lib import biblioteca_belgia as belg

TARI = {
    'belgia': {
        'nume': 'Belgia',
    },


  
}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'belgia': belg,
     #adauga tara> 'tara': tara
}


# Mapare tara -> template
TEMPLATE_TARA = {
    'belgia': 'belgia.html',


}
