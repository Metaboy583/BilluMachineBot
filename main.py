
from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL")
OWNER_ID = os.environ.get("OWNER_ID")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
BOT_NAME = os.environ.get("BOT_NAME")
START_IMG1 = os.environ.get("START_IMG1")
START_IMG2 = os.environ.get("START_IMG2", None)
START_IMG3 = os.environ.get("START_IMG3", None)
START_IMG4 = os.environ.get("START_IMG4", None)
START_IMG5 = os.environ.get("START_IMG5", None)
START_IMG6 = os.environ.get("START_IMG6", None)
START_IMG7 = os.environ.get("START_IMG7", None)
START_IMG8 = os.environ.get("START_IMG8", None)
START_IMG9 = os.environ.get("START_IMG9", None)
START_IMG10 = os.environ.get("START_IMG10", None)
STKR = os.environ.get("STKR")
STKR1 = os.environ.get("STKR1", None)
STKR2 = os.environ.get("STKR2", None)
STKR3 = os.environ.get("STKR3", None)
STKR4 = os.environ.get("STKR4", None)
STKR5 = os.environ.get("STKR5", None)
STKR6 = os.environ.get("STKR6", None)
STKR7 = os.environ.get("STKR7", None)
STKR8 = os.environ.get("STKR8", None)
STKR9 = os.environ.get("STKR9", None)

bot = Client(
    "VickBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


PHOTO = [
    START_IMG1,
    START_IMG2,
    START_IMG3,
    START_IMG4,
    START_IMG5,
    START_IMG6,
    START_IMG7,
    START_IMG8,
    START_IMG9,
    START_IMG10,
]

EMOJIOS = [ 
      "๐ฎ๐ณ",
      "๐ฅ",
      "๐ช",
      "๐งจ",
      "โก",
      "๐คก",
      "๐ป",
      "๐",
      "๐ฉ",
      "๐",
]
      
STICKER = [
      STKR,
      STKR1,
      STKR2,
      STKR3,
      STKR4,
      STKR5,
      STKR6,
      STKR7,
      STKR8,
      STKR9,
]
START = f"""
**โญ สแดส, ษช แดแด [{BOT_NAME}]({START_IMG1})**
**โป แดแด ษช สแดSแดแด แดษด แดสแดแดสแดแด**
**โโโโโโโโโโโโโโ**
**โป แดsแดษขแด /chatbot [แดษด/แดาา]**
<b>||โญ สษชแด สแดสแด สแดแดแดแดษด าแดส สแดสแดโญ||</b>
"""
 
แดษดษดแดx สแดส= [
    [
        InlineKeyboardButton(text=" โญ แดแดกษดแดส โญ", url=f"tg://settings"),
        InlineKeyboardButton(text=" โซ ๊ฑแดแดแดแดสแด โซ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text=" โ แดแดแด แดแด สแดแดส แดสแดแด ษขสแดแดแด โ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text=" โฏ สแดสแด & แดแดแดs โฏ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text=" โ sแดแดสแดแด โ", callback_data="SOURCE"),
        InlineKeyboardButton(text="โ๏ธ แดสแดแดแด โ๏ธ", callback_data="ABOUT"),
    ],
]
PNG_BTN = [
    [
         InlineKeyboardButton(
             text=" ๐พ  แดแดแด แดแด สแดแดส แดสแดแด ษขสแดแดแด ๐พ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="๐ฅ sแดแดแดแดสแด ๐ฅ", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
HELP_READ = f"""
<u>**แดแดแดแดแดษดแดs าแดส {BOT_NAME}**</u>
<u>**แดสแด ษขษชแด?แดษด สแดสแดแดก!**</u>
**แดสส แดสแด แดแดแดแดแดษดแดs แดแดษด สแด แดsแดแด แดกษชแดส:/**
**โโโโโโโโโโโโโโ**
<b>||ยฉ๏ธ @{OWNER_USERNAME}||</b>
"""
BACK = [
     [
           InlineKeyboardButton(text=" โณ สแดแดแด โฝ", callback_data="BACK"),
     ],
]
HELP_BTN = [
     [
          InlineKeyboardButton(text="โฃ๏ธ แดสแดแดสแดแด โฃ๏ธ", callback_data="CHATBOT_CMD"),
          InlineKeyboardButton(text="๐ซ แดแดแดสs ๐ซ", callback_data="TOOLS_DATA"),
     ],
     [
          InlineKeyboardButton(text="โจ สแดแดแด โจ", callback_data="BACK"),
          InlineKeyboardButton(text=" โฝ แดสแดsแด โฝ", callback_data="CLOSE"),
     ],
]

CLOSE_BTN = [
      [
           InlineKeyboardButton(text=" โฝ แดสแดsแด โฝ", callback_data="CLOSE"),
      ],
]

CHATBOT_ON = [
        [
            InlineKeyboardButton(text="แดษดแดสสแด", callback_data=f"addchat"),
            InlineKeyboardButton(text="แดษชsแดสสแด", callback_data=f"rmchat"),
        ],
]

PNG_BTN = [
    [
         InlineKeyboardButton(
             text="๐งธ แดแดแด แดแด สแดแดส แดสแดแด ษขสแดแดแด ๐งธ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="โจ แดสแดsแด โจ", 
                              callback_data="CLOSE",
         ),
     ],
]

TOOLS_DATA_READ = f"""
<u>**แดแดแดสs าแดส {BOT_NAME} แดสแด:**</u>
**โป แดsแด `/repo` าแดส ษขแดแดแดษชษดษข sแดแดสแดแด แดแดแดแด!**
**โโโโโโโโโโโโโโ**
**โป แดsแด `/ping` าแดส แดสแดแดแดษชษดษข แดสแด แดษชษดษข แดา {BOT_NAME}**
**โโโโโโโโโโโโโโ**
<b>||ยฉ๏ธ @{OWNER_USERNAME}||</b>
"""

CHATBOT_READ = f"""
<u>**แดแดแดแดแดษดแดs าแดส {BOT_NAME}**</u>
**โป แดsแด `/chatbot` แดแด แดษดแดสสแด/แดษชsแดสสแด แดสแด แดสแดแดสแดแด.**
**เน ษดแดแดแด โป แดสแด แดสแดแด?แด แดแดแดแดแดษดแด าแดส แดสแดแดสแดแด แดกแดสแด ษชษด ษขสแดแดแด แดษดสส!!**
**โโโโโโโโโโโโโโโ**
<b>||ยฉ๏ธ @{OWNER_USERNAME}||</b>
"""
CHATBOT_BACK = [
        [     
              InlineKeyboardButton(text="โจ สแดแดแด โจ", callback_data="CHATBOT_BACK"),
              InlineKeyboardButton(text="โ แดสแดsแด โ", callback_data="CLOSE"),
        ],
]
HELP_START = [
     [
            InlineKeyboardButton(text="๐ สแดสแด ๐", callback_data="HELP"),
            InlineKeyboardButton(text=" โ แดสแดsแด โ", callback_data="CLOSE"),
     ],
]

HELP_BUTN = [
     [
           InlineKeyboardButton(text="๐ สแดสแด ๐", url=f"https://t.me/{BOT_USERNAME}?start=help"),
           InlineKeyboardButton(text=" โฝ แดสแดsแด โฝ", callback_data="CLOSE"),
     ],
]

ABOUT_BTN = [
      [
           InlineKeyboardButton(text=" โฝ sแดแดแดแดสแด โฝ", url=f"https://t.me/{SUPPORT_GRP}"),  
           InlineKeyboardButton(text="๐ สแดสแด ๐", callback_data="HELP"),
      ],
      [    
           InlineKeyboardButton(text="๐ค แดแดกษดแดส ๐ค", url=f"https://t.me/{OWNER_USERNAME}"), 
           InlineKeyboardButton(text="โ๏ธ sแดแดสแดแด โ๏ธ", callback_data="SOURCE"),
      ],
      [ 
           InlineKeyboardButton(text="๐ณ แดแดแดแดแดแดs ๐ณ", url=f"https://t.me/{UPDATE_CHNL}"),  
           InlineKeyboardButton(text="โจ สแดแดแด โจ", callback_data="BACK"),
      ],
]
SOURCE_READ = f"**สแดส, แดสแด sแดแดสแดแด แดแดแดแด แดา [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ษชs ษขษชแด?แดษด สแดสแดแดก.**\n**แดสแดแดsแด าแดสแด แดสแด สแดแดแด & ษขษชแด?แด แดสแด sแดแดส โฏ**\n**โโโโโโโโโโโโโโโโโโ**\n**สแดสแด ษชs แดสแด [sแดแดสแดแด แดแดแดแด](https://t.me/BilluMachineBot)**\n**โโโโโโโโโโโโโโโโโโ**\n**ษชา สแดแด าแดแดแด แดษดส แดสแดสสแดแด แดสแดษด แดแดษดแดแดแดแด แดแด [sแดแดแดแดสแด แดสแดแด](https://t.me/{SUPPORT_GRP}).\n<b>||ยฉ๏ธ @{OWNER_USERNAME}||</b>"

ABOUT_READ = f"""
**โป [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ษชs แดษด แดษช สแดsแดแด แดสแดแด-สแดแด.**
**โป [{BOT_NAME}](https://t.me/{BOT_USERNAME}) สแดแดสษชแดs แดแดแดแดแดแดแดษชแดแดสสส แดแด แด แดsแดส.**
**โป สแดสแดs สแดแด ษชษด แดแดแดษชแด?แดแดษชษดษข สแดแดส ษขสแดแดแดs.**
**โป แดกสษชแดแดแดษด ษชษด [แดสแดสแดษด](https://www.python.org) แดกษชแดส [แดแดษดษขแด-แดส](https://www.mongodb.com) แดs แด แดแดแดแดสแดsแด**
**โโโโโโโโโโโโโโ**
**โป แดสษชแดแด แดษด แดสแด สแดแดแดแดษดs ษขษชแด?แดษด สแดสแดแดก าแดส ษขแดแดแดษชษดษข สแดsษชแด สแดสแดฉ แดษดแด ษชษดาแด แดสแดแดแด [{BOT_NAME}](https://t.me/{BOT_USERNAME})**
"""
@bot.on_message(filters.command(["start", "aistart", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        accha = await m.reply_text(
            text = random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__แดฮนะธg แดฯะธg ๊จ๏ธ ััฮฑััฮนะธg..__")
        await asyncio.sleep(0.2)
        await accha.edit("__แดฮนะธg แดฯะธg ๊จ sัฮฑััฮนะธg.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__แดฮนะธg แดฯะธg ๊จ๏ธ sัฮฑััฮนะธg..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
            sticker = random.choice(STICKER),
        )
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo = random.choice(PHOTO),
            caption=f"""**เน สแดส, ษช แดแด [{BOT_NAME}](t.me/{BOT_USERNAME})**\n**โป แดษด แดษช สแดsแดแด แดสแดแดสแดแด.**\n**โโโโโโโโโโโโโโ**\n**โป แดsแดษขแด /chatbot [แดษด/แดาา]**\n<b>||เน สษชแด สแดสแด สแดแดแดแดษด าแดส สแดสแด||</b>""",
            reply_markup=InlineKeyboardMarkup(Annexboy),
        )
    else:
        await m.reply_photo(
                      photo = random.choice(PHOTO),
                      caption = START,
                      reply_markup = InlineKeyboardMarkup(HELP_START),
   )

@bot.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    vickdb = MongoClient(MONGO_URL)
    vick = vickdb["VickDb"]["Vick"]
    if query.data == "HELP":
        await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BTN),
                      disable_web_page_preview=True,
     )
    elif query.data == "CLOSE":
            await query.message.delete()
    elif query.data == "BACK":
            await query.message.edit(
                  text = START,
                  reply_markup=InlineKeyboardMarkup(DEV_OP),
     )
    elif query.data == "SOURCE":
            await query.message.edit(
                   text = SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,

     )
    elif query.data == "ABOUT":
            await query.message.edit(
                    text = ABOUT_READ,
                    reply_markup = InlineKeyboardMarkup(ABOUT_BTN),
                    disable_web_page_preview=True,
     )
    elif query.data == "ADMINS":
            await query.message.edit(
                    text = ADMIN_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data== "TOOLS_DATA":
            await query.message.edit(
                    text= TOOLS_DATA_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK),
     )
    elif query.data == "BACK_HELP":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN),
     )
    elif query.data == "CHATBOT_CMD":
            await query.message.edit(
                    text = CHATBOT_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK), 
     )
    elif query.data == "CHATBOT_BACK":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN), 
     )
    elif query.data == "addchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "You don't have permissions to do this baby.",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:           
                await query.edit_message_text(f"**แดสแดแด-สแดแด แดสสแดแดแดส แดษดแดสสแดแด.**")
            if is_vick:
                vick.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**แดสแดแด-สแดแด แดษดแดสสแดแด สส** {query.from_user.mention}.")
    elif query.data == "rmchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "**สแดแด แดแดษด'แด สแดแด?แด แดแดสแดs แดแด แดแด แดสษชs สแดสส!**",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                vick.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**แดสแดแด-สแดแด แดษชsแดสสแดแด สส** {query.from_user.mention}.")
            if is_vick:
                await query.edit_message_text("**แดสแดแด-สแดแด แดสสแดแดแดส แดษชsแดสสแดแด.**")
                            
@bot.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(
                   text= SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(CLOSE_BTN),
                   disable_web_page_preview = True,
      )
@bot.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        hmm = await m.reply_photo(
                            photo = random.choice(PHOTO),
                            caption = HELP_READ,
                            reply_markup= InlineKeyboardMarkup(HELP_BTN),
        )
    else:
        await m.reply_photo(
                      photo = random.choice(PHOTO),
                      caption = "**สแดส, แดแด แดแด าแดส สแดสแด แดแดแดแดแดษดแดs!**",
                      reply_markup = InlineKeyboardMarkup(HELP_BUTN),
      )


@bot.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(client, message: Message):
    await message.delete()
    start = datetime.now()
    wtfbhemchomd = await message.reply_sticker(
                       sticker= random.choice(STICKER),
    )
    end = datetime.now()
    ms = (end-start).microseconds / 1000
    await message.reply_photo(
        photo=random.choice(PHOTO),
        caption=f"ะฝey ะฒฮฑะฒั!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME})** ฮนั alฮนve ๐ฅ ฮฑnd worฤธฮนng าฮนne wฮนัะฝ a pฮนng oา\nโฅ `{ms}` ms\n\n<b>||ะผฮฑdั ฯฮนัะฝ โฃ๏ธ ะฒั [King๐](https://t.me/AnnexBoy)||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )

                  
@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"])
    & ~filters.private)
async def chatonoff(client: Client, message: Message):
    if not message.from_user:
        return
    else:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (await is_admins(chat_id)):
            return await message.reply_text(
                "**สแดแด แดสแด'ษดแด แดษด แดแดแดษชษด.**"
            )
        else:
            await message.reply_text(
            text="ยป <u>**แดสแดแดsแด แดษด แดแดฉแดษชแดษด แดแด แดษดแดสสแด/แดษชsแดสสแด แดสแดแดสแดแด.**</u>",
            reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
        )


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivate(client: Client, message: Message):
