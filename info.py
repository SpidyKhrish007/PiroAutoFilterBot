import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
PORT = environ.get("PORT", "8000")
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '23830477'))
API_HASH = environ.get('API_HASH', '19f8365d98fb11c9cd6c1eaa8b1fa4b8')
BOT_TOKEN = environ.get('BOT_TOKEN', '6286222522:AAFLa7Gp_BkNPhdiXEMVthzYmA9q1rotZ3k')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
# Bot images & videos
PICS = (environ.get('PICS', 'https://te.legra.ph/file/4b536973fad1aad60f46b.jpg')).split()
NOR_IMG = environ.get("NOR_IMG",     "https://telegra.ph//file/451a9169cb4bca927080f.jpg",
    "https://telegra.ph//file/9fc8c8de06567f8ae2c2b.jpg",
    "https://telegra.ph//file/c529f35aacc3d2abc8506.jpg",
    "https://telegra.ph//file/510f122c639b622ff58d5.jpg",
    "https://telegra.ph//file/dd4c7a696ad93f61b8237.jpg",
    "https://telegra.ph//file/3dd35884409726bb73b36.jpg",
    "https://telegra.ph//file/8eb078168134871566d30.jpg",
    "https://telegra.ph//file/8d1d4b4a1ed2de4830273.jpg",
    "https://telegra.ph//file/1d28bcea826cc2a2c9799.jpg",
    "https://telegra.ph//file/89bac63888fedc062ccf9.jpg",
    "https://telegra.ph//file/e130508fd1c5a7afbce1d.jpg",
    "https://telegra.ph//file/78c87763cb140992f5ad6.jpg",
    "https://telegra.ph//file/dc92d039fa693acf5d979.jpg",
    "https://telegra.ph//file/e5cf0a4c1ce9e2c309bfe.jpg",
    "https://telegra.ph//file/50392bef6764d8b38b0bf.jpg",
    "https://telegra.ph//file/9206d428a468856bf1e0d.jpg",
    "https://telegra.ph//file/9d6efcb7813d9643067a7.jpg",
    "https://telegra.ph//file/f1a3d6b5a7f7f4ca36ee2.jpg",
    "https://telegra.ph//file/f07947ec8ee7c8560e19e.jpg",
    "https://telegra.ph//file/6660dc2786d6d4788d187.jpg",
    "https://telegra.ph//file/061fd49c54a12bb67e8f9.jpg",
    "https://telegra.ph//file/c1cbb94f2494d1aa528a3.jpg",
    "https://telegra.ph//file/0861d0d95232c6ff6adcd.jpg",
    "https://telegra.ph//file/1f6420b86cc6a4fc877c0.jpg",
    "https://telegra.ph//file/a78a305f1267b00f22ed4.jpg",
    "https://telegra.ph//file/73da3b58b9ce339670474.jpg",
    "https://telegra.ph//file/7a49738026138a2c062d9.jpg",
    "https://telegra.ph//file/fbe0918db37e0f48f30ba.jpg",
    "https://telegra.ph//file/6b07361706ff748816601.jpg",
    "https://telegra.ph//file/a8ec9b2c6db0f9bd6b3a8.jpg",
    "https://telegra.ph//file/7288b5da0fb688414deef.jpg",
    "https://telegra.ph//file/53a816b088124d3c66bc5.jpg",
    "https://telegra.ph//file/6ac56221904580d5d3441.jpg",
    "https://telegra.ph//file/f83b2d99b76e0ac35887d.jpg",
    "https://telegra.ph//file/390e16dcc796cfeb83577.jpg",
    "https://telegra.ph//file/4afbcbaba868f54e7a978.jpg",
    "https://telegra.ph//file/0b6fb808a8e24dae9ec1c.jpg",
    "https://telegra.ph//file/9e2d0a0af022d5ce1f29e.jpg",
    "https://telegra.ph//file/3411143bae8a8172af7e5.jpg",
    "https://telegra.ph//file/82a86dfb865384f3a7605.jpg",
    "https://telegra.ph//file/1649a05bfac2fe427c899.jpg",
    "https://telegra.ph//file/641f50719aa46c861b03b.jpg",
    "https://telegra.ph//file/195692b21de0a08c98e67.jpg",
    "https://telegra.ph//file/8893b4eafc1482fa1a9cc.jpg",
    "https://telegra.ph//file/dc3a6a9d4515bcba92738.jpg",
    "https://telegra.ph//file/3b67fbb27ec76733300d2.jpg",
    "https://telegra.ph//file/68b61bb9247d97e790a18.jpg",
    "https://telegra.ph//file/671337718cd6890dc6fc0.jpg",
    "https://telegra.ph//file/e3727d2204d61c5dde803.jpg",
    "https://telegra.ph//file/1f181a8a26415255079d7.jpg",
    "https://telegra.ph//file/7d74a6ffc20bb32c5965f.jpg",
    "https://telegra.ph//file/df934bd669d3fdce27c47.jpg",
    "https://telegra.ph//file/123c52599b60144a59a9c.jpg",
    "https://telegra.ph//file/7812a61812f1d21e87899.jpg",
    "https://telegra.ph//file/59a4a4e80675ef245772f.jpg",
    "https://telegra.ph//file/8f060e468a55b19d8b7f6.jpg",
    "https://telegra.ph//file/4b84bc8651f1712112755.jpg",
    "https://telegra.ph//file/65e0fe1f2d1bb2a3064ce.jpg",
    "https://telegra.ph//file/40a291550d830b600a052.jpg",
    "https://telegra.ph//file/f62474ef87f87c5f9c098.jpg",
    "https://telegra.ph//file/72f2a02a64218c0d04537.jpg",
    "https://telegra.ph//file/4133a958b124a519c6020.jpg",
    "https://telegra.ph//file/9abf5c4c8d35472536e0a.jpg",
    "https://telegra.ph//file/a846f83e78b5d84b6215f.jpg",
    "https://telegra.ph//file/6fd2b95a54bed69de5add.jpg",
    "https://telegra.ph//file/437f905fe9a8988d07f41.jpg",
    "https://telegra.ph//file/e1ebebf52ce8b2a749707.jpg",
    "https://telegra.ph//file/b877ee2028ebe45a41493.jpg",
    "https://telegra.ph//file/c7af99a1e5809772cafb2.jpg",
    "https://telegra.ph//file/54c502e96ce8505ae876e.jpg",
    "https://telegra.ph//file/d4174f0cdfb15f76f14b5.jpg",
    "https://telegra.ph//file/9859e28b47d7d7734b8f5.jpg",
    "https://telegra.ph//file/a396fb2e8771c5c4360a9.jpg",
    "https://telegra.ph//file/ff63898dcb9f74cdac179.jpg",
    "https://telegra.ph//file/84f57c7b814c33474231c.jpg",
    "https://telegra.ph//file/08a464bed5c135c212fb8.jpg",
    "https://telegra.ph//file/7282ef0777321f6e72a58.jpg",
    "https://telegra.ph//file/470058f042fba90717404.jpg",
    "https://telegra.ph//file/f1e1e9d31bc2a4d1e6798.jpg",
    "https://telegra.ph//file/15719217d3ad505f1346b.jpg",
    "https://telegra.ph//file/9c5aba59a85f1de92bd59.jpg",
    "https://telegra.ph//file/dde366c5b307679b25b1f.jpg",
    "https://telegra.ph//file/25d6e249f017b5c2a25e6.jpg",
    "https://telegra.ph//file/f042b7d173a57ec750082.jpg",
    "https://telegra.ph//file/7e7c20474b2f8601dce8f.jpg",
    "https://telegra.ph//file/fbb6e28a3b311dbb7df3b.jpg",
    "https://telegra.ph//file/79862f5ec9525f367f698.jpg",
    "https://telegra.ph//file/ca1d306c80e0ac0d524e5.jpg",
    "https://telegra.ph//file/04d7c9df026c3c2b75cfe.jpg",
    "https://telegra.ph//file/5da622b0a0b356cea1a4c.jpg")
MELCOW_VID = environ.get("MELCOW_VID",     "https://telegra.ph//file/451a9169cb4bca927080f.jpg",
    "https://telegra.ph//file/9fc8c8de06567f8ae2c2b.jpg",
    "https://telegra.ph//file/c529f35aacc3d2abc8506.jpg",
    "https://telegra.ph//file/510f122c639b622ff58d5.jpg",
    "https://telegra.ph//file/dd4c7a696ad93f61b8237.jpg",
    "https://telegra.ph//file/3dd35884409726bb73b36.jpg",
    "https://telegra.ph//file/8eb078168134871566d30.jpg",
    "https://telegra.ph//file/8d1d4b4a1ed2de4830273.jpg",
    "https://telegra.ph//file/1d28bcea826cc2a2c9799.jpg",
    "https://telegra.ph//file/89bac63888fedc062ccf9.jpg",
    "https://telegra.ph//file/e130508fd1c5a7afbce1d.jpg",
    "https://telegra.ph//file/78c87763cb140992f5ad6.jpg",
    "https://telegra.ph//file/dc92d039fa693acf5d979.jpg",
    "https://telegra.ph//file/e5cf0a4c1ce9e2c309bfe.jpg",
    "https://telegra.ph//file/50392bef6764d8b38b0bf.jpg",
    "https://telegra.ph//file/9206d428a468856bf1e0d.jpg",
    "https://telegra.ph//file/9d6efcb7813d9643067a7.jpg",
    "https://telegra.ph//file/f1a3d6b5a7f7f4ca36ee2.jpg",
    "https://telegra.ph//file/f07947ec8ee7c8560e19e.jpg",
    "https://telegra.ph//file/6660dc2786d6d4788d187.jpg",
    "https://telegra.ph//file/061fd49c54a12bb67e8f9.jpg",
    "https://telegra.ph//file/c1cbb94f2494d1aa528a3.jpg",
    "https://telegra.ph//file/0861d0d95232c6ff6adcd.jpg",
    "https://telegra.ph//file/1f6420b86cc6a4fc877c0.jpg",
    "https://telegra.ph//file/a78a305f1267b00f22ed4.jpg",
    "https://telegra.ph//file/73da3b58b9ce339670474.jpg",
    "https://telegra.ph//file/7a49738026138a2c062d9.jpg",
    "https://telegra.ph//file/fbe0918db37e0f48f30ba.jpg",
    "https://telegra.ph//file/6b07361706ff748816601.jpg",
    "https://telegra.ph//file/a8ec9b2c6db0f9bd6b3a8.jpg",
    "https://telegra.ph//file/7288b5da0fb688414deef.jpg",
    "https://telegra.ph//file/53a816b088124d3c66bc5.jpg",
    "https://telegra.ph//file/6ac56221904580d5d3441.jpg",
    "https://telegra.ph//file/f83b2d99b76e0ac35887d.jpg",
    "https://telegra.ph//file/390e16dcc796cfeb83577.jpg",
    "https://telegra.ph//file/4afbcbaba868f54e7a978.jpg",
    "https://telegra.ph//file/0b6fb808a8e24dae9ec1c.jpg",
    "https://telegra.ph//file/9e2d0a0af022d5ce1f29e.jpg",
    "https://telegra.ph//file/3411143bae8a8172af7e5.jpg",
    "https://telegra.ph//file/82a86dfb865384f3a7605.jpg",
    "https://telegra.ph//file/1649a05bfac2fe427c899.jpg",
    "https://telegra.ph//file/641f50719aa46c861b03b.jpg",
    "https://telegra.ph//file/195692b21de0a08c98e67.jpg",
    "https://telegra.ph//file/8893b4eafc1482fa1a9cc.jpg",
    "https://telegra.ph//file/dc3a6a9d4515bcba92738.jpg",
    "https://telegra.ph//file/3b67fbb27ec76733300d2.jpg",
    "https://telegra.ph//file/68b61bb9247d97e790a18.jpg",
    "https://telegra.ph//file/671337718cd6890dc6fc0.jpg",
    "https://telegra.ph//file/e3727d2204d61c5dde803.jpg",
    "https://telegra.ph//file/1f181a8a26415255079d7.jpg",
    "https://telegra.ph//file/7d74a6ffc20bb32c5965f.jpg",
    "https://telegra.ph//file/df934bd669d3fdce27c47.jpg",
    "https://telegra.ph//file/123c52599b60144a59a9c.jpg",
    "https://telegra.ph//file/7812a61812f1d21e87899.jpg",
    "https://telegra.ph//file/59a4a4e80675ef245772f.jpg",
    "https://telegra.ph//file/8f060e468a55b19d8b7f6.jpg",
    "https://telegra.ph//file/4b84bc8651f1712112755.jpg",
    "https://telegra.ph//file/65e0fe1f2d1bb2a3064ce.jpg",
    "https://telegra.ph//file/40a291550d830b600a052.jpg",
    "https://telegra.ph//file/f62474ef87f87c5f9c098.jpg",
    "https://telegra.ph//file/72f2a02a64218c0d04537.jpg",
    "https://telegra.ph//file/4133a958b124a519c6020.jpg",
    "https://telegra.ph//file/9abf5c4c8d35472536e0a.jpg",
    "https://telegra.ph//file/a846f83e78b5d84b6215f.jpg",
    "https://telegra.ph//file/6fd2b95a54bed69de5add.jpg",
    "https://telegra.ph//file/437f905fe9a8988d07f41.jpg",
    "https://telegra.ph//file/e1ebebf52ce8b2a749707.jpg",
    "https://telegra.ph//file/b877ee2028ebe45a41493.jpg",
    "https://telegra.ph//file/c7af99a1e5809772cafb2.jpg",
    "https://telegra.ph//file/54c502e96ce8505ae876e.jpg",
    "https://telegra.ph//file/d4174f0cdfb15f76f14b5.jpg",
    "https://telegra.ph//file/9859e28b47d7d7734b8f5.jpg",
    "https://telegra.ph//file/a396fb2e8771c5c4360a9.jpg",
    "https://telegra.ph//file/ff63898dcb9f74cdac179.jpg",
    "https://telegra.ph//file/84f57c7b814c33474231c.jpg",
    "https://telegra.ph//file/08a464bed5c135c212fb8.jpg",
    "https://telegra.ph//file/7282ef0777321f6e72a58.jpg",
    "https://telegra.ph//file/470058f042fba90717404.jpg",
    "https://telegra.ph//file/f1e1e9d31bc2a4d1e6798.jpg",
    "https://telegra.ph//file/15719217d3ad505f1346b.jpg",
    "https://telegra.ph//file/9c5aba59a85f1de92bd59.jpg",
    "https://telegra.ph//file/dde366c5b307679b25b1f.jpg",
    "https://telegra.ph//file/25d6e249f017b5c2a25e6.jpg",
    "https://telegra.ph//file/f042b7d173a57ec750082.jpg",
    "https://telegra.ph//file/7e7c20474b2f8601dce8f.jpg",
    "https://telegra.ph//file/fbb6e28a3b311dbb7df3b.jpg",
    "https://telegra.ph//file/79862f5ec9525f367f698.jpg",
    "https://telegra.ph//file/ca1d306c80e0ac0d524e5.jpg",
    "https://telegra.ph//file/04d7c9df026c3c2b75cfe.jpg",
    "https://telegra.ph//file/5da622b0a0b356cea1a4c.jpg")
SPELL_IMG = environ.get("SPELL_IMG",     "https://telegra.ph//file/451a9169cb4bca927080f.jpg",
    "https://telegra.ph//file/9fc8c8de06567f8ae2c2b.jpg",
    "https://telegra.ph//file/c529f35aacc3d2abc8506.jpg",
    "https://telegra.ph//file/510f122c639b622ff58d5.jpg",
    "https://telegra.ph//file/dd4c7a696ad93f61b8237.jpg",
    "https://telegra.ph//file/3dd35884409726bb73b36.jpg",
    "https://telegra.ph//file/8eb078168134871566d30.jpg",
    "https://telegra.ph//file/8d1d4b4a1ed2de4830273.jpg",
    "https://telegra.ph//file/1d28bcea826cc2a2c9799.jpg",
    "https://telegra.ph//file/89bac63888fedc062ccf9.jpg",
    "https://telegra.ph//file/e130508fd1c5a7afbce1d.jpg",
    "https://telegra.ph//file/78c87763cb140992f5ad6.jpg",
    "https://telegra.ph//file/dc92d039fa693acf5d979.jpg",
    "https://telegra.ph//file/e5cf0a4c1ce9e2c309bfe.jpg",
    "https://telegra.ph//file/50392bef6764d8b38b0bf.jpg",
    "https://telegra.ph//file/9206d428a468856bf1e0d.jpg",
    "https://telegra.ph//file/9d6efcb7813d9643067a7.jpg",
    "https://telegra.ph//file/f1a3d6b5a7f7f4ca36ee2.jpg",
    "https://telegra.ph//file/f07947ec8ee7c8560e19e.jpg",
    "https://telegra.ph//file/6660dc2786d6d4788d187.jpg",
    "https://telegra.ph//file/061fd49c54a12bb67e8f9.jpg",
    "https://telegra.ph//file/c1cbb94f2494d1aa528a3.jpg",
    "https://telegra.ph//file/0861d0d95232c6ff6adcd.jpg",
    "https://telegra.ph//file/1f6420b86cc6a4fc877c0.jpg",
    "https://telegra.ph//file/a78a305f1267b00f22ed4.jpg",
    "https://telegra.ph//file/73da3b58b9ce339670474.jpg",
    "https://telegra.ph//file/7a49738026138a2c062d9.jpg",
    "https://telegra.ph//file/fbe0918db37e0f48f30ba.jpg",
    "https://telegra.ph//file/6b07361706ff748816601.jpg",
    "https://telegra.ph//file/a8ec9b2c6db0f9bd6b3a8.jpg",
    "https://telegra.ph//file/7288b5da0fb688414deef.jpg",
    "https://telegra.ph//file/53a816b088124d3c66bc5.jpg",
    "https://telegra.ph//file/6ac56221904580d5d3441.jpg",
    "https://telegra.ph//file/f83b2d99b76e0ac35887d.jpg",
    "https://telegra.ph//file/390e16dcc796cfeb83577.jpg",
    "https://telegra.ph//file/4afbcbaba868f54e7a978.jpg",
    "https://telegra.ph//file/0b6fb808a8e24dae9ec1c.jpg",
    "https://telegra.ph//file/9e2d0a0af022d5ce1f29e.jpg",
    "https://telegra.ph//file/3411143bae8a8172af7e5.jpg",
    "https://telegra.ph//file/82a86dfb865384f3a7605.jpg",
    "https://telegra.ph//file/1649a05bfac2fe427c899.jpg",
    "https://telegra.ph//file/641f50719aa46c861b03b.jpg",
    "https://telegra.ph//file/195692b21de0a08c98e67.jpg",
    "https://telegra.ph//file/8893b4eafc1482fa1a9cc.jpg",
    "https://telegra.ph//file/dc3a6a9d4515bcba92738.jpg",
    "https://telegra.ph//file/3b67fbb27ec76733300d2.jpg",
    "https://telegra.ph//file/68b61bb9247d97e790a18.jpg",
    "https://telegra.ph//file/671337718cd6890dc6fc0.jpg",
    "https://telegra.ph//file/e3727d2204d61c5dde803.jpg",
    "https://telegra.ph//file/1f181a8a26415255079d7.jpg",
    "https://telegra.ph//file/7d74a6ffc20bb32c5965f.jpg",
    "https://telegra.ph//file/df934bd669d3fdce27c47.jpg",
    "https://telegra.ph//file/123c52599b60144a59a9c.jpg",
    "https://telegra.ph//file/7812a61812f1d21e87899.jpg",
    "https://telegra.ph//file/59a4a4e80675ef245772f.jpg",
    "https://telegra.ph//file/8f060e468a55b19d8b7f6.jpg",
    "https://telegra.ph//file/4b84bc8651f1712112755.jpg",
    "https://telegra.ph//file/65e0fe1f2d1bb2a3064ce.jpg",
    "https://telegra.ph//file/40a291550d830b600a052.jpg",
    "https://telegra.ph//file/f62474ef87f87c5f9c098.jpg",
    "https://telegra.ph//file/72f2a02a64218c0d04537.jpg",
    "https://telegra.ph//file/4133a958b124a519c6020.jpg",
    "https://telegra.ph//file/9abf5c4c8d35472536e0a.jpg",
    "https://telegra.ph//file/a846f83e78b5d84b6215f.jpg",
    "https://telegra.ph//file/6fd2b95a54bed69de5add.jpg",
    "https://telegra.ph//file/437f905fe9a8988d07f41.jpg",
    "https://telegra.ph//file/e1ebebf52ce8b2a749707.jpg",
    "https://telegra.ph//file/b877ee2028ebe45a41493.jpg",
    "https://telegra.ph//file/c7af99a1e5809772cafb2.jpg",
    "https://telegra.ph//file/54c502e96ce8505ae876e.jpg",
    "https://telegra.ph//file/d4174f0cdfb15f76f14b5.jpg",
    "https://telegra.ph//file/9859e28b47d7d7734b8f5.jpg",
    "https://telegra.ph//file/a396fb2e8771c5c4360a9.jpg",
    "https://telegra.ph//file/ff63898dcb9f74cdac179.jpg",
    "https://telegra.ph//file/84f57c7b814c33474231c.jpg",
    "https://telegra.ph//file/08a464bed5c135c212fb8.jpg",
    "https://telegra.ph//file/7282ef0777321f6e72a58.jpg",
    "https://telegra.ph//file/470058f042fba90717404.jpg",
    "https://telegra.ph//file/f1e1e9d31bc2a4d1e6798.jpg",
    "https://telegra.ph//file/15719217d3ad505f1346b.jpg",
    "https://telegra.ph//file/9c5aba59a85f1de92bd59.jpg",
    "https://telegra.ph//file/dde366c5b307679b25b1f.jpg",
    "https://telegra.ph//file/25d6e249f017b5c2a25e6.jpg",
    "https://telegra.ph//file/f042b7d173a57ec750082.jpg",
    "https://telegra.ph//file/7e7c20474b2f8601dce8f.jpg",
    "https://telegra.ph//file/fbb6e28a3b311dbb7df3b.jpg",
    "https://telegra.ph//file/79862f5ec9525f367f698.jpg",
    "https://telegra.ph//file/ca1d306c80e0ac0d524e5.jpg",
    "https://telegra.ph//file/04d7c9df026c3c2b75cfe.jpg",
    "https://telegra.ph//file/5da622b0a0b356cea1a4c.jpg")


# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1867884587').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001604178274').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001604178274')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL', '-1001828784633')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = -1001976227895
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Khrish:98982khrishisveryop07@cluster1.hh7bbcz.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster1")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001871138407'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MOVIES_HUB_ALPHA_DISCUSSION_2')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '<code>{file_name}</code>\n\n<b>━━━━━━━━━━•••••━━━━━━━━━\n🍿 Find any movie - 🏘 Backup - @MOVIES_HUB_ALPHA\n❤️ SHARE AND SUPPORT US</b>')
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", '<code>{file_name}</code>\n\n<b>━━━━━━━━━━•••••━━━━━━━━━\n🍿 Find any movie - 🏘 Backup - @MOVIES_HUB_ALPHA\n❤️ SHARE AND SUPPORT US</b>')
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", '🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10  \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [『 MOVIES HUB ALPHA 』](t.me/MOVIES_HUB_ALPHA)')
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
