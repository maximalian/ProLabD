# Konceptu modelis:Sabalansētas ēdienkartes
```mermaid
classDiagram
    class Lietotajs {
        +vards : String
        +uzturaIerobezojumi : String
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
    }

    class Produkts {
        +nosaukums : String
        +cena : float
        +kalorijas : int
        +uzturaVielas : String
    }

    Lietotajs --> Edienkarte : izveido
    Lietotajs --> SpecialasVajadzibas : nosaka
    SpecialasVajadzibas --> ProduktuSaraksts : ietekme
    Edienkarte --> ProduktuSaraksts : izmanto
    Edienkarte --> GrafiskaisAttelojums : paradit
    ProduktuSaraksts --> Produkts : satur
    ProduktuSaraksts --> GrafiskaisAttelojums : salidzinaCenas
