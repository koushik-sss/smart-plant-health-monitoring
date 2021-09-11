import telebot
import newpy
import diseaseCheck
import soilv2
import bird
token = '1832375580:AAHXfWE6ii1Ov7wnhPPeO-WOICkJBN0KmmA'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello!')
    bot.send_message(message.chat.id, 'Instructions: Type <disease> to identify diseases from the leaf images. If you want to check for the presence of water in soil, type <water>. To check for birds in the field, type <birds>. Type /help to display this message again.')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'disease':
        bot.send_message(message.chat.id, 'Checking for disease. Please wait.')
        x = diseaseCheck.diseaseID()
        bot.send_message(message.chat.id, x)
        
        if(x == 'Pepper__bell___Bacterial_spot'):
            bot.send_message(message.chat.id, 'https://www.amazon.in/Syngenta-Metabolites-Nutrients-Biostimulant-Enhancer/dp/B08SCBMKYB/ref=sr_1_3?dchild=1&keywords=syngenta&qid=1626593936&sr=8-3')
        
        elif(x == 'Potato___Early_blight'):
            bot.send_message(message.chat.id, 'https://www.amazon.in/Katyayani-Organic-Fungicide-Vegetable-Disease/dp/B082GDFTSX/ref=asc_df_B082GDFTSX/?tag=googleshopdes-21&linkCode=df0&hvadid=397081286768&hvpos=&hvnetw=g&hvrand=10906546266793390089&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007785&hvtargid=pla-862811653136&psc=1&ext_vrnc=hi')
        
        
        elif(x == 'Potato___Late_blight'):
            bot.send_message(message.chat.id, 'https://www.amazon.in/BAVISTIN-50-W-P-Systematic-Fungicide/dp/B07DQL6VT6/ref=asc_df_B07DQL6VT6/?tag=googleshopdes-21&linkCode=df0&hvadid=397009291831&hvpos=&hvnetw=g&hvrand=5148260506538894548&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007785&hvtargid=pla-838319413916&psc=1&ext_vrnc=hi')
        
        
        elif(x =='Tomato_Bacterial_spot'):
            bot.send_message(message.chat.id, 'A plant with bacterial spots cannot be cured. Remove symptomatic plants from the field to prevent the spread of bacteria to healthy plants.')
            
        elif(x == 'Tomato_Early_blight'):
            bot.send_message(message.chat.id, 'https://www.flipkart.com/upl-saaf-fungicide-carbendazim-12-mancozeb-63-wp-fertilizer/p/itmebdd6b2f0591a?pid=SMNFVDFQNYHJXHQG&lid=LSTSMNFVDFQNYHJXHQG68LQWG&marketplace=FLIPKART&tgi=sem,1,G,11214002,g,search,,161598646720,,,,c,,,,,,,&ef_id=CjwKCAjwos-HBhB3EiwAe4xM99p5_KOfkws3QYrSEjFnr3FNnWNaGnGcAom15IE6pfAD-RnTF70keBoCPnoQAvD_BwE:G:s&s_kwcid=AL!739!3!161598646720!!!g!305088224822!&gclsrc=aw.ds')
            
        elif(x == 'Tomato_Late_blight'):
            bot.send_message(message.chat.id, 'https://dir.indiamart.com/items/dupont-equation-pro-fungicide-200-ml-s137315.html')
            #bot.send_message(message.chat.id, x)
        elif(x == 'Tomato_Leaf_Mold'):
            bot.send_message(message.chat.id, 'https://www.amazon.in/Syngenta-Folio-Gold-Chlorothalonil-Metalaxyl-M/dp/B08YND5F8X/ref=asc_df_B08YND5F8X/?tag=googleshopdes-21&linkCode=df0&hvadid=397083402899&hvpos=&hvnetw=g&hvrand=6741642405898273846&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007785&hvtargid=pla-1360133612146&psc=1&ext_vrnc=hi')
            
        elif(x == 'Tomato_Septoria_leaf_spot'):
            bot.send_message(message.chat.id, 'https://www.amazon.in/3N-PD8E-MWY4-Potassium-Bicarbonate-1-lb/dp/B0064GZPU4/ref=sr_1_1?dchild=1&keywords=potassium+bicarbonate&qid=1626593638&sr=8-1')
        
        elif(x== 'Tomato_Spider_mites_Two_spotted_spider_mite'):
            bot.send_message(message.chat.id, 'https://www.amazon.in/Syngenta-Thionutri-Sulphur-Contact-Fungicide/dp/B08QN7WNGR/ref=asc_df_B08QN7WNGR/?tag=googleshopdes-21&linkCode=df0&hvadid=397080886040&hvpos=&hvnetw=g&hvrand=7610468782617145822&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007785&hvtargid=pla-1174523286703&psc=1&ext_vrnc=hi')
        
        elif(x== 'Tomato__Target_Spot'):
            bot.send_message(message.chat.id, 'https://www.google.com/aclk?sa=L&ai=DChcSEwjRyuash-zxAhVTrZYKHQqxC0gYABAHGgJ0bA&ae=2&sig=AOD64_2XtDQkU3InUH4TGsLKyTH97-jWeg&ctype=5&q=&ved=2ahUKEwiYsdesh-zxAhX5qksFHUIWBAoQ9aACegQIAhBQ&adurl=')
        
        elif(x== 'Tomato__Tomato_YellowLeaf__Curl_Virus'):
            bot.send_message(message.chat.id, 'https://www.amazon.in/Abtec-Bio-Neem-Plant-Pesticide/dp/B072HZSPDL')
            
        elif(x=='Tomato__Tomato_mosaic_virus'):
            bot.send_message(message.chat.id, 'No medicine can be used. Remove the infected parts as soon as possible to minimize damage.')
        
        
    elif message.text.lower() == 'moisture':
        bot.send_message(message.chat.id, 'checking soil!')
        a = soilv2.soilID()
        bot.send_message(message.chat.id, a)
    
    elif message.text.lower() == 'birds':
        bot.send_message(message.chat.id, 'Checking for birds. Please wait')
        a = bird.birdid()
        bot.send_message(message.chat.id, a)

bot.polling()
