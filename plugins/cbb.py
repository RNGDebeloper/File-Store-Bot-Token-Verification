#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>Our Premium package offers several benefits, including:</b>\n\n• Direct channel links with no ad links.\n• On-demand collections and one daily request.\n• Special access to events.\n\n<b>Included Channels In This Plan:</b>\n• @JAV_Uncensoreds\n• @HentaiHomies\n• @Live_Action_Hentai_1\n• @nHentai_Mangas\n• @OnlyFans_Adult_Archive\n• @PornHub_Premium_Videoss\n• @Ongoing_hanimes Coming soon..\n\n<b>Pricing:</b>\n1 Month - $1\n3 Months - $5\n6 Months - $10\n9 Months - $15\n12 Months - $20\n\n<b>Payment Methods:</b>\n• Payeer Account: P1109704654\n• Crypto: DM : @Its_Sasuke_Uchiha For Address.\n\nIf you are interested in subscribing, Send a payment screenshot to @Its_Sasuke_Uchiha. (For Process Auto Verification)\n\n<b>Please note that this pricing is temporary and we will soon be increasing our prices, We also have limited seats available for Premium users.</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/Uchiha_Community/40'),
                        InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
