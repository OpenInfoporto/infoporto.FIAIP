from xml.dom import minidom
from urllib2 import urlopen


class dataFetcher():

    def __init__(self, url):
        self.url = "http://62.149.166.102/agenzia_xml/fc86110a489b4c71a73a6abfb2286556.xml"

        self.fields = ['id_agenzia','rif','contratto','data','cod_regione','regione','cod_provincia',
            'provincia','sigla_provincia','cod_comune','comune','cod_istat','cod_zona_comune','localita',
            'ubicazione','indirizzo','civico','latitudine','longitudine','mappa_visibile','mappa_immobile_visibile',
            'cod_tipologia','tipologia','cod_categoria','testo','testo_eng','testo_ted','testo_fra','testo_rus',
            'prezzo','trattativa_riservata','mq','vani','camere','bagni','cod_condizioni','condizioni',
            'cod_riscaldamento','riscaldamento','classe_energetica','epi','epi_um','cod_cucina','cucina',
            'garage','garage_mq','ascensore','arredato','condizionatore','giardino','giardino_tipo','giardino_mq',
            'postoauto','postoauto_mq','balcone','balcone_mq','terrazza','terrazza_mq','mansarda','mansarda_mq',
            'cantina','cantina_mq','piano','piani_totali','distanza_mare','evidenza','sitoweb','agente',
            'prestigio','rent_tobuy','permuta','asta','investimento','tipo_incarico','note_riservate',
            'note_condivise','anno_immobile','livelli_immobile','unita_immobile','vista_mare','spese_condominiali',
            'email','titolo1','url1','titolo2','url2','titolo3','url3','titolo4','url4','titolo5','url5',
            'titolo6','url6','titolo7','url7','titolo8','url8','titolo9','url9','titolo10','url10',
            'titolo11','url11','titolo12','url12','trattativa_riservata']

    def connectAndGet(self):
        xmldoc = minidom.parse(urlopen(self.url))
        properties = xmldoc.getElementsByTagName('immobile')
        return properties

    def getElements(self, properties):
        elements = []
        for p in properties:
            element = {}
            for f in self.fields:
                try:
                    element[f] = p.getElementsByTagName(f)[0].childNodes[0].nodeValue
                except:
                    element[f] = ""

            elements.append(element)

        return elements

