# Ievads

## 1. Problēmas nostādne
Sabiedrībā pieaug nepieciešamība pēc veselīga un ekonomiska uztura plānošanas, kas atbilstu katra indivīda uzturvielu prasībām, vienlaikus samazinot izmaksas. Sabalansētas ēdienkartes plānošana ir komplekss uzdevums, kas prasa efektīvu uzturvērtību un izmaksu optimizāciju.

## 2. Darba un novērtēšanas mērķis
Projekta mērķis ir izstrādāt risinājumu, kas palīdz minimizēt ēdiena izmaksas, ņemot vērā cilvēkam ikdienā nepieciešamo uzturvērtības ierobežojumus. Risinājumam jābūt lietotājam draudzīgam, spējīgam pielāgoties individuālām prasībām un nodrošināt sabalansētu uzturu.

# Līdzīgo risinājumu pārskats

## 1. Līdzīgi tehniskie risinājumi

Šeit tiek izvērtēti līdzīgie risinājumi, kas nodrošina sabalansētu ēdienkartes plānošanu, izmantojot dažādus algoritmus un programmatūras risinājumus.

### 1.1. The Diet Problem
- **Saite:** [The Diet Problem](https://www.slideshare.net/santttosh/the-diet-problem)
- **Apraksts:** Šajā risinājumā tiek izmantota lineārā programmēšana, lai samazinātu uztura izmaksas, ņemot vērā uzturvielu ierobežojumus un produktu izmaksas. Modelis balstās uz ievades datiem un izmanto vienkāršotus pieņēmumus, kuri neņem vērā produktu dinamiku un mainīgās uztura prasības.

### 1.2. Diet Models with Linear Goal Programming
- **Saite:** [Impact of Achievement Functions](https://www.nature.com/articles/ejcn201556)
- **Apraksts:** Šis risinājums paplašina klasiskos uztura modeļus, izmantojot lineārās mērķa programmēšanas funkcijas, kas ļauj ņemt vērā vairākus faktorus, piemēram, izmaksas un uzturvielu līdzsvaru. Tas ir sarežģītāks nekā klasiskie modeļi, jo tas nodrošina lielāku elastību un pielāgošanās spēju atbilstoši mainīgajiem nosacījumiem.

### 1.3. A Review of the Use of Linear Programming to Optimize Diets
- **Saite:** [Linear Programming to Optimize Diets](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6021504/)
- **Apraksts:** Šis risinājums sniedz pārskatu par lineārās programmēšanas pielietošanu uztura optimizācijā, pievēršot uzmanību uzturvielu, ekonomiskajiem un vides faktoriem. Risinājums piedāvā daudzveidīgas iespējas, piemēram, pielāgojamību dažādiem mērķiem un ierobežojumiem, tai skaitā produktu pieejamību un lietotāju vēlmēm.

### 1.4. Powell Allocation Covering Blending Constraints
- **Saite:** [Powell Allocation](https://web.fe.up.pt/~mac/ensino/docs/OR/otherDocs/PowellAllocationCoveringBlendingConstraints.pdf)
- **Apraksts:** Šis risinājums koncentrējas uz resursu sadali un sajaukšanas ierobežojumiem, izmantojot matemātiskās optimizācijas metodes. Galvenā atšķirība no citiem risinājumiem ir sarežģītāku ierobežojumu un pieņēmumu izmantošana, kas ļauj modelim pielāgoties dažādiem apstākļiem, piemēram, resursu apvienošanai optimālam rezultātam.

## 2. Novērojumu apkopojums tabulā

| Risinājuma nosaukums                                             | Algoritms                         | Funkcionalitāte                      | Priekšrocības                             |
|------------------------------------------------------------------|-----------------------------------|--------------------------------------|-------------------------------------------|
| The Diet Problem                                                 | Lineārā programmēšana             | Minimālas izmaksas, uzturvērtības    | Vienkāršs modelis, viegli ieviešams       |
| Diet Models with Linear Goal Programming                         | Lineārā programmēšana             | Uzturvērtības un izmaksu līdzsvarošana | Mērķu pielāgošana, elastīga pieeja        |
| A Review of the Use of Linear Programming to Optimize Diets      | Lineārā programmēšana             | Uzturvielām, ekonomiski un ekoloģiski līdzsvarots uzturs | Pielāgojamība un daudzveidība            |
| Powell Allocation Covering Blending Constraints                  | Alokācijas un sajaukšanas algoritmi | Resursu optimizācija                 | Sarežģīta optimizācija, daudzpusīgums     |

## 3. Intelektuālo algoritmu pārskats

Līdzīgie risinājumi parasti izmanto lineāro programmēšanu, kas ir plaši pielietots algoritms uztura plānošanā. Šo algoritmu mērķis ir optimizēt pārtikas produktu izvēli, samazinot izmaksas un ievērojot uzturvielu ierobežojumus. Mērķa programmēšana nodrošina iespēju sasniegt vairākus mērķus vienlaikus un pielāgot risinājumu konkrētām vajadzībām, piedāvājot lielāku elastību un precizitāti.

Šis pārskats sniedz padziļinātu ieskatu līdzīgos tehniskajos risinājumos, kas var kalpot par pamatu efektīvas sabalansētas ēdienkartes plānošanai.

# Tehniskais risinājums

## 1. Prasības

Sistēmas prasības tiek sadalītas vairākās galvenajās kategorijās: funkcionālās, nefunkcionālās un lietotāja prasības.

- **Funkcionālās prasības:**
1. Lietotājam jāspēj ievadīt personīgo informāciju, piemēram, vecumu, dzimumu, svaru un produktu prasības.
2. Sistēmai jānodrošina iespēja ievadīt un atjaunināt produktu uzturvērtības (olbaltumvielas, tauki, ogļhidrāti, kalorijas u.c.) un cenas.
3. Jānodrošina iespēja optimizēt ēdienkarti, pamatojoties uz uzturvielu un cenu datiem, ievērojot lietotāja norādītos ierobežojumus.
4. Jānodrošina iespēja dinamiski atjaunināt pieejamo produktu sarakstu, piemēram, mainot produktus.
5. Jānodrošina uzturvielu grafiskā vizualizācija, parādot olbaltumvielu, tauku, ogļhidrātu un kaloriju vērtības lietotāja ēdienkartē.
6. Jānodrošina iespēja lietotājam sekot līdzi cenu izmaiņām dažādos veikalos.

- **Nefunkcionālās prasības:**
1. Sistēmai jābūt pieejamai kā tīmekļa lietotnei, nodrošinot lietojamību jebkurā laikā un no jebkuras vietas.
2. Datu bāzes struktūrai jābūt optimizētai ātrai meklēšanai un datu apstrādei.
3. Sistēmai jābūt drošai, nodrošinot lietotāju datu aizsardzību un privātumu.
4. Lietotāja interfeisam jābūt intuitīvam un viegli lietojamam.

## Lietotāja prasības

| Nr. | Lietotāju stāsts                                                              | Prioritāte     |
|---- |------------------------------------------------------------------------------ |--------------- |
| 1   | Lietotājs vēlas ievadīt savu vecumu, dzimumu un svaru, lai aprēķinātu ikdienas uztura vajadzības un personalizētu ēdienkartes plānu. | Must have      |
| 2   | Lietotājs vēlas rediģēt savas uztura prasības, lai pielāgotu ēdienkartes plānu mainīgām vajadzībām. | Must have      |
| 3   | Lietotājs vēlas sekot līdzi uzturvielu patēriņam, lai nodrošinātu sabalansētu uzturu. | Must have      |
| 4   | Lietotājs vēlas pārbaudīt ēdienkartes kopējās izmaksas, lai kontrolētu savu budžetu. | Must have      |
| 5   | Lietotājs vēlas saņemt vizualizācijas par uzturvielu sadalījumu, lai viegli analizētu datus. | Should have    |
| 6   | Lietotājs vēlas iespēju pievienot jaunus produktus ar uzturvērtību datiem, lai paplašinātu savu izvēli. | Must have      |
| 7   | Administrators vēlas pievienot un rediģēt produktu datus, lai uzturētu aktuālu datu bāzi. | Must have      |
| 8   | Administrators vēlas pārbaudīt produkta saites derīgumu un cenas, lai garantētu datu precizitāti. | Must have      |
| 9   | Lietotājs vēlas pievienot īpašus uztura ierobežojumus, piemēram, alerģijas vai vegānu opcijas. | Should have    |


## 2. Algoritms

Sistēma izmanto **lineārās programmēšanas algoritmu**, lai optimizētu lietotāja ēdienkarti. Algoritms darbojas šādi:
1. **Ievaddatu apstrāde**: Lietotājs ievada prasības un ierobežojumus (uzturvielu un cenu dati), kas tiek saglabāti datu bāzē.
2. **Uzturvielu aprēķins**: Algoritms aprēķina nepieciešamās uzturvielas un produktus, kas atbilst lietotāja vajadzībām, ņemot vērā uzturvērtību un izmaksas.
3. **Optimizācijas process**: Algoritms nosaka produktu kombināciju, kas nodrošina maksimālu uzturvielu vērtību, minimizējot kopējās izmaksas.
4. **Rezultātu attēlošana**: Pēc optimizācijas lietotājam tiek parādīta ēdienkarte, kurā atspoguļoti uzturvērtību dati un kopējās izmaksas.

## 3. Konceptu modelis

Konceptu modelis ietver šādus pamata elementus:
- **Lietotājs**: Sniedz datus par savām uzturvērtību prasībām, ievada īpašas prasības un pielāgo produktus.
- **Optimizācijas nosacījumi**: Ierobežojumi, kurus sistēma izmanto uztura plānošanai (alerģijas, produktu nepanesamība).
- **Ēdienkarte**: Galvenā sistēmas izeja, kur tiek parādīta optimizētā ēdienkarte, kas atbilst uzturvērtības un izmaksu nosacījumiem.
- **Produkts**: Informācija par produktu uzturvērtībām un izmaksām dažādos veikalos.
- **Veikals**: Datu avoti par produktu cenām.
- **Cena**: Informācija par optimizēto ēdiena izmaksu dažādos veikalos.
- **Uzturvērtība**: Produkta uzturvielu dati, kas tiek izmantoti optimizācijas algoritmā.

![Konceptu modelis](https://github.com/maximalian/ProLabD/blob/main/parskats/Konceptu%20modelis.jpg)

## 4. Tehnoloģiju steks

Tehnoloģiju steks, kas tiks izmantots risinājuma implementācijai, sastāv no šādiem komponentiem:

- **Satvars**: Python Flask – tīmekļa lietotnes apstrādei servera pusē.
- **Programmēšanas valoda**:
  - **Python** – risinājuma loģikas un funkcionalitātes izstrādei.  
  - **JavaScript** – dinamiskai lietotāja saskarnes funkcionalitātei un mijiedarbībai ar serveri.  
  - **HTML** – satura un struktūras izveidei tīmekļa lietotnei.  
  - **CSS** – dizaina un izkārtojuma pielāgošanai lietotāja saskarnē.  
- **Datu bāze**: PostgreSQL – datu glabāšanai un pārvaldībai.
- **Tīmekļa serveris**: nginx – tīmekļa lietotnes apkalpošanai un pieejamības nodrošināšanai.
- **Operētājsistēma**: Ubuntu – servera operētājsistēma, kas nodrošina stabilu vidi lietotnes darbībai.
- **Virtualizācija**: Amazon AWS (EC2) – virtualizācijas risinājums, kas nodrošina elastību un drošību serveru vadībā.

![Tehnoloģiju steks](https://github.com/maximalian/ProLabD/blob/master/parskats/Tehnolo%C4%A3iju%20steks.png)
  
## 5. Programmatūras apraksts

Izstrādātā sistēma ir tīmekļa lietotne, kas palīdz lietotājiem plānot ikdienas ēdienkarti, pamatojoties uz uzturvērtības un izmaksu ierobežojumiem. Lietotājs ievada informāciju par savām uztura vajadzībām un pieejamajiem produktiem. Sistēma, izmantojot lineārās programmēšanas algoritmus, ģenerē optimālu ēdienkarti, kas atbilst lietotāja uzturvielu prasībām, vienlaikus samazinot izmaksas. Lietotājs var vizualizēt uzturvērtības grafikos, kā arī saņemt informāciju par produktu cenām dažādos veikalos.

Sistēma ir izstrādāta, lai būtu lietotājam draudzīga, ar intuitīvu saskarni, ātru datu apstrādi un iespēju pielāgot produktu sarakstu dinamiskā veidā.
