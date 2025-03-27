**Edge Computing**
> Edge Computing ist ein verteiltes Computing-Framework.
> Beim Edge Computing finden die relevanten Operationen am Rand des Netzwerkes, in der Netzwerkperipherie statt. 
> Diese Operationen wie z.B. die Datenerfassung, die Datenanalyse usw. werden direkt dort berechnet, wo die Daten entstehen werden.
> Bei Anwendungen des IoT und bei Anwendungen, die Reaktionen in Echtzeit voraussetzen.
> **Vorteile** :
>	> Je höher die physische Distanz ist, desto größer sind die Verzögerungszeit und die Reaktionszeit. Beim Edge Computing wird die Berechnung physisch näher an die Quelle der Daten. Auf diese Weise wird die Reaktionszeit deutlich verringert.
>	> Außerdem werden Daten gefiltert, nur die benötigte Daten werden an das Rechenzentrum übertragen, was zur effizienten Verwendung der verfügbaren Bandbreite führt.
>	> Reduzierung von Netzwerkkosten
>	> Verbesserte Kontrollierbarkeit vertraulicher Daten
> **Nachteile**:
> 	> Sicherheit der Daten muss gewährleistet sein
> 	> Zuverlässigkeit des Betriebs auch bei Verbindungsabbruch muss gesichert sein
> 	> Ständige Verfügbarkeit der Geräte muss gewährleistet sein
> 	
> Ein belibiges Beispiel für dieses Muster ist die Gesichtserkennung aktueller Smartphones, die verwendet wird, um das Gerät zu entsperren. Ohne das Edge Computing muss das Gerät die Daten zum Rechenzenter senden und dann auf eine Antwort warten und braucht immer eine aktive Verbindung zum Internet, um die Daten zu senden. Mit dem Edge Computing wird die Implementierung dieser Anwendung einfacher und effizienter, weil alle Berechnungen lokal auf dem Gerät gemacht werden.

Quelle : 
1- https://de.wikipedia.org/wiki/Edge_Computing
2- https://www.ibm.com/topics/edge-computing#:~:text=Edge%20computing%20is%20a%20distributed,times%20and%20better%20bandwidth%20availability.

If you want a Chrome extension that automatically translates any text you select with your mouse without needing to right-click and choose from a context menu, you can modify the extension to listen for text selection and trigger the translation immediately. Here’s how you can achieve this:

### Step 1: Modify the Background Script

You will need to use a content script to detect when text is selected. The content script will communicate with the background script (or directly handle translation if you prefer) when text is selected.

#### **Content Script (`content.js`):**

This script will be injected into every webpage, and it will listen for text selection events. When text is selected, it will send the selected text to the background for translation.

javascript

Copy code

`document.addEventListener('mouseup', function() {     let selectedText = window.getSelection().toString().trim();     if (selectedText.length > 0) {         chrome.runtime.sendMessage({text: selectedText});     } });`

#### **Background Script (`background.js`):**

This script will receive the selected text from the content script and call the translation API.

javascript

Copy code

``chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {     if (request.text) {         translateText(request.text);     } });  function translateText(selectedText) {     const apiKey = 'YOUR_API_KEY';     const url = `https://translation.googleapis.com/language/translate/v2?key=${apiKey}&q=${encodeURIComponent(selectedText)}&source=en&target=es`;      fetch(url)         .then(response => response.json())         .then(data => {             const translation = data.data.translations[0].translatedText;             alert('Translated Text: ' + translation);         })         .catch(error => console.error('Error translating text:', error)); }``

### Step 2: Update the Manifest File

You’ll need to include the content script in your `manifest.json` and ensure you have the necessary permissions.

#### **Manifest (`manifest.json`)**:

json

Copy code

`{     "manifest_version": 3,     "name": "Word Translator",     "version": "1.0",     "permissions": ["activeTab"],     "background": {         "service_worker": "background.js"     },     "content_scripts": [         {             "matches": ["<all_urls>"],             "js": ["content.js"]         }     ],     "action": {         "default_popup": "popup.html",         "default_icon": "icon.png"     } }`

### Step 3: Handle API Keys Securely

Keep in mind that exposing your API key directly in your script is not secure. Ideally, you should set up a backend server to handle API requests or use other secure methods to store and manage your API keys.

### Step 4: Load and Test the Extension

Follow the same steps as before to load your extension into Chrome and test it by selecting text on any web page. The translation should appear automatically, typically shown in an alert dialog, but you can modify this to show in a more user-friendly manner such as an overlay or a tooltip.

This implementation will translate text instantly after text selection, enhancing the user experience by removing the need to manually invoke the translation.