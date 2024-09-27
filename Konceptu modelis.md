# Konceptu modelis:Sabalansētas ēdienkartes

classDiagram
    class Lietotajs {
        +vards : String
        +vecums : int
        +dzimums : String
        +svars : float
        +augums : float
        +uzturalerobezjojumi : String
        +alergijas : String
        +ievaditVajadzibas()
        +izveidotEdienkarti()
    }

    class ProduktuSaraksts {
        +produkti : Produkt[]
        +dinamiskaAtjaunosana()
        +salidzinatCenas()
    }

    class Edienkarte {
        +nosaukums : String
        +kalorijas : int
        +produkti : Produkt[]
        +optimizet()
    }

    class SpecialasVajadzibas {
        +nosaukums : String
        +alergijas : String
        +dietasVeids : String
    }

    class GrafiskaisAttelojums {
        +paraditUzturvielas()
        +paraditKalorijas()
        +paraditProduktusUnCenas()
    }

    class Produkts {
        +nosaukums : String
        +cena : float
        +kalorijas : int
        +uzturaVielas : String
        +svars : float
    }

    class Veikals {
        +nosaukums : String
        +adrese : String
        +iegutCenas()
    }

    Lietotajs --> Edienkarte : izveido
    Lietotajs --> SpecialasVajadzibas : nosaka
    SpecialasVajadzibas --> ProduktuSaraksts : ietekme
    Edienkarte --> ProduktuSaraksts : izmanto
    Edienkarte --> GrafiskaisAttelojums : paradit
    ProduktuSaraksts --> Produkts : satur
    ProduktuSaraksts --> GrafiskaisAttelojums : salidzinaCenas
    Produkts <-- Veikals : piedava
