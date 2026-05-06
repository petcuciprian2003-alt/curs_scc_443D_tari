# Configuratie globala a proiectului
from app.lib import biblioteca_coreea as sk

TARI = {
    'coreea-de-sud': {
        'nume': 'Coreea de Sud',
    },


  
}


# Mapare tara -> biblioteca

BIBLIOTECI = {
    'coreea-de-sud': sk,
     #adauga tara> 'tara': tara
}


# Mapare tara -> template
TEMPLATE_TARA = {
    'coreea-de-sud': 'coreea.html',


}
