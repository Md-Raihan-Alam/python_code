myData = [
[50.06688579999999,19.9136192, 'aleja Adama Mickiewicza 30, 30-059 Kraków, Poland'],
[52.2394019,21.0150792, 'Krakowskie Przedmieście 5, 00-068 Warszawa, Poland'],
[30.0186205,31.5014854, 'AUC Avenue، Road، New Cairo 1, Cairo Governorate 11835, Egypt'],
[34.0489281,-111.0937311, 'Arizona, USA'],
[38.0399391,23.8030901, 'Monumental Plaza, Building C, 1st Floor, Leof. Kifisias 44, Marousi 151 25, Greece'],
[28.3588163,75.58802039999999, 'Vidya Vihar, Pilani, Rajasthan 333031, India'],
[6.891986300000001,3.7181286, '121103, Ilishan-Remo, Nigeria'],
[25.2677203,82.99125819999999, 'Ajagara, Varanasi, Uttar Pradesh 221005, India'],
[12.9504048,77.5020617, 'Mysore Rd, Jnana Bharathi, Bengaluru, Karnataka 560056, India'],
[31.5488923,-97.1130573, '1311 S 5th St, Waco, TX 76706, USA'],
[39.9619537,116.3662615, '19 Xinwai Ave, Beitaipingzhuang, Hai Dian Qu, Bei Jing Shi, China, 100875'],
[53.8938988,27.5460609, 'prasp. Niezaliežnasci 4, Minsk, Belarus'],
[44.8184518,20.4575913, 'Studentski trg 1, Beograd, Serbia'],
[42.5030333,-89.0309048, '700 College St, Beloit, WI 53511, USA'],
[53.8938988,27.5460609, 'prasp. Niezaliežnasci 4, Minsk, Belarus'],
[31.261426,34.7995546, 'David Ben Gurion Blvd 1, Beer Sheva, Israel'],
[10.6779085,78.74454879999999, 'Palkalaiperur, Tiruchirappalli, Tamil Nadu 620024, India'],
[42.3504997,-71.1053991, 'Boston, MA 02215, USA'],
[35.3011298,-120.6582825, '1 Grand Ave, San Luis Obispo, CA 93407, USA'],
[34.1813584,-117.3231875, '5500 University Pkwy, San Bernardino, CA 92407, USA'],
[51.5210416,-0.1746649, '25 Paddington Grn, London W2 1NB, UK'],
[40.8075355,-73.9625727, 'New York, NY 10027, USA'],
[52.0746136,-0.6282833, 'College Rd, Cranfield, Wharley End, Bedford MK43 0AL, UK'],
[50.1030364,14.3912841, '166 36 Prague 6, Czechia'],
[43.7044406,-72.2886934, 'Hanover, NH 03755, USA'],
[37.3192827,-122.0447913, '21250 Stevens Creek Blvd, Cupertino, CA 95014, USA'],
[51.3769424,7.4946354, 'Universitätsstraße 11, 58097 Hagen, Germany'],
[48.4331922,35.0427966, 'Haharina Ave, 72, Dnipropetrovsk, Dnipropetrovska oblast, Ukraine, 49000'],
[38.430691,27.13692, 'No: 144 35210, Alsancak, Cumhuriyet Blv, 35220 Konak/İzmir, Turkey'],
[39.9566127,-75.18994409999999, '3141 Chestnut St, Philadelphia, PA 19104, USA'],
[30.2849185,-97.7340567, 'Austin, TX 78712, USA'],
[36.0014258,-78.9382286, 'Durham, NC 27708, USA'],
[45.7864448,4.7641329, '23 Av. Guy de Collongue, 69130 Écully, France'],
[48.709445,2.1661629, 'CentraleSupélec, 3 Rue Joliot Curie, 91190 Gif-sur-Yvette, France'],
[36.1026877,-79.5023313, '50 Campus Drive, Elon, NC 27244, USA'],
[54.9134537,9.7780196, 'Alsion 4, 6400 Sønderborg, Denmark'],
[-2.1480702,-79.9644896, 'Vía Perimetral 5, Guayaquil, Ecuador'],
[51.24683899999999,6.7916647, 'Münsterstraße 156, 40476 Düsseldorf, Germany'],
[47.7233835,13.0871253, 'Urstein S 1, 5412 Salzburg, Austria'],
[-23.6956191,-46.5469041, 'Av. Pereira Barreto, 400 - Vila Baeta Neves - Centro, São Bernardo do Campo - SP, 09751-000, Brazil'],
[45.2461012,19.8516968, 'Trg Dositeja Obradovića 6, Novi Sad 106314, Serbia'],
[40.7529167,-73.4266988, '2350 NY-110, Farmingdale, NY 11735, USA'],
[-19.870682,-43.9677359, 'Av. Pres. Antônio Carlos, 6627 - Pampulha, Belo Horizonte - MG, 31270-901, Brazil'],
[26.3749876,-80.10106329999999, '777 Glades Rd, Boca Raton, FL 33431, USA'],
[42.7789743,-72.05553929999999, '40 University Dr, Rindge, NH 03461, USA'],
[26.1540317,91.6629743, 'Gopinath Bordoloi Nagar, Jalukbari, Guwahati, Assam 781014, India'],
[38.8298118,-77.3073606, '4400 University Dr, Fairfax, VA 22030, USA'],
[38.8977953,-77.0129087, '600 New Jersey Ave NW, Washington, DC 20001, USA'],
[33.753068,-84.38528190000001, 'Atlanta, GA 30302, USA'],
[42.9097484,-85.7630885, 'Grandville, MI, USA'],
[50.87485419999999,4.7077677, 'Andreas Vesaliusstraat 13, 3000 Leuven, Belgium'],
[21.0070253,105.843136, '1 Đại Cồ Việt, Bách Khoa, Hai Bà Trưng, Hà Nội, Vietnam'],
[31.7945578,35.2414009, 'Jerusalem'],
[17.4448649,78.34981379999999, 'Professor CR Rao Rd, Gachibowli, Hyderabad, Telangana 500032, India'],
[26.5123388,80.2329, 'Kalyanpur, Kanpur, Uttar Pradesh 208016, India'],
[59.3954004,24.6641777, 'Raja 4, 12616 Tallinn, Estonia'],
[39.1784384,-86.5133166, '107 S Indiana Ave, Bloomington, IN 47405, USA'],
[45.4377574,12.3223297, 'Santa Croce, 191, 30135 Venezia VE, Italy'],
[41.8348731,-87.6270059, '10 W 35th St, Chicago, IL 60616, USA'],
[41.5042613,-88.17752689999999, 'Jr College, Joliet, IL 60431, USA'],
[28.545718,77.19276789999999, 'IIT Delhi Main Rd, IIT Campus, Hauz Khas, New Delhi, Delhi 110016, India'],
[22.3150063,87.3100489, '8886+223, IIT Kharagpur, Kharagpur, West Bengal 721302, India'],
[23.8142953,86.44118069999999, 'Police Line Road, Main Campus IIT (ISM, near Rani Bandh, IIT (ISM, Hirapur, Sardar Patel Nagar, Dhanbad, Jharkhand 826004, India'],
[39.1784384,-86.5133166, '107 S Indiana Ave, Bloomington, IN 47405, USA'],
[39.1784384,-86.5133166, '107 S Indiana Ave, Bloomington, IN 47405, USA'],
[45.618429,-72.9672599, '3230 Rue Sicotte, Saint-Hyacinthe, QC J2S 2M2, Canada'],
[40.7551279,-73.9861749, '1460 Broadway, New York, NY 10036, USA'],
[18.4880037,-69.96249499999999, 'Av. de los Próceres 49, Santo Domingo 10602, Dominican Republic']
];
