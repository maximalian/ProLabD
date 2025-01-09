# **Projekta komanda**
   - Projekta izstrādātāji:
     - **Aleksandrs Popjonoks** [https://github.com/AleksandrsPo]
     - **Maksims Maļinovskis** (Maksims.Malinovskis_2@edu.rtu.lv) [https://github.com/maximalian]
     - **Jūgans Tomingass** [https://github.com/yvargg]
     - **Aleksejs Bočarovs** [https://github.com/Xizerten]
     - **Olesja Samohvalova** [https://github.com/Olesja-Samohvaalova]
     - **Viktors Nikolajevs** [https://github.com/sweetkaa]

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

- **Lietotāja prasības:**

| Nr. | Lietotāja stāsts                                                                                               | Izpildīts (Jā/Nē) | Prioritāte     | Komentārs                                                                                                                      |
|---- |----------------------------------------------------------------------------------------------------------------|-------------------|--------------- |-------------------------------------------------------------------------------------------------------------------------------|
| 1   | Lietotājs vēlas ievadīt savu vecumu, dzimumu, svaru un īpašus uztura ierobežojumus (piemēram, alerģijas vai vegānu opcijas), lai aprēķinātu ikdienas uztura vajadzības un personalizētu ēdienkartes plānu. | Jā                | Must have      | Var izmantot kategorijas un ierobežojumus produktu daudzumiem, lai atbilstu uztura prasībām. (Profile, Add details)             |
| 2   | Lietotājs vēlas rediģēt savas uztura prasības, lai pielāgotu ēdienkartes plānu mainīgām vajadzībām.              | Jā                | Must have      | Rediģēšana pieejama sadaļā. (Profile)                                                                                           |
| 3   | Lietotājs vēlas izvēlēties cenas uz produktiem no dažādiem veikaliem, lai optimizētu savas izmaksas.             | Jā                | Must have      | Pieejama cenu salīdzināšanas funkcija no Maxima un Rimi. (Result)                                                                |
| 4   | Lietotājs vēlas pārbaudīt ēdienkartes kopējās izmaksas, lai kontrolētu savu budžetu.                             | Jā                | Must have      | Izmaksu aprēķins pieejams. (Result)                                                                                              |
| 5   | Lietotājs vēlas saņemt vizualizācijas par uzturvielu sadalījumu, lai viegli analizētu datus.                     | Jā                | Should have    | Grafiskais pārskats gatavs. (Result)                                                                                             |
| 6   | Lietotājs vēlas iespēju pievienot jaunus produktus ar uzturvērtību datiem, lai paplašinātu savu izvēli.          | Jā                | Must have      | Produkta pievienošanas funkcija. (Edit products)                                                                                |
| 7   | Lietotājs vēlas pārbaudīt produkta saites derīgumu un cenas, lai garantētu datu precizitāti.                      | Jā                | Must have      | Datu atjaunināšanas sistēma darbojas. (Edit products)                                                                            |
| 8   | Lietotājs vēlas lejupielādēt ēdienkartes plānu DOCX formātā, lai to varētu izmantot bezsaistē.                   | Jā                | Could have     | Funkcija pieejama. (Result)                                                                                                    |

## 2. Algoritms

Sistēma izmanto **lineārās programmēšanas algoritmu**, lai optimizētu lietotāja ēdienkarti. Algoritms darbojas šādi:

1. **Ievaddatu apstrāde**  
   - Lietotājs ievada savus datus, tostarp vecumu, dzimumu, svaru un uztura ierobežojumus (piemēram, alerģijas vai vegānu opcijas).  
   - Dati tiek saglabāti datu bāzē turpmākai apstrādei.  

2. **Uzturvielu aprēķins**  
   - Algoritms aprēķina lietotāja ikdienas uztura vajadzības, balstoties uz ievadītajiem datiem.  
   - Atlasīti produkti, kas atbilst uzturvērtībām un budžetam, izmantojot pieejamos cenu datus no dažādiem veikaliem (piemēram, Maxima un Rimi).  

3. **Optimizācijas process**  
   - Algoritms izvēlas produktu kombināciju, kas maksimāli atbilst uzturvērtību prasībām un minimizē kopējās izmaksas.  
   - Optimizācijas rezultāti tiek validēti un pārbaudīti.  

4. **Rezultātu attēlošana**  
   - Sistēma parāda lietotājam optimizētu ēdienkarti ar uzturvielu sadalījumu un kopējām izmaksām.  
   - Lietotājs var saglabāt rezultātus DOCX formātā vai rediģēt ievades parametrus turpmākai optimizācijai.  

![Algoritma diagramma](https://github.com/maximalian/ProLabD/blob/main/Projekt%C4%93%C5%A1anas%20p%C4%81rskats/Algoritms.png)


## 3. Konceptu modelis

Konceptu modelis ietver šādus pamata elementus:
- **Lietotājs**: Sniedz datus par savām uzturvērtību prasībām, ievada īpašas prasības un pielāgo produktus.
- **Optimizācijas nosacījumi**: Ierobežojumi, kurus sistēma izmanto uztura plānošanai (alerģijas, produktu nepanesamība).
- **Ēdienkarte**: Galvenā sistēmas izeja, kur tiek parādīta optimizētā ēdienkarte, kas atbilst uzturvērtības un izmaksu nosacījumiem.
- **Produkts**: Informācija par produktu uzturvērtībām un izmaksām dažādos veikalos.
- **Veikals**: Datu avoti par produktu cenām.
- **Cena**: Informācija par optimizēto ēdiena izmaksu dažādos veikalos.
- **Uzturvērtība**: Produkta uzturvielu dati, kas tiek izmantoti optimizācijas algoritmā.

![Konceptu modelis](https://github.com/maximalian/ProLabD/blob/main/Projekt%C4%93%C5%A1anas%20p%C4%81rskats/Konceptu%20modelis.jpg)

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

![Tehnoloģiju steks](https://github.com/maximalian/ProLabD/blob/main/Projekt%C4%93%C5%A1anas%20p%C4%81rskats/Tehnolo%C4%A3iju%20steks.png)
  
## 5. Programmatūras apraksts

Programmai var piekļūt, izmantojot šādu saiti: [http://13.61.89.142/](http://13.61.89.142/)

Izstrādātā tīmekļa lietotne ir programma, kas palīdz lietotājiem plānot ikdienas ēdienkarti, pamatojoties uz uzturvērtības un izmaksu ierobežojumiem. Lietotājs ievada informāciju par savām uztura vajadzībām un pieejamajiem produktiem. Programma, izmantojot lineārās programmēšanas algoritmus, ģenerē optimālu ēdienkarti, kas atbilst lietotāja uzturvielu prasībām, vienlaikus samazinot izmaksas. Lietotājs var vizualizēt uzturvērtības grafikos, kā arī saņemt informāciju par produktu cenām dažādos veikalos.

Programma ir izstrādāta, lai būtu lietotājam draudzīga, ar intuitīvu saskarni, ātru datu apstrādi un iespēju pielāgot produktu sarakstu dinamiskā veidā.

---

## 5.1 Pieteikšanās lapa
### Funkcionalitāte:
- Lietotājs ievada savu e-pasta adresi un paroli.
- Tiek veikta lietotāja autentifikācija, izmantojot bcrypt hash algoritmu.
- Ja pieteikšanās ir veiksmīga, lietotājs tiek pāradresēts uz personalizēto profilu.

![Pieteikšanās Lapa](https://github.com/maximalian/ProLabD/blob/main/parskats/login.png)

### Kods:
- [app.py](https://github.com/maximalian/ProLabD/blob/main/app.py) - Galvenā aplikācijas konfigurācija un maršrutēšana.
  - **home()** - Atgriež galveno lapu.
- [auth_routes.py](https://github.com/maximalian/ProLabD/blob/main/auth_routes.py) - Pieteikšanās un reģistrācijas loģika.
  - **login()** - Apstrādā pieteikšanās pieprasījumus (GET un POST).
  - **register()** - Reģistrē jaunu lietotāju.
  - **logout()** - Izraksta lietotāju no sistēmas.
- [index.html](https://github.com/maximalian/ProLabD/blob/main/templates/index.html) - HTML veidne pieteikšanās lapai.
  - Satur ievades laukus e-pastam un parolei.
  - Pogas pieteikšanās un reģistrācijai.
- [styles.css](https://github.com/maximalian/ProLabD/blob/main/static/css/styles.css) - CSS stila faili lietotāja saskarnei.
  - Nodrošina dizainu ar responsīvu izkārtojumu un pogu animācijām.

---

## 5.2 Reģistrācijas lapa
### Funkcionalitāte:
- Lietotājs ievada e-pasta adresi, paroli un apstiprina paroli.
- Nodrošināta paroles redzamības pārslēgšana.
- Validē e-pasta un paroles atbilstību.
- Ja reģistrācija veiksmīga, lietotājs tiek novirzīts uz profila iestatīšanas lapu.

![Reģistrācijas Lapa](https://github.com/maximalian/ProLabD/blob/main/parskats/register.png)

### Kods:
- [auth_routes.py](https://github.com/maximalian/ProLabD/blob/main/auth_routes.py) - Reģistrācijas loģika.
  - **register()** - Apstrādā reģistrācijas pieprasījumus (GET un POST).
  - **check_email()** - Pārbauda, vai e-pasta adrese jau pastāv datubāzē, un atgriež rezultātu JSON formātā.  
- [register.html](https://github.com/maximalian/ProLabD/blob/main/templates/register.html) - HTML veidne reģistrācijas lapai.
  - Ievades lauki e-pastam, parolei un apstiprinājuma parolei.
  - Validācija un paroles redzamības pārslēgšana.
- [register.js](https://github.com/maximalian/ProLabD/blob/main/static/js/register.js) - JavaScript funkcijas reģistrācijas formas validācijai un paroles redzamības pārslēgšanai.  
  - **togglePasswordVisibility(passwordFieldId, toggleButtonId)** - Pārslēdz paroles redzamību ievades laukā, mainot tās tipu starp 'password' un 'text'.  
  - **validateForm(event)** - Validē reģistrācijas formu, pārbaudot e-pasta adreses pieejamību un paroles atbilstību apstiprinājuma laukam, pirms iesniedz datus serverim.
- [styles.css](https://github.com/maximalian/ProLabD/blob/main/static/css/styles.css) - CSS stila faili.
  - Dizains ar responsīvu izkārtojumu un animācijām.

---

## 5.3 Lietotāja dati un produktu filtrēšana
### Funkcionalitāte:
- Lietotājs ievada personas datus (vārds, uzvārds, dzimums, vecums, svars, augums).
- Lietotājs filtrē produktus pēc kategorijām un diētas prasībām (vegan, ne-vegan).
- Ir iespēja uzstādīt minimālos un maksimālos daudzumus produktiem.
- Produktus var izslēgt no aprēķina (piem., alerģiju vai nepatiku dēļ). Piemēram, ja lietotājam ir alerģija uz riekstiem, viņš var atlasīt kategoriju "Rieksti", nospiest "Exclude All Filtered" un visi atzīmētie produkti netiks ņemti vērā ēdienkartes veidošanā.
- Filtrēšanas rezultāti tiek saglabāti lietotāja profilā.
- Produktu filtrēšana:  
  - Lietotājs var atlasīt produktus pēc kategorijas (piem., augļi, dārzeņi, gaļa) un uztura prasībām (vegan, ne-vegan).  
  - Ir iespējams filtrēt produktus pēc minimālā un maksimālā daudzuma uz vienu produktu (piem., ne vairāk kā 100 g ābolu vai ne mazāk kā 10 g banānu).  
  - Lietotājs var definēt daudzuma ierobežojumus konkrētiem produktiem, ņemot vērā individuālās vajadzības vai diētas plānus.  
  - Produktu daudzumu var pielāgot, lai nodrošinātu optimālu uzturvielu līdzsvaru un ievērotu kaloriju, proteīnu, tauku un ogļhidrātu prasības.  
  - Filtrēšanas rezultāti tiek parādīti tabulā, kur lietotājs var rediģēt daudzumus vai izslēgt produktus, kas neatbilst prasībām.  



- Lietotāja datu ievade un filtri

  ![Lietotāja dati](https://github.com/maximalian/ProLabD/blob/main/parskats/details.png)
- Produktu filtrēšana piemērs

  ![Produktu filtrs](https://github.com/maximalian/ProLabD/blob/main/parskats/details_filter.png)

### Kods:
- [auth_routes.py](https://github.com/maximalian/ProLabD/blob/main/auth_routes.py) - Datu apstrādes loģika.
  - **add_details()** - Lietotāja datu pievienošana un atjaunināšana.
- [add_details.html](https://github.com/maximalian/ProLabD/blob/main/templates/add_details.html) - HTML veidne lietotāja datu ievadei.
- [product_table.js](https://github.com/maximalian/ProLabD/blob/main/static/js/product_table.js) - JavaScript funkcijas produktu filtrēšanai un ierobežojumu iestatīšanai.
  - **prepareLimits()** - Sagatavo un validē minimālos un maksimālos produktu ierobežojumus, saglabājot tos JSON formātā.  
  - **renderRows(products)** - Ģenerē un attēlo produktu rindas tabulā ar iespēju iestatīt ierobežojumus un izslēgt produktus.  
  - **applyFilters(allProducts)** - Filtrē produktus pēc kategorijas, vegānisma statusa un nosaukuma, atjaunojot tabulu ar rezultātiem.  
  - **setLimitsForFiltered()** - Uzstāda minimālos un maksimālos ierobežojumus visiem filtrētajiem produktiem, pamatojoties uz ievadītajām vērtībām.  
  - **clearLimitsForFiltered()** - Noņem minimālos un maksimālos ierobežojumus visiem filtrētajiem produktiem, neietekmējot izslēgtos produktus.  
  - **excludeFilteredProducts()** - Izslēdz filtrētos produktus no apstrādes un atjauno tabulu ar izmaiņām.  
  - **clearExcludedFilteredProducts()** - Noņem filtrēto produktu izslēgšanas statusu un atjauno tabulu ar atgrieztajiem produktiem.  
- [profile.css](https://github.com/maximalian/ProLabD/blob/main/static/css/profile.css) - CSS stila faili lietotāja saskarnei.

---

## 5.4 Aprēķinu rezultāti

### Funkcionalitāte:
- Lietotājs apskata uztura aprēķinu rezultātus, ieskaitot uzturvielu daudzumus, kalorijas un kopējās izmaksas.
- Lietotājs var salīdzināt iegūtos datus ar dienas normām.
- Vizualizācija tiek parādīta diagrammu veidā.
- Mazākās cenas tiek iezīmētas ar zaļu krāsu, lai palīdzētu lietotājiem ātri identificēt labākos piedāvājumus.
- Tabulā tiek rādīti šādi atribūti:
  - Produktu nosaukums.
  - Uzturvielu daudzumi (proteīni, tauki, ogļhidrāti, kalorijas).
  - Daudzums un vienības.
  - Cena atsevišķos veikalos (Maxima, Rimi) un kopējās izmaksas.
  - Kopējā ēdienkartes cena tiek rādīta apakšā.


### Navigācijas pogas:
- **"Back to Login"** - Atgriež lietotāju uz pieteikšanās lapu.
- **"Profile"** - Ķauj rediģēt lietotāja informāciju (vārds, vecums, dzimums) un ierobežojumus uzturvielām.
- **"Edit Products"** - Dod iespēju rediģēt esošo produktu sarakstu datubāzē.
- **"Calculate"** - Aprēķina uztura plānu un cenas, balstoties uz lietotāja izvēlētajiem veikaliem.
- **"Download as DOCX"** - Lejupielādē rezultātus DOCX faila formātā, ķaujot tos saglabāt vai izdrukāt. DOCX faila piemērs: [Arturs_Pavlovs_results.docx](https://github.com/maximalian/ProLabD/blob/main/parskats/Arturs_Pavlovs_results.docx).

### Aprēķinu rezultātu vizualizācijas:
- Kopējās aprēķinu rezultātu lapa

  ![Rezultātu lapa](https://github.com/maximalian/ProLabD/blob/main/parskats/result.png)
- Lietotāja dati

  ![Lietotāja dati](https://github.com/maximalian/ProLabD/blob/main/parskats/user_details.png)
- Aprēķinu tabula

  ![Aprēķinu tabula](https://github.com/maximalian/ProLabD/blob/main/parskats/calc_result.png)
- Dienas uzturvielu normas

  ![Uzturvielu normas](https://github.com/maximalian/ProLabD/blob/main/parskats/daily_NN.png)
- Dienas uzturvielu salīdzinājums

  ![Salīdzinājums](https://github.com/maximalian/ProLabD/blob/main/parskats/daily_NC.png)
- Izvēlētie produkti

  ![Izvēlētie produkti](https://github.com/maximalian/ProLabD/blob/main/parskats/selected_products.png)
- Veikalu izvēle un aprēķini

  ![Veikalu izvēle](https://github.com/maximalian/ProLabD/blob/main/parskats/calculate.png)
- Navigācijas pogas

  ![Navigācijas pogas](https://github.com/maximalian/ProLabD/blob/main/parskats/result_buttons.png)

### Kods:
- [DIETcalc.py](https://github.com/maximalian/ProLabD/blob/main/DIETcalc.py) - Galvenais algoritms uztura plāna aprēķināšanai.
  - **calculate_diet()** - Veido optimizācijas modeli, lai minimizētu izmaksas un nodrošinātu uzturvielu prasības.
  - Algoritms izmanto Pulp bibliotēku, lai atrisinātu lineārās programmēšanas problēmu.
- [user_routes.py](https://github.com/maximalian/ProLabD/blob/main/user_routes.py) - Funkcijas aprēķinu veikšanai un lietotāja datu apstrādei.
  - **calculate_menu()** - Aprēķina uztura plānu.
  - **update_selected_products()** - Atjauno lietotāja izvēlētos produktus.
- [result.html](https://github.com/maximalian/ProLabD/blob/main/templates/result.html) - HTML veidne aprēķinu rezultātu parādīšanai.
- [result.js](https://github.com/maximalian/ProLabD/blob/main/static/js/result.js) - JavaScript koda funkcijas vizualizācijai un validācijai.
  - **validateStoreSelection()** - Pārbauda, vai lietotājs ir izvēlējies vismaz vienu veikalu (Maxima vai Rimi) un parāda brīdinājumu, ja veikals nav izvēlēts.
  - **generateChart()** - Ģenerē uzturvielu salīdzinājuma diagrammu, vizualizējot iegūtās un dienas normas vērtības.
  - **downloadDoc()** - Ģenerē un lejupielādē DOCX dokumentu ar aprēķinu rezultātiem, iekļaujot tabulas un diagrammas no lapas satura.
  - **prepareChartImage()** - Konvertē diagrammu attēla formātā, lai to pievienotu DOCX dokumentam.
  - **exportTableToHtml()** - Izveido HTML struktūru no tabulas datiem, ko var eksportēt DOCX formātā.
  - **addChartToExport()** - Pievieno diagrammas attēlu pie eksporta datiem DOCX dokumentam.
- [result.css](https://github.com/maximalian/ProLabD/blob/main/static/css/result.css) - CSS stili rezultātu noformējumam un izkārtojumam.

---

## 5.5 Profila lapa
### Funkcionalitāte:
- Lietotājs var rediģēt savu informāciju, ieskaitot vārdu, uzvārdu, e-pastu, vecumu, augumu un svaru.
- Parole var tikt mainīta, ievadot jaunu paroli.
- Uzturvērtību ierobežojumi (minimālie un maksimālie) var tikt definēti konkrētiem produktiem.
- Produkta filtri ļauj izslēgt produktus pēc kategorijas vai vegānisma statusa.
- Ierobežojumu saglabāšana automātiski atjaunina uztura aprēķinus.

### Navigācijas pogas:
- **"Back to Results"** - Atgriež lietotāju uz rezultātu lapu.
- **"Save Changes"** - Saglabā lietotāja veiktās izmaiņas.
- **"Edit Products"** - Dod iespēju pārvaldīt produktu sarakstu datubāzē.

- Kopējais profils:

  ![Profils](https://github.com/maximalian/ProLabD/blob/main/parskats/user_profile.png)
- Lietotāja informācija:

  ![Informācija](https://github.com/maximalian/ProLabD/blob/main/parskats/user_info.png)
- Filtra piemēri:

  ![Filtri](https://github.com/maximalian/ProLabD/blob/main/parskats/profile_product_filter.png)
  
  ![Filtru ierobežojumi](https://github.com/maximalian/ProLabD/blob/main/parskats/profile_filter.png)

- Navigācijas pogas:

  ![Navigācija](https://github.com/maximalian/ProLabD/blob/main/parskats/profile_button.png)
- Jauni aprēķini pēc izmaiņām:

  ![Rezultāti](https://github.com/maximalian/ProLabD/blob/main/parskats/new_calculation_result.png)
  ![Izvēlētie produkti](https://github.com/maximalian/ProLabD/blob/main/parskats/new_celected_products.png)

### Kods:
- [user_routes.py](https://github.com/maximalian/ProLabD/blob/main/user_routes.py) - Funkcijas profila un uztura ierobežojumu atjaunināšanai.
  - **profile()** - Rediģē lietotāja profilu.
  - **update_selected_products()** - Atjauno lietotāja izvēlētos produktus.
- [profile.html](https://github.com/maximalian/ProLabD/blob/main/templates/profile.html) - HTML veidne profila rediģēšanai.
- [product_table.js](https://github.com/maximalian/ProLabD/blob/main/static/js/product_table.js) - Produkta filtru pārvaldība.
  - **prepareLimits()** - Sagatavo un validē minimālos un maksimālos produktu ierobežojumus, saglabājot tos JSON formātā.  
  - **renderRows(products)** - Ģenerē un attēlo produktu rindas tabulā ar iespēju iestatīt ierobežojumus un izslēgt produktus.  
  - **applyFilters(allProducts)** - Filtrē produktus pēc kategorijas, vegānisma statusa un nosaukuma, atjaunojot tabulu ar rezultātiem.  
  - **setLimitsForFiltered()** - Uzstāda minimālos un maksimālos ierobežojumus visiem filtrētajiem produktiem, pamatojoties uz ievadītajām vērtībām.  
  - **clearLimitsForFiltered()** - Noņem minimālos un maksimālos ierobežojumus visiem filtrētajiem produktiem, neietekmējot izslēgtos produktus.  
  - **excludeFilteredProducts()** - Izslēdz filtrētos produktus no apstrādes un atjauno tabulu ar izmaiņām.  
  - **clearExcludedFilteredProducts()** - Noņem filtrēto produktu izslēgšanas statusu un atjauno tabulu ar atgrieztajiem produktiem.  
- [profile.css](https://github.com/maximalian/ProLabD/blob/main/static/css/profile.css) - Stila faili profila lapai.

---

## 5.6 Produktu saraksta pārvaldība

### Funkcionalitāte:
- **Produktu rediģēšana**: Lietotājs var rediģēt esošo produktu sarakstu, ieskaitot nosaukumu, uzturvielu daudzumu (kalorijas, proteīni, tauki, ogļhidrāti), cenu, veikalus, vienības, kategoriju un vegānismu.
- **Kategoriju pārvaldība**:
  - Pieejama iespēja pievienot jaunas kategorijas.
  - Dzēst nevajadzīgās kategorijas.
- **Produktu pievienošana**:
  - Lietotājs var pievienot produktus pa vienam vai masveidā, izmantojot .xlsx failu.
- **Filtri**:
  - Meklēšana pēc produkta nosaukuma.
  - Filtrēšana pēc kategorijām vai vegānisma statusa.
  - Atzīmēti bojāti URL tiek izcelti sarkanā krāsā.
- **Navigācija**:
  - Pogas atgriež uz profila vai rezultātu lapām.

### Produktu pārvaldības sadaļas:
  - Galvenā pārvaldības lapa, kas apvieno visas funkcionalitātes: filtrus, kategoriju pārvaldību, datu augšupielādi un produktu sarakstu.

  ![Produktu pārvaldības lapa](https://github.com/maximalian/ProLabD/blob/main/parskats/manage_products.png)

- **Produktu tabula**:
  - Produkta īpašību (kalorijas, olbaltumvielas, tauki, ogļhidrāti, cenas, saites) rediģēšana un saglabāšana.
  - Rediģēšanas piemērs ar izceltiem nederīgiem URL sarkanā krāsā.

  ![Produktu tabula](https://github.com/maximalian/ProLabD/blob/main/parskats/manage_table.png)

- **Produktu filtrs**:
  - Lietotājs var meklēt produktus un filtrēt tos pēc noteiktiem kritērijiem (kategorija, vegānisms, bojāti URL).

  ![Produktu filtrs](https://github.com/maximalian/ProLabD/blob/main/parskats/filter_manage_product.png)

- **Kategoriju pārvaldība**:
  - Jaunas kategorijas pievienošana vai esošās kategorijas dzēšana.

  ![Kategorijas pārvaldība](https://github.com/maximalian/ProLabD/blob/main/parskats/manage_category.png)

- **Failu pārvaldība**:
  - Masveida produktu pievienošana, izmantojot .xlsx failus.

  ![Failu pārvaldība](https://github.com/maximalian/ProLabD/blob/main/parskats/manage_file.png)

- **Produktu rindas**:
  - Jaunu produktu pievienošana pa vienam vai vairākiem uzreiz.
  - Lietotājs var aizpildīt datus par produktiem, norādot nosaukumu, kalorijas, olbaltumvielas, taukus, ogļhidrātus, saites uz veikaliem, cenas un citas īpašības.
  - Ir iespēja izvēlēties kategoriju un norādīt, vai produkts ir vegānisks.
  - Pievienot produktus ar pogu **Add Product** vai dzēst tos ar pogu **Delete Table**.
  - Papildu iespēja pievienot vairākas rindas vienlaicīgi, izmantojot pogu **Add Table** vai pievienot visus produktus uzreiz ar pogu **Add All**.

  ![Produktu rinda](https://github.com/maximalian/ProLabD/blob/main/parskats/product_rows.png)
  ![Produktu rindas](https://github.com/maximalian/ProLabD/blob/main/parskats/product_rows_addTable.png)

- **Navigācijas pogas**:
  - Pāreja uz citām sadaļām (Profils vai Rezultāti).

  ![Navigācijas pogas](https://github.com/maximalian/ProLabD/blob/main/parskats/manage_products_button.png)

### Kods:
- [product_routes.py](https://github.com/maximalian/ProLabD/blob/main/product_routes.py) - Funkcijas produktu saraksta pārvaldībai:
  - **download_template()** - Lejupielādē produktu veidnes Excel failu ar aktuālajām kategorijām.
  - **download_example()** - Lejupielādē piemēra Excel failu produktu sarakstam.
  - **upload_products()** - Augšupielādē produktus no Excel faila, validē datus un pievieno tos datubāzei.
  - **manage_products()** - Attēlo visu produktu sarakstu un ļauj tos pārvaldīt.
  - **update_product()** - Atjaunina produkta informāciju, piemēram, nosaukumu, uzturvielas, cenas un saites.
  - **get_existing_names()** - Atgriež esošo produktu nosaukumus JSON formātā, lai pārbaudītu dublikātus.
  - **add_product()** - Pievieno jaunus produktus masveidā, izmantojot JSON datus.
  - **add_single_product()** - Pievieno vienu produktu, validējot datus un pārbaudot saites.
  - **delete_product()** - Dzēš konkrētu produktu pēc tā ID.
  - **add_category()** - Pievieno jaunu kategoriju ar unikālu nosaukumu un identifikatoru.
  - **delete_category()** - Dzēš norādīto kategoriju no datubāzes pēc tās ID.

- [manage_products.html](https://github.com/maximalian/ProLabD/blob/main/templates/manage_products.html) - HTML veidne produktu saraksta pārvaldībai.
- [manage_products.js](https://github.com/maximalian/ProLabD/blob/main/static/js/manage_products.js) - JavaScript funkcijas tabulas un produktu datu validācijai.
  - **deleteProduct(productId)** - Dzēš produktu pēc ID, nosūtot POST pieprasījumu serverim un apstrādājot atbildi.  
  - **saveRow(productId)** - Saglabā izmaiņas produktam, validē ievadītos datus un nosūta tos serverim.  
  - **renderRows(products)** - Ģenerē tabulas rindas katram produktam un ievieto tās HTML tabulā.  
  - **applyFilters()** - Filtrē produktus pēc nosaukuma, kategorijas, vegānisma statusa un nederīgām saitēm.  
  - **validateProduct(table, existingNames)** - Validē produkta datus, pārbaudot nosaukumu un saites.  
  - **addSingleProduct(table)** - Pievieno vienu produktu, pārbaudot validāciju un nosūtot POST pieprasījumu serverim.  
  - **addAllProducts(event)** - Pievieno vairākus produktus vienlaicīgi, validējot datus un veicot masveida augšupielādi.  
  - **setupTableActions(table)** - Inicializē pogas un darbības tabulā, piemēram, pievienošanu un dzēšanu.  
  - **sortDropdown()** - Sakārto kategoriju nolaižamajā sarakstā vērtības augošā secībā.  
  - **addCategory()** - Pievieno jaunu kategoriju, validē tās nosaukumu un saglabā to serverī.  
  - **deleteCategory()** - Dzēš izvēlēto kategoriju, pārbaudot apstiprinājumu un dzēšot no servera.  
  - **downloadTemplate()** - Lejupielādē Excel veidnes failu ar produktu struktūru.  
  - **downloadExample()** - Lejupielādē Excel faila piemēru ar produktu sarakstu.  
  - **uploadFile()** - Apstrādā lietotāja augšupielādēto Excel failu un nosūta datus serverim apstrādei.  
- [manage_products.css](https://github.com/maximalian/ProLabD/blob/main/static/css/manage_products.css) - Stila faili tabulas un produktu pārvaldības lapai.

---

## 5.7 Datu bāzes apraksts

Programma izmanto relāciju datubāzi PostgreSQL, lai glabātu lietotāju, produktu un kategoriju datus. Zemāk aprakstītas galvenās datubāzes tabulas, to struktūra un katra atribūta nozīme.

### **5.7.1 Lietotāju tabula (lietotajs)**

Tabula saglabā informāciju par lietotājiem, tostarp personīgos datus, uztura ierobežojumus un izvēles.

![Lietotāju tabula](https://github.com/maximalian/ProLabD/blob/main/parskats/lietotajs.png)

**Atribūtu apraksts:**
- **id** - Unikāls identifikators katram lietotājam (primārā atslēga).
- **vards** - Lietotāja vārds (piemēram, Anna).
- **uzvards** - Lietotāja uzvārds (piemēram, Kalniņa).
- **epasts** - E-pasta adrese lietotāja autentifikācijai un saziņai.
- **parole** - Lietotāja parole, kas tiek glabāta hash formātā drošībai.
- **auth_provider** - Norāda autentifikācijas avotu (piem., vietējā vai Google autentifikācija).
- **created_at** - Konta izveides datums un laiks.
- **dzimums** - Lietotāja dzimums (piem., vīrietis vai sieviete).
- **svars** - Lietotāja svars kilogramu formātā.
- **augums** - Lietotāja augums centimetros.
- **vecums** - Lietotāja vecums gados.
- **max_limits** - JSON objekts, kas satur maksimālos produkta daudzuma ierobežojumus uz vienu mērvienību (piem., ne vairāk kā 100 g ābolu vai 200 ml piena).  
- **min_limits** - JSON objekts, kas satur minimālos produkta daudzuma ierobežojumus uz vienu mērvienību (piem., ne mazāk kā 50 g riekstu vai 100 ml kefīra).  
- **store_preference** - Norāda lietotāja vēlamo veikalu (piem., Maxima, Rimi vai abi).
- **selected_products** - JSON saraksts ar lietotāja izvēlētajiem produktiem.

### **5.7.2 Produktu tabula (produkts)**

Tabula glabā produktu datus, tostarp uzturvērtības, cenas un saites uz veikaliem.

![Produktu tabula](https://github.com/maximalian/ProLabD/blob/main/parskats/produkts.png)

**Atribūtu apraksts:**
- **id** - Unikāls identifikators katram produktam (primārā atslēga).
- **nosaukums** - Produkta nosaukums (piem., ābols, piens).
- **kalorijas** - Produkta enerģētiskā vērtība uz kilogramu (kcal/kg).
- **olbaltumvielas** - Olbaltumvielu daudzums gramos uz kilogramu (g/kg).
- **tauki** - Tauku daudzums gramos uz kilogramu (g/kg).
- **oglhidrati** - Ogļhidrātu daudzums gramos uz kilogramu (g/kg).
- **cena_maxima** - Produkta cena veikalā Maxima.
- **cena_rimi** - Produkta cena veikalā Rimi.
- **saite_maxima** - Hipersaite uz produktu Maxima internetveikalā.
- **saite_rimi** - Hipersaite uz produktu Rimi internetveikalā.
- **meris_vieniba** - Produkta mērīšanas vienība (piem., kg, l).
- **kategorija_key** - Ārējā atslēga, kas saista produktu ar konkrētu kategoriju.
- **vegan** - Norāda, vai produkts ir vegānisks (1 - jā, 0 - nē).
- **failed_urls** - JSON saraksts ar kļūdainām saitēm, kas nav derīgas.

### **5.7.3 Kategoriju tabula (kategorijas)**

Tabula glabā informāciju par produktu kategorijām, lai grupētu produktus.

![Kategoriju tabula](https://github.com/maximalian/ProLabD/blob/main/parskats/kategorijas.png)

**Atribūtu apraksts:**
- **kategorija_key** - Unikāls identifikators katrai kategorijai (primārā atslēga).
- **nosaukums** - Kategorijas nosaukums (piem., augļi, dārzeņi, dzērieni).

### **5.7.4 Galvenās attiecības starp tabulām**
1. **Lietotājs un produkti**:
   - Lietotāja izvēlētie produkti tiek saglabāti kā JSON formāts tabulā **lietotajs** atribūtā `selected_products`.

2. **Produkti un kategorijas**:
   - Katram produktam ir svešatslēga `kategorija_key`, kas norāda uz tā kategoriju tabulā **kategorijas**.

### **5.7.5 Datu bāzes optimizācija un drošība**
- **Indeksi**:
  - Indekss uz kolonnām `id` un `kategorija_key` nodrošina ātru meklēšanu un savienošanu starp tabulām.
- **Datu validācija**:
  - Obligātie lauki nepieļauj null vērtības, lai novērstu nepilnīgus ierakstus.
- **Šifrēšana**:
  - Lietotāja paroles tiek glabātas kā hash, izmantojot bcrypt algoritmu.
- **Drošība**:
  - Datu bāze tiek aizsargāta ar lietotājvārdu un paroli.
  - Piekļuve ir iespējama tikai autorizētiem lietotājiem.

# Novērtējums

Novērtēt uztura plāna precizitāti un optimizācijas efektivitāti, balstoties uz lietotāja prasībām un produktu datiem.

## **Novērtēšanas plāns**

### **1. Ieejas mainīgie**
- **Datu apjoms (N)**: Produktu skaits datubāzē (100, 150, 175 produkti).
- **Diētas tips (V)**:
  - **A**: Dzīvnieku izcelsmes diēta (Animal-based diet) - Yes Vegan.
  - **B**: Augu izcelsmes diēta (Plant-based diet) - No Vegan.
  - **C**: Visēdāja diēta (Omnivore diet) – Visi produkti bez ierobežojumiem.

### **2. Novērtēšanas mēri**
- **Precizitāte (P, %)**: Pārbaudīt, cik labi uztura plāns atbilst kaloriju un uzturvielu prasībām.
- **Aprēķina laiks (T_A, sekundes)**: Laiks, kas nepieciešams optimizācijas algoritma izpildei.
- **Pielāgojamības ātrums (T_R, sekundes)**: Laiks, kas vajadzīgs izmaiņu veikšanai prasībās.

## **Novērtēšanas rezultāti un to analīze**

## **1. Aprēķini**

Aprēķinus detalizētāk var apskatīt, noklišķinot uz linku.
[Eksperimnetu aprēķini](https://github.com/maximalian/ProLabD/blob/main/Projekt%C4%93%C5%A1anas%20p%C4%81rskats/eksperiments.docx)

## **2. Novērtēšanas rezultāti**

| Nr. | N   | V | P (%)  | T_A (s) | T_R (s) |
|-----|-----|---|--------|---------|---------|
| 1   | 100 | A | 87.32  | 0.122   | 0.055   |
| 2   | 150 | A | 87.81  | 0.129   | 0.057   |
| 3   | 175 | A | 86.20  | 0.120   | 0.058   |
| 4   | 100 | B | 89.55  | 0.106   | 0.057   |
| 5   | 150 | B | 91.58  | 0.118   | 0.056   |
| 6   | 175 | B | 93.91  | 0.132   | 0.060   |
| 7   | 100 | C | 93.33  | 0.113   | 0.055   |
| 8   | 150 | C | 91.60  | 0.108   | 0.059   |
| 9   | 175 | C | 93.91  | 0.111   | 0.064   |

Šāda pieeja ļauj izvērtēt, kā dažādi uztura tipi un datu apjomi ietekmē optimizācijas precizitāti un ātrumu, palīdzot lietotājam pieņemt informētus lēmumus par uztura plāniem.

## **3. Novērtējuma secinājumi**

Balstoties uz novērtēšanas rezultātiem, var izdarīt šādus secinājumus:

### **3.1 Precizitāte (P, %):**
- Visēdāja diēta (**C**) uzrāda visaugstāko precizitāti ar vērtībām no **91.60% līdz 93.91%**.
- Augu izcelsmes diēta (**B**) arī uzrāda augstu precizitāti, kas palielinās, pieaugot produktu skaitam (no **89.55% līdz 93.91%**).
- Dzīvnieku izcelsmes diētai (**A**) precizitāte ir mazliet zemāka (no **86.20% līdz 87.81%**), kas varētu būt saistīts ar ierobežotāku produktu klāstu.

### **3.2 Aprēķina laiks (T_A, sekundes):**
- **Augu izcelsmes diēta (B)** ir visātrākā aprēķinu ziņā, kas liecina, ka algoritms efektīvāk pārvalda ierobežotāku datu kopu.
- **Dzīvnieku izcelsmes diēta (A)** un **visēdāja diēta (C)** uzrāda līdzīgu aprēķinu laiku, tomēr pieaug datu apjoma gadījumā mazliet lēnāk.
- Visu diētu aprēķina laiki paliek zem **0.15 sekundēm**, kas nozīmē, ka algoritms ir ātrs un piemērots reāllaika aprēķiniem.

### **3.3 Pielāgojamības ātrums (T_R, sekundes):**
- Visēdāja diēta (**C**) uzrāda nelielu pielāgošanās laika pieaugumu, palielinoties datu apjomam (līdz **0.064 sekundēm**).
- Dzīvnieku izcelsmes (**A**) un augu izcelsmes (**B**) diētām pielāgošanās ātrums saglabājas stabils ap **0.055–0.060 sekundēm**.
- Kopumā **T_R** vērtības ir ļoti zemas, kas norāda uz sistēmas spēju ātri pielāgoties izmaiņām.

### **3.4 Datu apjoma ietekme:**
- Palielinot datu apjomu (no **100 līdz 175 produktiem**), precizitāte un aprēķina laiki nedaudz mainās, bet paliek efektīvi.
- Augstākā precizitāte tiek sasniegta pie maksimālā datu apjoma, kas norāda uz algoritma spēju labi izmantot lielu datu kopu.

### **3.5 Kopējais secinājums:**
- Algoritms labi pielāgojas dažādiem uztura veidiem un datu apjomiem, nodrošinot augstu precizitāti un zemu aprēķina laiku.
- Visēdāja diēta (**C**) piedāvā vislielāko elastību un precizitāti, savukārt augu izcelsmes diēta (**B**) nodrošina visātrāko aprēķinu.
- Sistēma spēj efektīvi apstrādāt lietotāja prasības, nodrošinot reāllaika optimizāciju un ātru pielāgošanos.

# Secinājumi

1. Problēmas aktualitāte:
   - Sabalansētas un ekonomiskas ēdienkartes plānošana mūsdienās ir aktuāla problēma.
   - Šo problēmu var efektīvi risināt, izmantojot tehnoloģiskas pieejas.

2. Līdzīgo risinājumu analīze:
   - Esošie risinājumi pierāda lineārās programmēšanas modeļu efektivitāti.
   - Tiem bieži trūkst dinamiskas pielāgošanās lietotāja prasībām un datu atjaunināšanas.

3. Izstrādātais tehniskais risinājums:
   - Sistēma piedāvā intuitīvu lietotāja pieredzi un personalizētu uztura plānošanu.
   - Lineārās programmēšanas algoritms optimizē uzturvielu līdzsvaru un izmaksas.
   - Izmantotās tehnoloģijas (Python Flask, PostgreSQL, Amazon AWS) nodrošina stabilitāti un elastību.

4. Novērtēšanas rezultāti:
   - Sistēma uzrāda augstu precizitāti un zemu aprēķinu laiku dažādos scenārijos.
   - Algoritms efektīvi pielāgojas uztura plāniem un dažādiem datu apjomiem.

5. Vispārējais secinājums:
   - Izstrādātais risinājums ir dzīvotspējīgs un praktisks.
   - Tas piedāvā personalizētu un ekonomisku pieeju sabalansētas ēdienkartes plānošanai.
   - Risinājums ir gatavs turpmākai attīstībai, piemēram, jaunu uztura modeļu vai lielākas datubāzes integrācijai.

