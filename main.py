import pyrogram
from pyrogram import *
from pyrogram.types import *
import requests
from telegraph import upload_file
import os



app = Client(
"APP",
api_id = int(os.environ["API_ID"]),
api_hash = os.environ["API_HASH"],
bot_token = os.environ["BOT_TOKEN"]
)


@app.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
       m = message.chat.id
       user = message.from_user.mention
       do = requests.get(f"https://api.telegram.org/bot{app_token}/getChatMember?chat_id=@{CHANNEL}&user_id={message.from_user.id}").text
       if do.count("left") or do.count("Bad Request: user not found"):
          await message.reply_text(f"**Join [this channel](t.me/{CHANNEL}) first to be able to use the app ✨**", disable_web_page_preview=True,
          reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                        "Join Channel ✨ .",
                        url=f'https://t.me/{CHANNEL}'),
                        ],
                    ]
                )
            ) 
       else:
         await app.send_photo(
		message.chat.id , 
		photo="https://telegra.ph/file/2824d32a8a264d5c2c94b.jpg",
		caption = f"""
اهلا {message.from_user.mention},
🔮أنا هنا لإنشاء روابط التلجراف لملفات الوسائط الخاصة بك.

👨🏼‍💻ما عليك سوى إرسال ملف وسائط صالح مباشرة إلى هذه الدردشة.
♻️انواع الملفات الصالحه هي:- 'jpeg', 'jpg', 'png', 'mp4' and 'gif'.

🌐لأنشاء الروابط في **المجموعات**,اضفني لمجموعه خارقه اي عامه وارسل الامر <code>/tl</code> ردا علي ملف وسائط صالح.
🖥 | [◜ 𝙼𝙰𝚈 𝙱𝙾𝚃𝚂 𓃠◞🌀](https://t.me/appatiiii)

🖥 | [◜ ♔... « 𝙷𝙼𝚂 » ...♔◞🌀](https://t.me/hms_00)

🖥 | [◜ ♡ آج‌ــ‌๋ـر ♡◞🌀](https://t.me/ddeneat)

🐼 | [ᯓ˹ 𝙷ٍْ𝙼ٍْ𝚂ْ 𓃠）⛧](https://t.me/hms_01)
            """,
            reply_markup=InlineKeyboardMarkup(
            [
            	[
            		InlineKeyboardButton(
            			text='ٱآلمོ ـطو₎​​​ر⁽ ',
            			user_id=916165019
            			)
            		],[
            		InlineKeyboardButton(
            			text='ِقنٱآهه ٱآلبو₎​​​تٖ ',
            			url='https://t.me/appatiiii'
            			)
            		],
            	]
            )
        )
   
#@app.on_message(filters.text & filters.group)
#async def gp(client,message):
#		m = message.chat.id
#		user = message.from_user.mention
#		do = requests.get(f"https://api.telegram.org/bot{app_token}/getChatMember?chat_id=@{CHANNEL}&user_id={message.from_user.id}").text
#		if do.count("left") or do.count("Bad Request: user not found"):
#		    await app.delete_messages(message.chat.id , message.id)
#		    await message.reply_text(f"Hy {message.from_user.mention} \n\n**Join [this channel](t.me/{CHANNEL}) first to speak here ✨**", disable_web_page_preview=True,
#          reply_markup=InlineKeyboardMarkup(
#                    [
#                        [
#                            InlineKeyboardButton(
#                        "Join Channel ✨ .",
#                        url=f'https://t.me/{CHANNEL}'),
#                        ],
#                    ]
#                )
#            ) 
#           
#		else:
#			pass
#			
@app.on_message(filters.media & filters.private)
async def glink(client, message):
    try:
        text = await message.reply("✦› جار المعالجة...")
        async def progress(current, total):
            await text.edit_text(f"📥 جار التحميل... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            lo = await message.download(location, progress=progress)
            await text.edit_text("📤 جار الرفع ...")
            up = upload_file(lo) 
            await text.edit_text(f"**◉ : تم الرفع بنجاح واليك الرابط...  **:\n\n<code>https://telegra.ph{up[0]}</code>",
            reply_markup=InlineKeyboardMarkup(
            [
            	[
            		InlineKeyboardButton(
            			text='ِقنٱآهه ٱآلبو₎​​​تٖ ',
            			url='https://t.me/botatiiii'
            			)
            		],
            	]
            )
        )     
            os.remove(lo) 
        except Exception as e:
            await text.edit_text(f"**⚠️ ¦ حدث خطأ **\n\n<i>**السبب**: {e}</i>")
            os.remove(lo) 
            return                 
    except Exception:
        pass        
  
#@app.on_message(filters.command(["/tl","/t","ت","تليجراف","تلكراف"],prefixes="") & filters.group)
#async def tele(client,message):
#	try:
#	   text = await message.reply("✦ جار المعالجة...")
#	   async def progress(current, total):
#            await text.edit_text(f"📥 جار التحميل... {current * 100 / total:.1f}%")
#            try:
#            	location = f"./media/group/"
#            	lo = await message.download(location, progress=progress)
#            	await text.edit_text("📤 جار الرفع ...")
#            	up = upload_file(lo) 
#            	await text.edit_text(f"**◉ : تم الرفع بنجاح واليك الرابط...  **:\n\n<code>https://telegra.ph{up[0]}</code>",
#            	reply_markup=InlineKeyboardMarkup(
#            [
#            	[
#            		InlineKeyboardButton(
#            			text='ِقنٱآهه ٱآلبو₎​​​تٖ ',
#            			url='https://t.me/botatiiii'
#            			)
#            		],
#            	]
#            )
#       		 )     
#            	os.remove(lo) 
#            except Exception as e:
#            	await text.edit_text(f"**⚠️ ¦ حدث خطأ **\n\n<i>**السبب**: {e}</i>")
#            	os.remove(lo) 
#            	return                 
#	except Exception:
#		pass
#		

@app.on_message(filters.command(['المطور','همس','سورس'],prefixes=""))
async def dev(client,message):
	await app.send_photo(
	message.chat.id , 
	photo="https://telegra.ph/file/352c68fbab79f70d74070.jpg",
	caption="""
	ـ• ┉ • ┉ • ┉ • ┉ • ┉ • 
⌯⁞ قنوات ذات صلة بالبوت↯

⌯⁞ ♡ آج‌ــ‌๋ـر ♡ ⋙ @ddeneat⌯

⌯ قناة تحديثات البوتات ♡ ⋙ @botatiiii⌯

⌯⁞ 🖤🥀 هنا كل مايلامس قلبي 🥀🖤 ⋙ @hms_00⌯

⌯⁞ بوت التواصل ♡ ⋙ @Towasolbot⌯
ـ ⋙    ♡ ⌯
"""
)
		
print('started⚠️')
app.run()