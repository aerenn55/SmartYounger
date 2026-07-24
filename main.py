import random
import time

# Asistanın temel bilgi hafızası
hafiza = {
    "selam": ["Aleykümselam kral, hoş geldin!", "Selamlar! Nasıl yardımcı olabilirim?"],
    "naber": ["İyidir, terminalin içinde takılıyorum. Senden naber?", "Yuvarlanıp gidiyoruz, sen nasılsın?"],
    "kimsin": ["Ben SmartYounger! Senin bilgisayarında çalışan yerel asistanım."],
    "proje": ["Şu an Python ile harika bir mantık algoritması çalıştırıyorsun."]
}

print("🤖 SmartYounger Hazır! (Çıkmak için 'q' yaz)\n" + "="*45)

while True:
    girdi = input("\nSen: ").strip().lower()
    
    if girdi == 'q':
        print("\nAI: Görüşürüz kral, kendine iyi bak!")
        break
        
    if not girdi:
        continue
        
    print("AI düşünülüyor...")
    time.sleep(0.5)
    
    cevap_bulundu = False
    for anahtar in hafiza:
        if anahtar in girdi:
            print(f"\nAI: {random.choice(hafiza[anahtar])}")
            cevap_bulundu = True
            break
            
    if not cevap_bulundu:
        print(f"\nAI: '{girdi}' ne demek bilmiyorum. Bu mesaja ne cevap vermeliyim?")
        yeni_cevap = input("Sen (Öğret): ")
        
        if yeni_cevap:
            hafiza[girdi] = [yeni_cevap]
            print(f"AI: Anlaşıldı! Artık '{girdi}' dediğinde bunu hatırlayacağım.")
