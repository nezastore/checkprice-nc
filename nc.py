import time
import requests
from telegram import Bot
from datetime import datetime

# Token Telegram Bot
TELEGRAM_TOKEN = "7651087091:AAFSW9U3NxulCfmp7DYiktGRdM345BFyHeQ"
CHAT_ID = "-1002402298037"  # ID chat di mana bot akan mengirim pesan

# URL CoinGecko untuk mendapatkan harga NodeCoin
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Fungsi untuk mendapatkan harga NodeCoin dalam USD dan IDR
def get_nodecoin_price():
    try:
        params = {
            "ids": "nodecoin",
            "vs_currencies": "usd,idr"
        }
        response = requests.get(COINGECKO_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        usd_price = data["nodecoin"]["usd"]
        idr_price = data["nodecoin"]["idr"]
        return usd_price, idr_price

    except Exception as e:
        print(f"Error fetching price: {e}")
        return None, None

# Fungsi untuk mengirim pesan ke Telegram
def send_message(bot, chat_id, message):
    try:
        bot.send_message(chat_id=chat_id, text=message, parse_mode="HTML")
    except Exception as e:
        print(f"Error sending message: {e}")

# Fungsi utama bot
def main():
    bot = Bot(token=TELEGRAM_TOKEN)
    last_price_usd = None
    last_price_idr = None
    interval = 300  # Interval waktu pembaruan (dalam detik)

    while True:
        usd_price, idr_price = get_nodecoin_price()

        if usd_price is not None and idr_price is not None:
            # Format pesan
            message = (
                f"<b>NodeCoin Price Update</b>\n"
                f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                f"<b>USD:</b> ${usd_price:.4f}\n"
                f"<b>IDR:</b> Rp{idr_price:,.0f}"
            )

            # Kirim pesan hanya jika ada perubahan harga
            if usd_price != last_price_usd or idr_price != last_price_idr:
                send_message(bot, CHAT_ID, message)
                last_price_usd = usd_price
                last_price_idr = idr_price

        else:
            # Jika terjadi kesalahan, kirim pesan error
            error_message = "Failed to fetch NodeCoin price. Please check the API or internet connection."
            send_message(bot, CHAT_ID, error_message)

        time.sleep(interval)  # Tunggu sebelum pembaruan berikutnya

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bot stopped by user.")
