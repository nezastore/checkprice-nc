# CHECK PRICE NC

# Pengambilan Data Harga:

# Data harga NodeCoin dalam USD dan IDR diambil dari CoinGecko melalui API https://api.coingecko.com/api/v3/simple/price.
Format Pesan Telegram:

# Bot membuat pesan menggunakan format HTML yang berisi harga NodeCoin terbaru dan timestamp.
Interval Pembaruan:

# Harga NodeCoin diperiksa setiap 300 detik (5 menit). Anda bisa mengubah nilai variabel interval sesuai kebutuhan.
Mengirim Pesan Telegram:

# Pesan hanya dikirim jika harga NodeCoin berubah dari pembaruan sebelumnya.
Kesalahan:

# Jika gagal mendapatkan harga, bot akan mengirim pesan error ke chat.
# Cara Menjalankan
Ganti YOUR_TELEGRAM_BOT_TOKEN dengan token bot Telegram Anda.
Ganti YOUR_TELEGRAM_CHAT_ID dengan chat ID (grup atau pengguna).
Jalankan skrip dengan Python (NC.py).
Bot akan terus berjalan dan memberikan pembaruan harga NodeCoin secara otomatis.
