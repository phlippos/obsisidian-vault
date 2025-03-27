Bu dönem yazılım projesini V model kullanarak ilerleteceğiz(Bilmeyenler gidip araştırsın). Bu Modelin ilk aşaması Gereksinim analizi. Bu CUMA gününe kadar herkes öncelikli olarak kendi çalıştığı alanın gereksinimlerini tespit edip döküman hazırlıycak. CUMA günü akşam belirlenen saatte bu gereksinimleri konuşucaz, bunlara önem puanı vericez ve birbirine bağımlı olan gereksinimleri tespit edip. Grafiğini kurucaz. Bu Gereksinimler için sizlerin ne eğitimlere ihtiyacınız var bunları tespit edip bunlar için bir süre belirleyeceğiz.


Anforderungsanalyse : 
priorität : 1,2,3
funktionale :
- ROS : 
	- offboard : 
			- waypointe dronun hareket etmesi
			- kameradan tespit ettiği rakibe göre hareket
	- fake target :
			- random waypoint oluştur
			- random kamera koordinatı oluştur
	- Telemetry : 
			- şartnameden istenilen telemetri verileri toplanacak
			- yki ' ye gönderilecek
	- Kamikaze : 
			- karekod okuma 
	 -  Yasaklı alandan kaçış : 
			 - ???
	- YKİ :
			- seçilen rakibin telemetri verisi jetson'a gönderilecek.
- Computer Vision :
	- Dataset 
	- Sim testi (Yolov3)
		- dataset
	- Video kayıt ve bu kaydın aktarılması
	- Videonun aktarılması (canlı)
- Qgroundcontrol : 
	- front end tasarım
	- backend 
	- backend ve frontend bağlantıları
- Haberleşme : 
	- YKİ ve drone bağlantısı
	- Jetson ve px4 bağlantı
	- server
nicht funktionale : 
	- ROS2 Humble kodları c++ ile yazılacak 
		- topic -> custom topic
		- msg ->  custom msg
	- Ubuntu jammy 22.04
	- Gazebo ignition sim
		- custom model 
		- multivehicle test
		- Gazeboda test tüm görevler için
		- Gazeboda yeni dünya 
	- Qgroundcontrol
		- qt designer 
		- python
		- c++
	- Haberleşme :
		- Microxrce dds agent ve client
	- PX4-autopilot