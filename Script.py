class script(object):
        START_TXT = """𝙷𝙴𝙻𝙾 {},
𝗠𝗬 𝗡𝗔𝗠𝗘 𝗜𝗦 <a href='https://t.me/FSLoki_bot'>𝗟𝗢𝗞𝗜 𝗟𝗔𝗨𝗙𝗘𝗦𝗢𝗡</a>, 𝗔 𝗨𝗡𝗟𝗜𝗠𝗜𝗧𝗘𝗗 𝗔𝗨𝗧𝗢𝗙𝗜𝗟𝗧𝗘𝗥 + 𝗙𝗜𝗟𝗧𝗘𝗥 𝗕𝗢𝗧 𝗪𝗜𝗧𝗛 𝗠𝗔𝗡𝗬 𝗔𝗕𝗜𝗟𝗜𝗧𝗜𝗘𝗦.

𝗬𝗢𝗨 𝗖𝗔𝗡 𝗨𝗦𝗘 𝗠𝗘 𝗜𝗡 𝗬𝗢𝗨'𝗥𝗘 𝗚𝗥𝗢𝗨𝗣 𝗕𝗬 𝗦𝗜𝗠𝗣𝗟𝗘 𝗦𝗧𝗘𝗣𝗦 𝗝𝗨𝗦𝗧 𝗔𝗗𝗗 𝗠𝗘 𝗜𝗡 𝗬𝗢𝗨'𝗥𝗘 𝗚𝗥𝗢𝗨𝗣 𝗔𝗡𝗗 𝗠𝗔𝗞𝗘 𝗠𝗘 𝗔𝗦 𝗔𝗗𝗠𝗜𝗡 𝗜𝗡 𝗬𝗢𝗨'𝗥𝗘 𝗚𝗥𝗢𝗨𝗣 𝗔𝗡𝗗 𝗦𝗘𝗘 𝗠𝗬 𝗣𝗢𝗪𝗘𝗥𝗦 🔥🔥

𝗔 𝗕𝗢𝗧 𝗠𝗔𝗜𝗡𝗧𝗔𝗜𝗡𝗘𝗗 𝗕𝗬 @TOM_HOLLA_ND"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: LOKI LAUFESON 
   Hellooo    {} 🤓
    
○ My Name : 𝗟𝗢𝗞𝗜 𝗟𝗔𝗨𝗙𝗘𝗦𝗢𝗡(http://t.me/FSLoki_bot)
○ Creator : Filmspoter(https://t.me/filmspoteradmin)
○ Language : 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
○ Library : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼(https://docs.pyrogram.org/)
○ Supported Site : Telegram(https://my.telegram.org/)
○ Source Code : Source(https://t.me/AdhavaaBiriyaniKittiyalo)
○ Server : Heroku(https://herokuapp.com)
○ Database : MongoDB(https://www.mongodb.com)
○ Build Status : v1.0.1 [ 𝙱𝙴𝚃𝙰 ]]"""
    

<b>𝗠𝗔𝗦𝗧𝗘𝗥:</b>
- <a href=https://t.me/filmspoteradmin>Filmspoter</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Loki should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Loki supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of tessa

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
