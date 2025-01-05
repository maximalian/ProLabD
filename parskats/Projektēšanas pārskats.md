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
1. **Ievaddatu apstrāde**: Lietotājs ievada prasības un ierobežojumus, kas tiek saglabāti datu bāzē.
2. **Uzturvielu aprēķins**: Algoritms aprēķina nepieciešamās uzturvielas un produktus, kas atbilst lietotāja vajadzībām, ņemot vērā uzturvērtību un izmaksas.
3. **Optimizācijas process**: Algoritms nosaka produktu kombināciju, kas nodrošina maksimālu uzturvielu vērtību, minimizējot kopējās izmaksas.
4. **Rezultātu attēlošana**: Pēc optimizācijas lietotājam tiek parādīta ēdienkarte, kurā atspoguļoti uzturvērtību dati un kopējās izmaksas.

![Algoritma diagramma](https://github.com/maximalian/ProLabD/blob/master/parskats/algoritms.png)

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

Izstrādātā sistēma ir tīmeka lietotne, kas palīdz lietotājiem plānot ikdienas ēdienkarti, pamatojoties uz uzturvērtības un izmaksu ierobežojumiem. Lietotājs ievada informāciju par savām uztura vajadzībām un pieejamajiem produktiem. Sistēma, izmantojot lineārās programmēšanas algoritmus, ģenerē optimālu ēdienkarti, kas atbilst lietotāja uzturvielu prasībām, vienlaikus samazinot izmaksas. Lietotājs var vizualizēt uzturvērtības grafikos, kā arī saņemt informāciju par produktu cenām dažādos veikalos.

Sistēma ir izstrādāta, lai būtu lietotājam draudzīga, ar intuitīvu saskarni, ātru datu apstrādi un iespēju pielāgot produktu sarakstu dinamiskā veidā.

---

## 5.1 Pieteikšanās lapa
### Funkcionalitāte:
- Lietotājs ievada savu e-pasta adresi un paroli.
- Tiek veikta lietotāja autentifikācija, izmantojot bcrypt hash algoritmu.
- Ja pieteikšanās ir veiksmīga, lietotājs tiek pāradresēts uz personalizēto profilu.

![Pieteikšanās Lapa](https://github.com/maximalian/ProLabD/blob/master/parskats/login.png)

### Kods:
- [app.py](https://github.com/maximalian/ProLabD/blob/master/app.py) - Galvenā aplikācijas konfigurācija un maršrutēšana【51†source】.
  - Funkcija: **home()** - Atgriež galveno lapu.

- [auth_routes.py](https://github.com/maximalian/ProLabD/blob/master/auth_routes.py) - Pieteikšanās un reģistrācijas loģika【52†source】.
  - Funkcija: **login()** - Apstrādā pieteikšanās pieprasījumus (GET un POST).
  - Funkcija: **register()** - Reģistrē jaunu lietotāju.
  - Funkcija: **logout()** - Izraksta lietotāju no sistēmas.

- [index.html](https://github.com/maximalian/ProLabD/blob/master/templates/index.html) - HTML veidne pieteikšanās lapai【53†source】.
  - Satur ievades laukus e-pastam un parolei.
  - Pogas pieteikšanās un reģistrācijai.

- [styles.css](https://github.com/maximalian/ProLabD/blob/master/static/css/styles.css) - CSS stila faili lietotāja saskarnei【54†source】.
  - Nodrošina dizainu ar responsīvu izkārtojumu un pogu animācijām.

---

## 5.2 Reģistrācijas lapa
### Funkcionalitāte:
- Lietotājs ievada e-pasta adresi, paroli un apstiprina paroli.
- Nodrošināta paroles redzamības pārslēgšana.
- Validē e-pasta un paroles atbilstību.
- Ja reģistrācija veiksmīga, lietotājs tiek novirzīts uz profila iestatīšanas lapu.

![Reģistrācijas Lapa](https://github.com/maximalian/ProLabD/blob/master/parskats/register.png)

### Kods:
- [auth_routes.py](https://github.com/maximalian/ProLabD/blob/master/auth_routes.py) - Reģistrācijas loģika【79†source】.
  - Funkcija: **register()** - Apstrādā reģistrācijas pieprasījumus (GET un POST).

- [register.html](https://github.com/maximalian/ProLabD/blob/master/templates/register.html) - HTML veidne reģistrācijas lapai【80†source】.
  - Ievades lauki e-pastam, parolei un apstiprinājuma parolei.
  - Validācija un paroles redzamības pārslēgšana.

- [styles.css](https://github.com/maximalian/ProLabD/blob/master/static/css/styles.css) - CSS stila faili【81†source】.
  - Dizains ar responsīvu izkārtojumu un animācijām.

---

## 5.3 Lietotāja dati un produktu filtrēšana
### Funkcionalitāte:
- Lietotājs ievada personas datus (vārds, uzvārds, dzimums, vecums, svars, augums).
- Lietotājs filtrē produktus pēc kategorijām un diētas prasībām (vegan, ne-vegan).
- Ir iespēja uzstādīt minimālos un maksimālos daudzumus produktiem.
- Produktus var izslēgt no aprēķina (piem., alerģiju vai nepatiku dēļ). Piemēram, ja lietotājam ir alerģija uz riekstiem, viņš var atlasīt kategoriju "Rieksti", nospiest "Exclude All Filtered" un visi atzīmētie produkti netiks ņemti vērā ēdienkartes veidošanā.
- Filtrēšanas rezultāti tiek saglabāti lietotāja profilā.

- Lietotāja datu ievade un filtri

  ![Lietotāja dati](https://github.com/maximalian/ProLabD/blob/master/parskats/details.png)
- Produktu filtrēšana

  ![Produktu filtrs](https://github.com/maximalian/ProLabD/blob/master/parskats/details_filter.png)

### Kods:
- [auth_routes.py](https://github.com/maximalian/ProLabD/blob/master/auth_routes.py) - Datu apstrādes loģika【95†source】.
  - Funkcija: **add_details()** - Lietotāja datu pievienošana un atjaunināšana.
- [add_details.html](https://github.com/maximalian/ProLabD/blob/master/templates/add_details.html) - HTML veidne lietotāja datu ievadei【96†source】.
- [profile.css](https://github.com/maximalian/ProLabD/blob/master/static/css/profile.css) - CSS stila faili lietotāja saskarnei【97†source】.
- [product_table.js](https://github.com/maximalian/ProLabD/blob/master/static/js/product_table.js) - JavaScript funkcijas produktu filtrēšanai un ierobežojumu iestatīšanai【98†source】.

---

## 5.4 Aprēķinu rezultāti

### Funkcionalitāte:
- Lietotājs apskata uztura aprēķinu rezultātus, ieskaitot uzturvielu daudzumus, kalorijas un kopējās izmaksas.
- Lietotājs var salīdzināt iegūtos datus ar dienas normām.
- Vizualizācija tiek parādīta diagrammu veidā.
- Ir iespēja lejupielādēt rezultātus DOCX formātā, izmantojot pogu **"Download as DOCX"**.
- Lietotāji var izvēlēties, no kuriem veikaliem (piem., Maxima, Rimi) iegūt cenu informāciju, izmantojot pogu **"Calculate"**.

### Navigācijas pogas:
- **"Back to Login"** - Atgriež lietotāju uz pieteikšanās lapu.
- **"Profile"** - Ķauj rediģēt lietotāja informāciju (vārds, vecums, dzimums) un ierobežojumus uzturvielām.
- **"Edit Products"** - Dod iespēju rediģēt esošo produktu sarakstu datubāzē.
- **"Calculate"** - Aprēķina uztura plānu un cenas, balstoties uz lietotāja izvēlētajiem veikaliem.
- **"Download as DOCX"** - Lejupielādē rezultātus DOCX faila formātā, ķaujot tos saglabāt vai izdrukāt. DOCX faila piemērs: [Arturs_Pavlovs_results.docx](https://github.com/maximalian/ProLabD/blob/master/parskats/Arturs_Pavlovs_results.docx).

### Aprēķinu rezultātu vizualizācijas:
- Kopējās aprēķinu rezultātu lapa

  ![Rezultātu lapa](https://github.com/maximalian/ProLabD/blob/master/parskats/result.png)
- Lietotāja dati

  ![Lietotāja dati](https://github.com/maximalian/ProLabD/blob/master/parskats/user_details.png)
- Aprēķinu tabula

  ![Aprēķinu tabula](https://github.com/maximalian/ProLabD/blob/master/parskats/calc_result.png)
- Dienas uzturvielu normas

  ![Uzturvielu normas](https://github.com/maximalian/ProLabD/blob/master/parskats/daily_NN.png)
- Dienas uzturvielu salīdzinājums

  ![Salīdzinājums](https://github.com/maximalian/ProLabD/blob/master/parskats/daily_NC.png)
- Izvēlētie produkti

  ![Izvēlētie produkti](https://github.com/maximalian/ProLabD/blob/master/parskats/selected_products.png)
- Veikalu izvēle un aprēķini

  ![Veikalu izvēle](https://github.com/maximalian/ProLabD/blob/master/parskats/calculate.png)
- Navigācijas pogas

  ![Navigācijas pogas](https://github.com/maximalian/ProLabD/blob/master/parskats/result_buttons.png)

### Kods:
- [DIETcalc.py](https://github.com/maximalian/ProLabD/blob/master/DIETcalc.py) - Galvenais algoritms uztura plāna aprēķināšanai【147†source】.
  - Funkcija: **calculate_diet()** - Veido optimizācijas modeli, lai minimizētu izmaksas un nodrošinātu uzturvielu prasības.
  - Algoritms izmanto Pulp bibliotēku, lai atrisinātu lineārās programmēšanas problēmu.
- [user_routes.py](https://github.com/maximalian/ProLabD/blob/master/user_routes.py) - Funkcijas aprēķinu veikšanai un lietotāja datu apstrādei【120†source】.
  - Funkcija: **calculate_menu()** - Aprēķina uztura plānu.
  - Funkcija: **update_selected_products()** - Atjauno lietotāja izvēlētos produktus.
- [result.html](https://github.com/maximalian/ProLabD/blob/master/templates/result.html) - HTML veidne aprēķinu rezultātu parādīšanai【121†source】.
- [result.js](https://github.com/maximalian/ProLabD/blob/master/static/js/result.js) - JavaScript koda funkcijas vizualizācijai un validācijai【122†source】.
  - Funkcija: **validateStoreSelection()** - Pārbauda veikalu izvēli.
  - Grafiku vizualizācijas izveide un eksportēšana DOCX formātā.
- [result.css](https://github.com/maximalian/ProLabD/blob/master/static/css/result.css) - CSS stili rezultātu noformējumam un izkārtojumam.

### Papildu funkcionalitāte:
- Mazākās cenas tiek iezīmētas ar zaļu krāsu, lai palīdzētu lietotājiem ātri identificēt labākos piedāvājumus.
- Tabulā tiek rādīti šādi atribūti:
  - Produktu nosaukums.
  - Uzturvielu daudzumi (proteīni, tauki, ogļhidrāti, kalorijas).
  - Daudzums un vienības.
  - Cena atsevišķos veikalos (Maxima, Rimi) un kopējās izmaksas.
  - Kopējā ēdienkartes cena tiek rādīta apakšā.

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
  ![Profils](https://github.com/maximalian/ProLabD/blob/master/parskats/user_profile.png)
- Lietotāja informācija:
  ![Informācija](https://github.com/maximalian/ProLabD/blob/master/parskats/user_info.png)
- Filtra piemēri:
  ![Filtri](https://github.com/maximalian/ProLabD/blob/master/parskats/profile_product_filter.png)
  ![Filtru ierobežojumi](https://github.com/maximalian/ProLabD/blob/master/parskats/profile_filter.png)
- Navigācijas pogas:
  ![Navigācija](https://github.com/maximalian/ProLabD/blob/master/parskats/profile_button.png)
- Jauni aprēķini pēc izmaiņām:
  ![Rezultāti](https://github.com/maximalian/ProLabD/blob/master/parskats/new_calculation_result.png)
  ![Izvēlētie produkti](https://github.com/maximalian/ProLabD/blob/master/parskats/new_celected_products.png)

### Kods:
- [user_routes.py](https://github.com/maximalian/ProLabD/blob/master/user_routes.py) - Funkcijas profila un uztura ierobežojumu atjaunināšanai.
  - Funkcija: **profile()** - Rediģē lietotāja profilu.
  - Funkcija: **update_selected_products()** - Atjauno lietotāja izvēlētos produktus.
- [profile.html](https://github.com/maximalian/ProLabD/blob/master/templates/profile.html) - HTML veidne profila rediģēšanai.
- [product_table.js](https://github.com/maximalian/ProLabD/blob/master/static/js/product_table.js) - Produkta filtru pārvaldība.
- [profile.css](https://github.com/maximalian/ProLabD/blob/master/static/css/profile.css) - Stila faili profila lapai.


