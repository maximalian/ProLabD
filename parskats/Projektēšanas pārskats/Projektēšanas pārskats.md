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

Programmai var piekļūt, izmantojot šādu saiti: [http://13.61.89.142/](http://13.61.89.142/)

Izstrādātā tīmekļa lietotne ir programma, kas palīdz lietotājiem plānot ikdienas ēdienkarti, pamatojoties uz uzturvērtības un izmaksu ierobežojumiem. Lietotājs ievada informāciju par savām uztura vajadzībām un pieejamajiem produktiem. Programma, izmantojot lineārās programmēšanas algoritmus, ģenerē optimālu ēdienkarti, kas atbilst lietotāja uzturvielu prasībām, vienlaikus samazinot izmaksas. Lietotājs var vizualizēt uzturvērtības grafikos, kā arī saņemt informāciju par produktu cenām dažādos veikalos.

Programma ir izstrādāta, lai būtu lietotājam draudzīga, ar intuitīvu saskarni, ātru datu apstrādi un iespēju pielāgot produktu sarakstu dinamiskā veidā.

---

## 5.1 Pieteikšanās lapa
### Funkcionalitāte:
- Lietotājs ievada savu e-pasta adresi un paroli.
- Tiek veikta lietotāja autentifikācija, izmantojot bcrypt hash algoritmu.
- Ja pieteikšanās ir veiksmīga, lietotājs tiek pāradresēts uz personalizēto profilu.

![Pieteikšanās Lapa](https://github.com/maximalian/ProLabD/blob/master/parskats/login.png)

### Kods:
- [app.py](https://github.com/maximalian/ProLabD/blob/master/app.py) - Galvenā aplikācijas konfigurācija un maršrutēšana.
  - Funkcija: **home()** - Atgriež galveno lapu.

- [auth_routes.py](https://github.com/maximalian/ProLabD/blob/master/auth_routes.py) - Pieteikšanās un reģistrācijas loģika.
  - Funkcija: **login()** - Apstrādā pieteikšanās pieprasījumus (GET un POST).
  - Funkcija: **register()** - Reģistrē jaunu lietotāju.
  - Funkcija: **logout()** - Izraksta lietotāju no sistēmas.

- [index.html](https://github.com/maximalian/ProLabD/blob/master/templates/index.html) - HTML veidne pieteikšanās lapai.
  - Satur ievades laukus e-pastam un parolei.
  - Pogas pieteikšanās un reģistrācijai.

- [styles.css](https://github.com/maximalian/ProLabD/blob/master/static/css/styles.css) - CSS stila faili lietotāja saskarnei.
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
- [auth_routes.py](https://github.com/maximalian/ProLabD/blob/master/auth_routes.py) - Reģistrācijas loģika.
  - Funkcija: **register()** - Apstrādā reģistrācijas pieprasījumus (GET un POST).

- [register.html](https://github.com/maximalian/ProLabD/blob/master/templates/register.html) - HTML veidne reģistrācijas lapai.
  - Ievades lauki e-pastam, parolei un apstiprinājuma parolei.
  - Validācija un paroles redzamības pārslēgšana.

- [styles.css](https://github.com/maximalian/ProLabD/blob/master/static/css/styles.css) - CSS stila faili.
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

  ![Lietotāja dati](https://github.com/maximalian/ProLabD/blob/master/parskats/details.png)
- Produktu filtrēšana piemērs

  ![Produktu filtrs](https://github.com/maximalian/ProLabD/blob/master/parskats/details_filter.png)

### Kods:
- [auth_routes.py](https://github.com/maximalian/ProLabD/blob/master/auth_routes.py) - Datu apstrādes loģika.
  - Funkcija: **add_details()** - Lietotāja datu pievienošana un atjaunināšana.
- [add_details.html](https://github.com/maximalian/ProLabD/blob/master/templates/add_details.html) - HTML veidne lietotāja datu ievadei.
- [profile.css](https://github.com/maximalian/ProLabD/blob/master/static/css/profile.css) - CSS stila faili lietotāja saskarnei.
- [product_table.js](https://github.com/maximalian/ProLabD/blob/master/static/js/product_table.js) - JavaScript funkcijas produktu filtrēšanai un ierobežojumu iestatīšanai.

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
- [DIETcalc.py](https://github.com/maximalian/ProLabD/blob/master/DIETcalc.py) - Galvenais algoritms uztura plāna aprēķināšanai.
  - Funkcija: **calculate_diet()** - Veido optimizācijas modeli, lai minimizētu izmaksas un nodrošinātu uzturvielu prasības.
  - Algoritms izmanto Pulp bibliotēku, lai atrisinātu lineārās programmēšanas problēmu.
- [user_routes.py](https://github.com/maximalian/ProLabD/blob/master/user_routes.py) - Funkcijas aprēķinu veikšanai un lietotāja datu apstrādei.
  - Funkcija: **calculate_menu()** - Aprēķina uztura plānu.
  - Funkcija: **update_selected_products()** - Atjauno lietotāja izvēlētos produktus.
- [result.html](https://github.com/maximalian/ProLabD/blob/master/templates/result.html) - HTML veidne aprēķinu rezultātu parādīšanai.
- [result.js](https://github.com/maximalian/ProLabD/blob/master/static/js/result.js) - JavaScript koda funkcijas vizualizācijai un validācijai.
  - Funkcija: **validateStoreSelection()** - Pārbauda veikalu izvēli.
  - Grafiku vizualizācijas izveide un eksportēšana DOCX formātā.
- [result.css](https://github.com/maximalian/ProLabD/blob/master/static/css/result.css) - CSS stili rezultātu noformējumam un izkārtojumam.

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

  ![Produktu pārvaldības lapa](https://github.com/maximalian/ProLabD/blob/master/parskats/manage_products.png)

- **Produktu tabula**:
  - Produkta īpašību (kalorijas, olbaltumvielas, tauki, ogļhidrāti, cenas, saites) rediģēšana un saglabāšana.
  - Rediģēšanas piemērs ar izceltiem nederīgiem URL sarkanā krāsā.

  ![Produktu tabula](https://github.com/maximalian/ProLabD/blob/master/parskats/manage_table.png)

- **Produktu filtrs**:
  - Lietotājs var meklēt produktus un filtrēt tos pēc noteiktiem kritērijiem (kategorija, vegānisms, bojāti URL).

  ![Produktu filtrs](https://github.com/maximalian/ProLabD/blob/master/parskats/filter_manage_product.png)

- **Kategoriju pārvaldība**:
  - Jaunas kategorijas pievienošana vai esošās kategorijas dzēšana.

  ![Kategorijas pārvaldība](https://github.com/maximalian/ProLabD/blob/master/parskats/manage_category.png)

- **Failu pārvaldība**:
  - Masveida produktu pievienošana, izmantojot .xlsx failus.

  ![Failu pārvaldība](https://github.com/maximalian/ProLabD/blob/master/parskats/manage_file.png)

- **Produktu rindas**:
  - Jaunu produktu pievienošana pa vienam vai vairākiem uzreiz.
  - Lietotājs var aizpildīt datus par produktiem, norādot nosaukumu, kalorijas, olbaltumvielas, taukus, ogļhidrātus, saites uz veikaliem, cenas un citas īpašības.
  - Ir iespēja izvēlēties kategoriju un norādīt, vai produkts ir vegānisks.
  - Pievienot produktus ar pogu **Add Product** vai dzēst tos ar pogu **Delete Table**.
  - Papildu iespēja pievienot vairākas rindas vienlaicīgi, izmantojot pogu **Add Table** vai pievienot visus produktus uzreiz ar pogu **Add All**.

  ![Produktu rinda](https://github.com/maximalian/ProLabD/blob/master/parskats/product_rows.png)
  ![Produktu rindas](https://github.com/maximalian/ProLabD/blob/master/parskats/product_rows_addTable.png)

- **Navigācijas pogas**:
  - Pāreja uz citām sadaļām (Profils vai Rezultāti).

  ![Navigācijas pogas](https://github.com/maximalian/ProLabD/blob/master/parskats/manage_products_button.png)

### Kods:
- [product_routes.py](https://github.com/maximalian/ProLabD/blob/master/product_routes.py) - Funkcijas produktu saraksta pārvaldībai:
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

- [manage_products.html](https://github.com/maximalian/ProLabD/blob/master/templates/manage_products.html) - HTML veidne produktu saraksta pārvaldībai.
- [manage_products.js](https://github.com/maximalian/ProLabD/blob/master/static/js/manage_products.js) - JavaScript funkcijas tabulas un produktu datu validācijai.
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
- [manage_products.css](https://github.com/maximalian/ProLabD/blob/master/static/css/manage_products.css) - Stila faili tabulas un produktu pārvaldības lapai.

---

## 5.7 Datu bāzes apraksts

Programma izmanto relāciju datubāzi PostgreSQL, lai glabātu lietotāju, produktu un kategoriju datus. Zemāk aprakstītas galvenās datubāzes tabulas, to struktūra un katra atribūta nozīme.

### **5.7.1 Lietotāju tabula (lietotajs)**

Tabula saglabā informāciju par lietotājiem, tostarp personīgos datus, uztura ierobežojumus un izvēles.

![Lietotāju tabula](https://github.com/maximalian/ProLabD/blob/master/parskats/lietotajs.png)

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

![Produktu tabula](https://github.com/maximalian/ProLabD/blob/master/parskats/produkts.png)

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

![Kategoriju tabula](https://github.com/maximalian/ProLabD/blob/master/parskats/kategorijas.png)

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
