import telebot
from telebot import types

TOKEN = '7738412885:AAGrfGPaytm5BvvL5dLIoAbaoe6Uy2H5iHM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("القائمة")  
    markup.add(button)
    bot.send_message(message.chat.id, "عايز تختار ايه", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "القائمة")
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("فرنش")
    button2 = types.KeyboardButton("مش عايز")
    markup.add(button1, button2)
    bot.send_message(message.chat.id,"اختار يا حمادة:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "فرنش")
def Frensh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1_1 = types.KeyboardButton("الافعال") 
    button1_2 = types.KeyboardButton("اسماء الاشارة") 
    button1_3 = types.KeyboardButton("حروف الجر") 
    button1_4 = types.KeyboardButton("المراكز")
    button1_5 = types.KeyboardButton("وظائف")
    button1_6 = types.KeyboardButton("البلاد")
    button1_7 = types.KeyboardButton("الجنسيات")
    button1_8 = types.KeyboardButton("ارجع")
    markup.add(button1_1, button1_2, button1_3, button1_4,button1_5, button1_6, button1_7, button1_8)
    bot.send_message(message.chat.id,"تحب تراجع ايه", reply_markup=markup)

verbs = {
    "Etre يكون": """Être (أن يكون):\n\nJe suis\nTu es\nIl/Elle est\nNous sommes\nVous êtes\nIls/Elles sont""",
    "Avoir يمتلك": """Avoir (أن يمتلك):\n\nJ'ai\nTu as\nIl/Elle a\nNous avons\nVous avez\nIls/Elles ont""",
    "Savoir يعرف": """Savoir (أن يعرف):\n\nJe sais\nTu sais\nIl/Elle sait\nNous savons\nVous savez\nIls/Elles savent""",
    "Faire يفعل": """Faire (أن يفعل):\n\nJe fais\nTu fais\nIl/Elle fait\nNous faisons\nVous faites\nIls/Elles font""",
    "Prendre يأخذ": """Prendre (أن يأخذ):\n\nJe prends\nTu prends\nIl/Elle prend\nNous prenons\nVous prenez\nIls/Elles prennent""",
    "Pouvoir يستطيع": """Pouvoir (أن يستطيع):\n\nJe peux\nTu peux\nIl/Elle peut\nNous pouvons\nVous pouvez\nIls/Elles peuvent""",
    "Vouloir يريد": """Vouloir (أن يريد):\n\nJe veux\nTu veux\nIl/Elle veut\nNous voulons\nVous voulez\nIls/Elles veulent""",
    "Venir يأتي": """Venir (أن يأتي):\n\nJe viens\nTu viens\nIl/Elle vient\nNous venons\nVous venez\nIls/Elles viennent""",
    "Aller يذهب": """Aller (أن يذهب):\n\nJe vais\nTu vas\nIl/Elle va\nNous allons\nVous allez\nIls/Elles vont""",
    "Se lever ينهض": """Se lever (أن ينهض):\n\nJe me lève\nTu te lèves\nIl/Elle se lève\nNous nous levons\nVous vous levez\nIls/Elles se lèvent"""
}

@bot.message_handler(func=lambda message: message.text == "الافعال")
def af3al(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # إضافة الأفعال إلى لوحة المفاتيح
    for verb in verbs.keys():
        markup.add(types.KeyboardButton(verb))
    back2 = types.KeyboardButton("للخلف")
    markup.add(back2)
    bot.send_message(message.chat.id, "عايز فعل ايه؟", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in verbs.keys())
def show_verb(message):
    bot.send_message(message.chat.id, verbs[message.text])



@bot.message_handler(func=lambda message: message.text == "اسماء الاشارة")
def asmaa(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("امثلة Ce") 
    button2 = types.KeyboardButton("امثلة Cet")
    button3 = types.KeyboardButton("امثلة Cette") 
    button4 = types.KeyboardButton("امثلة Ces")
    button5 = types.KeyboardButton("للخلف")
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id,"""أسماء الإشارة في الفرنسية تُستخدم للإشارة إلى شيء أو شخص زي ما في العربية عندنا
أنواع أسماء الإشارة:

هذا (للشيء المذكر القريب) Ce:
مثال: Ce livre (هذا الكتاب)

هذا (لو الاسم فيه حرف متحرك) Cet:
مثال: Cet homme (هذا الرجل)

هذه (للشيء المؤنث) Cette:
مثال: Cette table (هذه الطاولة)

هؤلاء (للجمع) Ces:
مثال: Ces livres (هؤلاء الكتب)

دلوقتي اختار اداة الاشارة الي عايز تشوف كل الامثلة بتاعتها في المنهج

""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة Ce")
def Ce(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""امثلة المنهج على (هذا Ce):

-Ce Pantalon بنطال
-Ce Pull سويتشيرت
-Ce Garson ولد
-Ce Caryon قلم رصاص
-Ce Livre كتاب
-Ce Cahier كراس
-Ce Stylo قلم
-Ce Tableau لوحة
-Ce Club نادي
-Ce Cinema سينما
-Ce Pyjma بيجاما
-Ce Restaurant مطعم""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة Cet")
def Cet(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""امثلة المنهج على (Cet):

-Cet Homme رجل
-Cet Avion طيارة
-Cet Aiseau عصفور
-Cet Immeuble عمارة
-Cet Appartment شقة
-Cet Exerice امتحان
-Cet Arbre شجرة
-Cet Hotel فندق
-Cet Hopital مستشفى
-Cet Anarok معطف
-Cet Animal حيوان""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة Cette")
def Cette(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""
امثلة المنهج على (هذه Cette):

-Cette Ecole مدرسة
-Cette Orange برتقالة
-Cette Fille فتاة
-Cette Robe فستان
-Cette Bague خاتم
-Cette Jupe جيبة
-Cette Chemise قميص
-Cette Voiture سيارة
-Cette Maison منزل
-Cette Vest سترة
-Cette Amie صديقة
-Cette Regle مسطرة
-Cette Casquette قبعة
-Cette Caravate ربطة عنق""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة Ces")
def Ces(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""امثلة المنهج على (هؤلاء Ces):

-Ces Hommes رجال
-Ces Filles فتيات
-Ces Garsons اولاد
-Ces Oranges برتقالات
-Ces Gateaux جاتوهات
-Ces Chaussettes جوارب""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "حروف الجر")
def dirs(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("الحروف التي تسبق المكان") 
    button2 = types.KeyboardButton("حرف جر De")
    button3 = types.KeyboardButton("حرف الجر à") 
    button4 = types.KeyboardButton("حروف جر المواصلات")
    button5 = types.KeyboardButton("للخلف")
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id,"""اي حروف جر تريد""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "الحروف التي تسبق المكان")
def gar(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""حروف الجر التي تسبق الاماكن

près de - بالقرب من
loin de - بعيد عن
à côté de - بجانب
à droite de - إلى اليمين من
à droite - إلى اليمين
à gauche de - إلى اليسار من
à gauche - إلى اليسار
à l'est de - إلى الشرق من
à l'ouest de - إلى الغرب من
au sud de - إلى الجنوب من
au nord de - إلى الشمال من
au centre de - في مركز
en face de - أمام
devant - أمام
derrière - خلف
entre - بين
sur - على
sous - تحت""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "حرف جر De")
def de(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("امثلة du")
    button2 = types.KeyboardButton("امثلة de l'")
    button3 = types.KeyboardButton("امثلة de la")
    button4 = types.KeyboardButton("امثلة des")
    button5 = types.KeyboardButton("عودة")
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id,"""de هو حرف يعني (من / عن) ويتغير حسب حالة الاسم التي يليه

-du مع الاسم المذكر البادئ بساكن
-de l' مع الاسم المفرد البادئ بمتحرك
-de la مع الاسم المؤنث البادئ بساكن
-des مع الاسم الجمع بكلتا حلاته""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة du")
def de1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""امثلة الحرف du 

du club - من النادي
du cinéma - من السينما
du restaurant - من المطعم
du musée - من المتحف
du manche - من المقود
du lycée - من المدرسة الثانوية
du parc - من الحديقة""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة de l'")
def de2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""امثلة الحرف de l'

de l'hôtel - من الفندق
de l'hôpital - من المستشفى
de l'école - من المدرسة
de l'épicerie - من البقالة""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة de la")
def de3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""امثلة الحرف de la

de la clinique - من العيادة
de la maison - من المنزل
de la mer - من البحر
de la pharmacie - من الصيدلية
de la librairie - من المكتبة
de la piscine - من المسبح
de la plage - من الشاطئ
de la fête - من الحفلة""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة des")
def de4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""من امثلة الحرف des
    
    des clubs - من الأندية
des cinémas - من السينمات
des restaurants - من المطاعم
des musées - من المتاحف
des manches - من الأكمام
des lycées - من المدارس الثانوية
des parcs - من الحدائق""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "حرف الجر à")
def a(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("امثلة au")
    button2 = types.KeyboardButton("امثلة à l'")
    button3 = types.KeyboardButton("امثلة à la")
    button4 = types.KeyboardButton("امثلة aux")
    button5 = types.KeyboardButton("عودة")
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id,"""à هو حرف يعني (إلى / في) ويتغير حسب حالة الاسم التي يليه

-au مع الاسم المذكر البادئ بساكن
-à l' مع الاسم المفرد البادئ بمتحرك
-à la مع الاسم المؤنث البادئ بساكن
-aux مع الاسم الجمع بكلتا حلاته""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة au")
def a1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""امثلة الحرف au 

au parc - في الحديقة
au cinéma - في السينما
au restaurant - في المطعم
au musée - في المتحف
au travail - في العمل
au marché - في السوق
au stade - في الملعب""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة à l'")
def a2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""امثلة الحرف à l'

à l'école - في المدرسة
à l'hôtel - في الفندق
à l'hôpital - في المستشفى
à l'université - في الجامعة
à l'aéroport - في المطار
à l'église - في الكنيسة
à l'exposition - في المعرض""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة à la")
def a3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""امثلة الحرف à la

à la maison - في المنزل
à la plage - في الشاطئ
à la bibliothèque - في المكتبة
à la gare - في المحطة
à la cuisine - في المطبخ
à la pharmacie - في الصيدلية
à la banque - في البنك""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "امثلة aux")
def a4(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""من امثلة الحرف aux

aux États-Unis - في الولايات المتحدة
aux magasins - في المتاجر
aux écoles - في المدارس
aux restaurants - في المطاعم
aux parcs - في الحدائق
aux bureaux - في المكاتب
aux plages - في الشواطئ""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "حروف جر المواصلات")
def hrka(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("En")
    button2 = types.KeyboardButton("à")
    button3 = types.KeyboardButton("par")
    button4 = types.KeyboardButton("عودة")
    markup.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id,"""هي الحروف التي تأتي قبل وسيلة التحرك""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "En")
def en(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""هي اداة تستخدم قبل وسيلة النقل التي تكون كبيرة وللعامة وتكون محددة
    
    en voiture - بالسيارة
en bus - بالحافلة
en avion - بالطائرة
en train - بالقطار
en métro - بالمترو
en bateau - بالسفينة
en tram - بالترام""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "à")
def a0(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""هي اداة تستخدم مع الوسائلة الصغيرة والبسيطة
    
    à pied - مشياً على الأقدام
à vélo - بالدراجة
à moto - بالدراجة النارية
à cheval - على ظهر الخيل""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "par")
def par(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""هية اداة تستخدم مع وسائل النقل ولكن بشكل عام بدون تحديد وسيلة معينة وغالبا ما يأتي معها le,la,l'
    
    par le train - بالقطار (وسيلة النقل عبر القطار)
par le métro - بالمترو (وسيلة النقل عبر المترو)
par avion - بالطائرة (وسيلة النقل عبر الطائرة)
par la voiture - بالسيارة (وسيلة النقل عبر السيارة)""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "المراكز")
def marakez(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""هذه هي المراكز الترتيبية في المسابقات
    
    Premier / Première (1er / 1ère) - الأول / الأولى
Deuxième (2ème) - الثاني / الثانية
Second / Seconde (2nd / 2nde) - الثاني / الثانية (الحالة البديلة)
Troisième (3ème) - الثالث / الثالثة
Quatrième (4ème) - الرابع / الرابعة
Cinquième (5ème) - الخامس / الخامسة
Sixième (6ème) - السادس / السادسة
Septième (7ème) - السابع / السابعة
Huitième (8ème) - الثامن / الثامنة
Neuvième (9ème) - التاسع / التاسعة
Dixième (10ème) - العاشر / العاشرة
Onzième (11ème) - الحادي عشر / الحادية عشر
Douzième (12ème) - الثاني عشر / الثانية عشر
Treizième (13ème) - الثالث عشر / الثالثة عشر
Quatorzième (14ème) - الرابع عشر / الرابعة عشر
Quinzième (15ème) - الخامس عشر / الخامسة عشر""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "وظائف")
def jobs(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("طرق التأنيث المختلفة للوظائف")
    button2 = types.KeyboardButton("للخلف")
    markup.add(button1, button2)
    bot.send_message(message.chat.id,"""هذه هي بعذ الوظائف المهمة في الفرنساوي
    
    طبيب - Médecin
صيدلي - Pharmacien / Pharmacienne
ممرضة - Infirmière
طبيب بيطري - Vétérinaire
أستاذ - Professeur
حلاق - Coiffeur / Coiffeuse
ممثل - Acteur / Actrice
مذيع - Animateur / Animatrice
رسام - Peintre
مصور - Photographe
طباخ - Cuisinier / Cuisinière
رجل إطفاء - Pompier
بائعة الزهور - Fleuriste
صحفي - Journaliste
بائع - Vendeur / Vendeuse
طبيب أسنان - Dentiste
موسيقي - Musicien / Musicienne""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "طرق التأنيث المختلفة للوظائف")
def femalejobs(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""هذه هي القواعد لتأنيث الوظائف
    
    1. التي تؤنث بإضافة -e:
Avocat (محامي) → Avocate (محامية)
Professeur (معلم) → Professeure (معلمة)
Coiffeur (مساعد) → Coiffeuse (مساعدة)

2. التي تنتهي بـ -e (لا تغيير الجذر):
Peintre (رسام) → Peintre (رسامة)
Photographe (مصور) → Photographe (مصورة)
Vétérinaire (طبيب بيطري) → Vétérinaire (طبيبة بيطرية)

3. التي تنتهي بـ -é ويضاف إليها -e:
Employé (موظف) → Employée (موظفة)

4. التي تنتهي بـ -eur وتتحول إلى -euse:
Vendeur (بائع) → Vendeuse (بائعة)
Chanteur (مغني) → Chanteuse (مغنية)
Acheteur (مشتري) → Acheteuse (مشتريّة)

5. التي تنتهي بـ -teur وتتحول إلى -trice:
Directeur (مدير) → Directrice (مديرة)
Agriculteur (مزارع) → Agricultrice (مزارعة)

6. التي تنتهي بـ -f وتتحول إلى -ve:
Sportif (رياضي) → Sportive (رياضية)

7. التي تنتهي بـ -en وتضاف إليها -ne:
Pharmacien (صيدلي) → Pharmacienne (صيدلية)
Musicien (موسيقي) → Musicienne (موسيقية)

8. التي تنتهي بـ -er وتتحول إلى -ère:
Boulanger (خباز) → Boulangère (خبازة)
Infirmier (ممرض) → Infirmière (ممرضة)
Cuisinier (طباخ) → Cuisinière (طباخة)

9. التي لا تتغير أبدًا:
Pompier (رجل إطفاء) → Pompier (امرأة إطفاء)
Mannequin (عارض أزياء) → Mannequin (عارضة أزياء)
Médecin (طبيب) → Médecin (طبيبة)""", reply_markup=markup)    

@bot.message_handler(func=lambda message: message.text == "الجنسيات")
def gensez(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""الجنسيات التي تؤنث باضافة e في نهايتها:
فرنسي (Français) → فرنسية (Française)
إنجليزي (Anglais) → إنجليزية (Anglaise)
هولندي (Néerlandais) → هولندية (Néerlandaise)
مغربي (Marocain) → مغربية (Marocaine)
أرجنتيني (Argentin) → أرجنتينية (Argentine)
مكسيكي (Mexicain) → مكسيكية (Mexicaine)
لبناني (Libanais) → لبنانية (Libanaise)
صيني (Chinois) → صينية (Chinoise)
أمريكي (Américain) → أمريكية (Américaine)
إسباني (Espagnol) → إسبانية (Espagnole)
سويدي (Suédois) → سويدية (Suédoise)
ألماني (Allemand) → ألمانية (Allemande)
ياباني (Japonais) → يابانية (Japonaise)
برتغالي (Portugais) → برتغالية (Portugaise)
سنغالي (Sénégalais) → سنغالية (Sénégalaise)
مكسيكي (Mexicain) → مكسيكية (Mexicaine)

الجنسيات التي تبقى كما هي:
روسي (Russe) → روسية (Russe)
سويسري (Suisse) → سويسرية (Suisse)
بلجيكي (Belge) → بلجيكية (Belge)

الجنسيات التي تنتهي بen تؤنث باضافة ne :
مصري (Égyptien) → مصرية (Égyptienne)
إيطالي (Italien) → إيطالية (Italienne)
جزائري (Algérien) → جزائرية (Algérienne)
برازيلي (Brésilien) → برازييلية (Brésilienne)
تونسي (Tunisien) → تونسية (Tunisienne)
كندي (Canadien) → كندية (Canadienne)
هندي (Indien) → هندية (Indienne)
أسترالي (Australien) → أسترالية (Australienne)

الجنسيات الشاذة في التأنيث :
يوناني (Grec) → يونانية (Grecque)
تركي (Turc) → تركية (Turque)""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "البلاد")
def pays(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    botton1 = types.KeyboardButton("قواعد من و عن / الى و في")
    botton2 = types.KeyboardButton("للخلف")
    markup.add(botton1, botton2)
    bot.send_message(message.chat.id,"""
    أفريقيا (L'Afrique):
L'Égypte (مصر) → Le Caire (القاهرة)
Le Maroc (المغرب) → Rabat (الرباط)
La Mauritanie (موريتانيا) → Nouakchott (نواكشوط)
Le Soudan (السودان) → Khartoum (الخرطوم)
L'Algérie (الجزائر) → Alger (الجزائر)
La Libye (ليبيا) → Tripoli (طرابلس)
La Tunisie (تونس) → Tunis (تونس)
Le Zimbabwe (زيمبابوي) → Harare (هراري)

أوروبا (L'Europe):
La France (فرنسا) → Paris (باريس)
L'Angleterre (إنجلترا) → Londres (لندن)
Les Pays-Bas (هولندا) → Amsterdam (أمستردام)
Le Portugal (البرتغال) → Lisbonne (لشبونة)
L'Espagne (إسبانيا) → Madrid (مدريد)
L'Italie (إيطاليا) → Rome (روما)
L'Allemagne (ألمانيا) → Berlin (برلين)
La Belgique (بلجيكا) → Bruxelles (بروكسل)
La Suisse (سويسرا) → Berne (برن)

آسيا (L'Asie):
Le Japon (اليابان) → Tokyo (طوكيو)
La Russie (روسيا) → Moscou (موسكو)
Le Liban (لبنان) → Beyrouth (بيروت)
La Syrie (سوريا) → Damas (دمشق)
L'Arabie Saoudite (السعودية) → Riyad (الرياض)
Le Koweït (الكويت) → Koweït (مدينة الكويت)
La Grèce (اليونان) → Athènes (أثينا)
La Turquie (تركيا) → Ankara (أنقرة)
La Chine (الصين) → Pékin (بكين)
L'Inde (الهند) → New Delhi (نيودلهي)

أمريكا الشمالية (L'Amérique du Nord):
Le Canada (كندا) → Ottawa (أوتاوا)
Les États-Unis (الولايات المتحدة) → Washington, D.C. (واشنطن)
Le Mexique (المكسيك) → Mexico (مكسيكو سيتي)

أمريكا الجنوبية (L'Amérique du Sud):
Le Brésil (البرازيل) → Brasília (برازيليا)
L'Argentine (الأرجنتين) → Buenos Aires (بوينس آيرس)

أستراليا (L'Australie):
L'Australie (أستراليا) → Canberra (كانبيرا)""", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "قواعد من و عن / الى و في")
def ka3eda(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bot.send_message(message.chat.id,"""
1- القارات

-جميع القارات تأخذ en (من وإالى)
-جميع القارات تأخذ d' (من وعن) 

2- الدول

الدول المذكرة
-التي تبدأ بحرف ساكن تأخذ au (من وإالى)
-التي تبدا بساكن تأخذ du (من وعن) 

الدول المؤنثة
-التي تنتهي ب e تاخذ en (من وإالى)
-التي تبداء بساكن تأخذ de (من وعن) 

الدول البادئ بمتحرك
-en (من وإالى)
-d' (من وعن) 

الدول الجمع
-aux (من وإالى)
-des (من وعن) 

3- الجزر

الجزر المفردة
-à (من وإالى)
-de (من وعن) 

الجزر الجمع
-aux (من وإالى)
-des (من وعن) 

4- المدن

المدن بصفة عامة
-à (من وإالى)
-de/d' (من وعن) 

في حالة ال Fayoum,Caire,Sinai,Havre
-au (من وإالى)
-au (من وعن) 

في حالة ال Mecque,Havane
-à la (من وإالى)
-de la (من وعن) 

5- الاماكن العامة

مفرد مذكر ساكن
-au (من وإالى)
-du (من وعن) 

مفرد مؤنث ساكن
-à la (من وإالى)
-de la (من وعن) 

مفرد متحرك
-à l' (من وإالى)
-de l' (من وعن) 

جمع بنوعيه
-aux (من وإالى)
-des (من وعن) 
""", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "عودة")
def back3(message):
    dirs(message)
@bot.message_handler(func=lambda message: message.text == "ارجع")
def back(message):
    show_menu(message)
@bot.message_handler(func=lambda message: message.text == "للخلف")
def back2(message):
    Frensh(message)
bot.polling()