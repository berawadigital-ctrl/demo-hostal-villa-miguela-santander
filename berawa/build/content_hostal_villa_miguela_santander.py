# Contenido de la demo Villa Miguela (Santander) (es/en/fr/de). Hechos de villamiguela.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Literas en habitación compartida','Habitaciones privadas con baño'],'en':['Bunks in shared rooms','Private rooms with bathroom'],'fr':['Lits en chambre partagée','Chambres privées avec salle de bain'],'de':['Betten im Mehrbettzimmer','Privatzimmer mit Bad']}
RD={
'es':['Literas cápsula con cortinas opacas, lámpara de lectura, enchufe, USB, ropa de cama y cajón guardaequipaje. Habitaciones mixtas de 18 y femeninas de 6. Baño compartido fuera de la habitación.','Marinera (6 plazas), Bahía (5), Sardinero (4) y Raqueros (4): todas exteriores, con baño propio, cama doble de 150 y sofá cama. También grupos privados de 3, 4 y 6 plazas.'],
'en':['Capsule bunks with blackout curtains, reading lamp, socket, USB, bed linen and luggage drawer. Mixed rooms of 18 and female rooms of 6. Shared bathroom outside the room.','Marinera (6 guests), Bahía (5), Sardinero (4) and Raqueros (4): all exterior, with private bathroom, 150 cm double bed and sofa bed. Also private group rooms for 3, 4 and 6.'],
'fr':["Lits capsule avec rideaux occultants, lampe de lecture, prise, USB, linge de lit et tiroir à bagages. Chambres mixtes de 18 et féminines de 6. Salle de bain partagée hors de la chambre.","Marinera (6 personnes), Bahía (5), Sardinero (4) et Raqueros (4) : toutes extérieures, avec salle de bain privée, lit double de 150 et canapé-lit. Aussi des chambres privées de groupe de 3, 4 et 6."],
'de':['Kapselbetten mit Verdunkelungsvorhang, Leselampe, Steckdose, USB, Bettwäsche und Gepäckschublade. Gemischte Zimmer mit 18 und Frauenzimmer mit 6 Betten. Gemeinschaftsbad außerhalb des Zimmers.','Marinera (6 Personen), Bahía (5), Sardinero (4) und Raqueros (4): alle nach außen gelegen, mit eigenem Bad, Doppelbett 150 cm und Schlafsofa. Außerdem private Gruppenzimmer für 3, 4 und 6.']}
ART={
'hero':('waves',9801,['#12384a','#e9a96b','#f6d6a8','#2c5f73','#1d4a5c','#0d2a38']),
'intro':('skyline',9802,['#e9eef0','#e3a873','#f1cfa0','#2c5f73','#1d4a5c','#0d2a38']),
'r1':('columns',9811,['#eef1f1','#f8f6f2','#2c5f73','#1d4a5c','#0d2a38']),
'r2':('arches',9812,['#efe9df','#e0a66d','#2c5f73','#12384a','#0a1f2a']),
'g1':('waves',9821,['#1d4a5c','#efb57c','#f7dcb3','#367086','#285b6e','#163846']),
'g2':('hills',9822,['#e7eee9','#efe4cc','#dfa56a','#8fb3a6','#5f8a7c','#3d6457']),
'g3':('skyline',9823,['#1f3d4f','#e5a266','#f3d19e','#5b4a6e','#47395a','#2a2138']),
'g4':('arches',9824,['#e9e2d6','#d99f66','#2c5f73','#12384a','#0a1f2a'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Villa Miguela · Hostel en Santander',see_rooms='Ver las habitaciones',hero_k='Santander · Menéndez Pelayo 66',hero_t='La diversión de un hostel con la comodidad de un hotel',hero_s='60 literas individuales, 4 habitaciones privadas con baño y 7 habitaciones compartidas en Santander.',
 intro_t='Santander empieza aquí',intro_p1='La vida en común de un hostel con la privacidad de una litera individual. Una planta entera está reservada a habitaciones privadas con baño propio, pensadas para familias, parejas y grupos.',
 intro_p2='Salón con televisión y sofás, comedor, espacio de trabajo, terraza superior con vistas panorámicas y patio donde se celebran conciertos y actividades.',
 stats=['60 literas','4 habitaciones privadas','7 habitaciones compartidas','Wi-fi gratis'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Literas en habitaciones compartidas (mixtas y femeninas) y habitaciones privadas con baño.',
 svcs=['Wi-fi gratis','Salón y comedor','Work-office','Terraza con vistas','Patio con actividades','Check-in online'],
 around_s='A pocos metros del Túnel del Tren de Pombo, que lleva en un momento a la zona costera del Sardinero.',
 loc_p='Calle Menéndez Pelayo 66 · 39006 Santander (Cantabria). Recepción de lunes a viernes de 9:00 a 18:00.',
 chips=['¿Qué habitaciones tenéis?','¿A qué hora es el check-in?','¿Dónde está el hostel?','¿Cómo reservo?']),
'en':dict(title='Villa Miguela · Hostel in Santander',see_rooms='See the rooms',hero_k='Santander · Menéndez Pelayo 66',hero_t='The fun of a hostel with the comfort of a hotel',hero_s='60 individual bunks, 4 private rooms with bathroom and 7 shared rooms in Santander.',
 intro_t='Santander starts here',intro_p1='The shared life of a hostel with the privacy of an individual bunk. A whole floor is reserved for private rooms with their own bathroom, for families, couples and groups.',
 intro_p2='Lounge with TV and sofas, dining room, work space, top-floor terrace with panoramic views and a patio where concerts and activities are held.',
 stats=['60 bunks','4 private rooms','7 shared rooms','Free Wi-fi'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Bunks in shared rooms (mixed and female) and private rooms with bathroom.',
 svcs=['Free Wi-fi','Lounge and dining room','Work-office','Terrace with views','Patio with activities','Online check-in'],
 around_s='A few metres from the Pombo train tunnel, which takes you to the Sardinero seafront in no time.',
 loc_p='Calle Menéndez Pelayo 66 · 39006 Santander (Cantabria). Reception Monday to Friday from 9:00 to 18:00.',
 chips=['Which rooms do you have?','What time is check-in?','Where is the hostel?','How do I book?']),
'fr':dict(title='Villa Miguela · Auberge à Santander',see_rooms='Voir les chambres',hero_k='Santander · Menéndez Pelayo 66',hero_t="L'ambiance d'une auberge avec le confort d'un hôtel",hero_s='60 lits individuels, 4 chambres privées avec salle de bain et 7 chambres partagées à Santander.',
 intro_t='Santander commence ici',intro_p1="La vie en commun d'une auberge avec l'intimité d'un lit individuel. Un étage entier est réservé aux chambres privées avec salle de bain, pour familles, couples et groupes.",
 intro_p2='Salon avec télévision et canapés, salle à manger, espace de travail, terrasse en haut avec vue panoramique et patio où ont lieu concerts et activités.',
 stats=['60 lits','4 chambres privées','7 chambres partagées','Wi-fi gratuit'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Lits en chambres partagées (mixtes et féminines) et chambres privées avec salle de bain.',
 svcs=['Wi-fi gratuit','Salon et salle à manger','Work-office','Terrasse avec vue','Patio avec activités','Check-in en ligne'],
 around_s='À quelques mètres du tunnel ferroviaire de Pombo, qui mène en un instant au front de mer du Sardinero.',
 loc_p='Calle Menéndez Pelayo 66 · 39006 Santander (Cantabrie). Réception du lundi au vendredi de 9:00 à 18:00.',
 chips=['Quelles chambres avez-vous ?',"À quelle heure est le check-in ?","Où se trouve l'auberge ?",'Comment réserver ?']),
'de':dict(title='Villa Miguela · Hostel in Santander',see_rooms='Zimmer ansehen',hero_k='Santander · Menéndez Pelayo 66',hero_t='Der Spaß eines Hostels mit dem Komfort eines Hotels',hero_s='60 Einzelbetten, 4 Privatzimmer mit Bad und 7 Mehrbettzimmer in Santander.',
 intro_t='Santander beginnt hier',intro_p1='Das Gemeinschaftsleben eines Hostels mit der Privatsphäre eines eigenen Bettes. Eine ganze Etage ist Privatzimmern mit eigenem Bad vorbehalten, für Familien, Paare und Gruppen.',
 intro_p2='Aufenthaltsraum mit Fernseher und Sofas, Speiseraum, Arbeitsbereich, Dachterrasse mit Panoramablick und ein Innenhof mit Konzerten und Aktivitäten.',
 stats=['60 Betten','4 Privatzimmer','7 Mehrbettzimmer','Kostenloses WLAN'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Betten in Mehrbettzimmern (gemischt und nur für Frauen) und Privatzimmer mit Bad.',
 svcs=['Kostenloses WLAN','Aufenthalts- und Speiseraum','Work-Office','Terrasse mit Aussicht','Innenhof mit Aktivitäten','Online-Check-in'],
 around_s='Wenige Meter vom Bahntunnel von Pombo, durch den Sie im Nu an die Küste des Sardinero gelangen.',
 loc_p='Calle Menéndez Pelayo 66 · 39006 Santander (Kantabrien). Rezeption Montag bis Freitag von 9:00 bis 18:00 Uhr.',
 chips=['Welche Zimmer gibt es?','Wann ist der Check-in?','Wo liegt das Hostel?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://booking.roomraccoon.es/villa-miguela/'
BOOK=dict(mode='engine',url={l:RB+l+'/' for l in ('es','en','fr','de')})
D=dict(name='Villa Miguela',ac='#12384a',ac2='#2c5f73',ac2_a11y='#1d4a5c',book=BOOK,around=['Túnel del Tren de Pombo','El Sardinero'],foot=FOOT,
 address='Calle Menéndez Pelayo 66 · 39006 Santander',phones=['+34 660 53 45 41'],emails=['hola@villamiguela.com'],maps='Villa Miguela, Calle Menéndez Pelayo 66, 39006 Santander',t=T)
META=dict(repo='demo-hostal-villa-miguela-santander',name='Villa Miguela',legal_name='RESIDENCIA VILLA MIGUELA S.L.',registry_ids=['B01882851'],
 url='https://www.villamiguela.com/',domain='villamiguela.com',municipality='Santander',province='Cantabria',sector='hostel con literas cápsula y habitaciones privadas con baño en Santander',
 read_at='2026-10-30T08:46:00+01:00',created_at='2026-10-30T08:45:00+01:00',built_at='2026-10-30T09:00:00+01:00',audit_date='2026-10-30T08:42:00+01:00',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T12:45:23+01:00',url='https://www.google.com/maps/place/Hostel+Villa+Miguela/@43.4668799,-3.7934558,17z/data=!4m9!3m8!1s0xd494b0c6a3c140d:0x214d8a3878235848!5m2!4m1!1i2!8m2!3d43.4668799!4d-3.7934558!16s%2Fg%2F11t3v2hp1x'),
 book=dict(mode='engine',url=RB+'es/',note='motor de reservas real de su web (RoomRaccoon, enlace RESERVAR de villamiguela.com), HTTP 200 comprobado el 30/10/2026 en es/en/fr/de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Cómo son las habitaciones privadas?','K02'),('¿A qué hora es el check-in?','K03'),('¿Hay wifi?','K04'),('¿Qué zonas comunes hay?','K05'),('¿Puedo dejar las maletas?','K06'),('¿Puedo ir con mi perro?','K07'),('¿Dónde está el hostel?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Está incluida la ropa de cama?','K10'),('¿Es accesible?','K11'),('¿Tenéis piscina?',None),('¿Hay gimnasio?',None)],
'en':[('Which rooms do you have?','K01'),('What are the private rooms like?','K02'),('What time is check-in?','K03'),('Is there wifi?','K04'),('What common areas are there?','K05'),('Can I leave my luggage?','K06'),('Can I bring my dog?','K07'),('Where is the hostel?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('Is bed linen included?','K10'),('Is it accessible?','K11'),('Do you have a swimming pool?',None),('Is there a gym?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Comment sont les chambres privées ?','K02'),('À quelle heure est le check-in ?','K03'),('Y a-t-il le wifi ?','K04'),('Quels espaces communs y a-t-il ?','K05'),('Puis-je laisser mes bagages ?','K06'),('Puis-je venir avec mon chien ?','K07'),("Où se trouve l'auberge ?",'K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Le linge de lit est-il inclus ?','K10'),('Est-ce accessible ?','K11'),('Avez-vous une piscine ?',None),('Y a-t-il une salle de sport ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wie sind die Privatzimmer?','K02'),('Wann ist der Check-in?','K03'),('Gibt es WLAN?','K04'),('Welche Gemeinschaftsräume gibt es?','K05'),('Kann ich mein Gepäck abgeben?','K06'),('Darf ich meinen Hund mitbringen?','K07'),('Wo liegt das Hostel?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Ist Bettwäsche inbegriffen?','K10'),('Ist es barrierefrei?','K11'),('Haben Sie ein Schwimmbad?',None),('Gibt es ein Fitnessstudio?',None)]}
