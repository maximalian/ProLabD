# Konceptu modelis:Sabalansētas ēdienkartes

```mermaid
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

    Lietotajs <--> Edienkarte : izveido un lieto
    Lietotajs --> SpecialasVajadzibas : nosaka
    SpecialasVajadzibas --> ProduktuSaraksts : ietekme
    Edienkarte <--> ProduktuSaraksts : izmanto un ietekme
    Edienkarte --> GrafiskaisAttelojums : paradit
    ProduktuSaraksts --> Produkts : satur
    ProduktuSaraksts <--> Veikals : piedava un atjauno
    ProduktuSaraksts --> GrafiskaisAttelojums : salidzinaCenas
    Produkts <-- Veikals : piedava

