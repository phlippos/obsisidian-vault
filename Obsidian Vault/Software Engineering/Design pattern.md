### **Struktur Muster**
- Strukturmuster geben eine Lösung vor, wie Klassen und Objekte kombiniert werden können um größere und komplexe Strukturen zu bilden.
- Strukturelle Objekt Muster zeigen, wie Objekte kombiniert werden können, um deren Funktionalität zu erweitern.
- **Objektadapter**
	- Es fungiert als Brücke zwischen zwei inkompatiblen Schnittstellen und sorgt dafür, dass sie zusammenarbeiten. Dieses Muster umfasst eine einzelne Klasse, den sogenannten Adapter, der für die Verknüpfung von Funktionalitäten unabhängiger oder inkompatibler Schnittstellen verantwortlich ist.
		- //Nehmen wir an, Sie haben zwei Freunde, einen, der nur Englisch spricht, und einen, der nur Französisch spricht. Sie möchten, dass sie kommunizieren, aber es gibt eine Sprachbarriere.
		- - Sie fungieren als Adapter und übersetzen Nachrichten zwischen ihnen. Ihre Rolle ermöglicht es dem englischen Sprecher, Ihnen Nachrichten zu übermitteln, und Sie wandeln diese Nachrichten für die andere Person ins Französische um.
		- - Auf diese Weise ermöglicht Ihre Anpassung trotz der Sprachunterschiede eine reibungslose Kommunikation zwischen Ihren Freunden.
		- - Diese Rolle, die Sie spielen, ähnelt dem Adapter-Entwurfsmuster und schließt die Lücke zwischen inkompatiblen Schnittstellen.
	- **Komponenten des Adapterentwurfsmusters**
		- **Target**:Definiert die vom Client erwartete Schnittstelle. Es stellt den Satz von Operationen dar, die der Clientcode verwenden kann.
		- **Adaptee**:Die vorhandene Klasse oder das vorhandene System mit einer inkompatiblen Schnittstelle, die in das neue System integriert werden muss.
		- **Adapter**: Eine Klasse, die die Zielschnittstelle implementiert und intern eine Instanz des Adaptee verwendet, um sie mit der Zielschnittstelle kompatibel zu machen.
		- ![[Pasted image 20240511103429.png]]
	- **Decorator**
		- ****Mit dem Decorator-Entwurfsmuster**** können wir einem Objekt dynamisch Funktionalität und Verhalten hinzufügen, ohne das Verhalten anderer vorhandener Objekte innerhalb derselben Klasse zu beeinflussen. Wir nutzen Vererbung, um das Verhalten der Klasse zu erweitern. Dies geschieht zur Kompilierungszeit und alle Instanzen dieser Klasse erhalten das erweiterte Verhalten.
		- - Das Dekorator-Entwurfsmuster verwendet abstrakte Klassen oder Schnittstellen mit der Komposition, um den Wrapper zu implementieren.
		- - Decorator-Entwurfsmuster erstellen Decorator-Klassen, die die ursprüngliche Klasse umschließen und zusätzliche Funktionalität bereitstellen, indem sie die Signatur der Klassenmethoden unverändert lassen.
		- Verfahren:
			- Erstellen Sie eine Schnittstelle.
			- Erstellen Sie konkrete Klassen, die dieselbe Schnittstelle implementieren.
			- Erstellen Sie eine abstrakte Dekoratorklasse, die dieselbe Schnittstelle wie oben implementiert.
			- Erstellen Sie eine konkrete Dekoratorklasse, die die obige abstrakte Dekoratorklasse erweitert.
			- 1. Verwenden Sie nun die oben erstellte konkrete Dekoratorklasse, um Schnittstellenobjekte zu dekorieren.
		- ![[Pasted image 20240511104350.png]]
		- ![[Pasted image 20240511104421.png]]
	- **Composite**
		- Es ermöglicht Kunden, einzelne Objekte und Objektkompositionen einheitlich zu behandeln. Mit anderen Worten: <mark style="background: #FFB86CA6;">Unabhängig davon, ob es sich um ein einzelnes Objekt oder eine Gruppe von Objekten (zusammengesetzt) ​​handelt</mark>, können Clients diese austauschbar verwenden.
		- **Komponenten**
			-  **Component**:Die Komponente deklariert die Schnittstelle für Objekte in der Komposition sowie für den Zugriff auf und die Verwaltung ihrer untergeordneten Komponenten.
			-  **Leaf***:Leaf definiert das Verhalten für primitive Objekte in der Komposition. Dies ist der Grundbaustein der Komposition und stellt einzelne Objekte dar, die keine untergeordneten Komponenten haben. Blattelemente implementieren die von der Komponentenschnittstelle definierten Operationen.
			- **Composite***:Composite speichert untergeordnete Komponenten und implementiert untergeordnete Vorgänge in der Komponentenschnittstelle. Dies ist eine Klasse mit untergeordneten Komponenten, bei denen es sich entweder um Blattelemente oder andere zusammengesetzte Elemente handeln kann. Eine zusammengesetzte Klasse implementiert die in der Komponentenschnittstelle deklarierten Methoden, häufig durch Delegieren der Vorgänge an ihre untergeordneten Komponenten.
			- ![[Pasted image 20240511105200.png]]
			- ![[Pasted image 20240511105231.png]]
	- ![[Pasted image 20240511105316.png]]
- **Erzeugungmuster**
	- Die Erzeugung eines Objektes soll ganz spezifisch gesteuert werden und folgt einem speziellen Muster.
	- In einem System werden zahlreiche Objekte erstellt. Die Variation der Objekte wird immer größer und komplexer. Die Erzeugung der Objekte wird ausgelagert, so dass die Objekte selbst nicht so komplex werden
	- **Singleton**
		- //Java Runtime
		- **Problem**:
			- von einer Klasse soll maximal eine Instanz exisitieren
			- die Instanz soll erstellt werden, wenn es noch keine gibt
			- wenn es schon eine Instanz gibt, soll diese benutzt werden
			- **Wann sollte das Designmuster der Singleton-Methode verwendet werden?**
				- - Es muss genau eine Instanz einer Klasse geben und diese muss für Clients von einem bekannten Zugangspunkt aus zugänglich sein.
				- - Wenn die einzige Instanz durch Unterklassen erweiterbar sein sollte und Clients in der Lage sein sollten, eine erweiterte Instanz ohne Änderungen zu verwenden
			- **Vor- und Nachteile**
				- Nachteile :
					- Singleton führt im Wesentlichen zu globalen Zuständen in einer Anwendung, was das Debugging und die Fehlersuche erschweren kann, da der Zustand von überall im Code verändert werden kann.
					- Die Verwendung des Singleton-Musters kann die Flexibilität der Softwarearchitektur einschränken.
				- Vorteile :
					- Singleton stellt sicher, dass eine Klasse nur eine einzige Instanz hat, was nützlich sein kann, wenn genau kontrolliert werden muss, wie und wo auf bestimmte Ressourcen zugegriffen wird. Dies ist oft der Fall bei Ressourcen, die systemweit nur einmal existieren sollten, wie z.B. Datenbankverbindungen oder Konfigurationsmanagementsysteme.
					- Da von der Singleton-Klasse nur eine Instanz erstellt wird, kann das Muster effizient mit Systemressourcen umgehen. Dies verhindert beispielsweise die mehrfache Instanziierung schwerer Objekte oder den übermäßigen Verbrauch von Ressourcen.
			- **Initialisierungstypen von Singleton**
				- **Eager Initialization (Frühzeitige Initialisierung)**
					-  Die Instanz der Singleton-Klasse wird bereits beim Laden der Klasse erstellt.
					- - Nachteil: Die Instanz wird unabhängig davon erstellt, ob sie jemals genutzt wird, was zu unnötigem Ressourcenverbrauch führen kann.
				- **Lazy Initialization (Verzögerte Initialisierung)**:
					- - Die Instanz wird erst erstellt, wenn sie das erste Mal benötigt wird.
					- - Vorteil: Ressourcenschonend, da die Instanz nur bei Bedarf erstellt wird.
					- - Nachteil: Die Standardimplementierung ist nicht threadsicher, was in multithreaded Umgebungen zu Problemen führen kann.
					- ![[Pasted image 20240511113822.png]]
	- **Factory Design Pattern**
		- Das Factory Method Design Pattern ist ein kreatives Designmuster, das in der Softwareentwicklung verwendet wird, um eine Schnittstelle zum Erstellen von Objekten in einer Oberklasse bereitzustellen und es gleichzeitig Unterklassen zu ermöglichen, den Typ der zu erstellenden Objekte zu ändern.
		- **Problem Ohne Factory-Methoden-Entwurfsmuster**
			- <mark style="background: #FFF3A3A6;">Starke Kopplung</mark>: Ohne das Factory-Muster kann der Code stark an spezifische Klassen gebunden sein, weil Objekte direkt innerhalb der Anwendungskomponenten instanziiert werden.
			- <mark style="background: #FFF3A3A6;">Schwierigkeiten bei der Erweiterung</mark>: Wenn neue Varianten oder Erweiterungen der Objekte eingeführt werden sollen, erfordert das direkte Erstellen von Objekten häufig Änderungen in vielen Teilen des Codes.
			- <mark style="background: #FFF3A3A6;">Probleme beim Unit-Testing</mark>: Das direkte Instanziieren von Klassen in Geschäftslogiken macht es schwierig, diese Logiken isoliert zu testen, da sie stark von den tatsächlichen Implementierungen der verwendeten Objekte abhängen.
		- **Wann sollte das Factory Method Design Pattern verwendet werden?**
			- **Wenn Sie die Objekterstellung kapseln möchten***
			- **Wenn Sie mehrere Produktvarianten unterstützen müssen***
		- **Komponenten**
			- **Creator**: Dies ist eine abstrakte Klasse oder eine Schnittstelle, die die Factory-Methode deklariert. Der Ersteller enthält normalerweise eine Methode, die als Factory zum Erstellen von Objekten dient.
			- **concrete Creator**: Konkrete Creator-Klassen sind Unterklassen des Creators, die die Factory-Methode implementieren, um bestimmte Objekttypen zu erstellen.
			- **Produkt**: Dies ist die Schnittstelle oder abstrakte Klasse für die Objekte, die die Factory-Methode erstellt. Das Produkt definiert die gemeinsame Schnittstelle für alle Objekte, die die Factory-Methode erstellen kann.
			- **Concrete Product**:Konkrete Produktklassen sind die tatsächlichen Objekte, die die Factory-Methode erstellt. Jede konkrete Produktklasse implementiert die Produktschnittstelle oder erweitert die abstrakte Produktklasse.
 ![[Pasted image 20240511120344.png]]
```java
// Library classes
abstract class Vehicle {
    public abstract void printVehicle();
}

class TwoWheeler extends Vehicle {
    public void printVehicle() {
        System.out.println("I am two wheeler");
    }
}

class FourWheeler extends Vehicle {
    public void printVehicle() {
        System.out.println("I am four wheeler");
    }
}

// Factory Interface
interface VehicleFactory {
    Vehicle createVehicle();
}

// Concrete Factory for TwoWheeler
class TwoWheelerFactory implements VehicleFactory {
    public Vehicle createVehicle() {
        return new TwoWheeler();
    }
}

// Concrete Factory for FourWheeler
class FourWheelerFactory implements VehicleFactory {
    public Vehicle createVehicle() {
        return new FourWheeler();
    }
}

// Client class
class Client {
    private Vehicle pVehicle;

    public Client(VehicleFactory factory) {
        pVehicle = factory.createVehicle();
    }

    public Vehicle getVehicle() {
        return pVehicle;
    }
}

// Driver program
public class GFG {
    public static void main(String[] args) {
        VehicleFactory twoWheelerFactory = new TwoWheelerFactory();
        Client twoWheelerClient = new Client(twoWheelerFactory);
        Vehicle twoWheeler = twoWheelerClient.getVehicle();
        twoWheeler.printVehicle();

        VehicleFactory fourWheelerFactory = new FourWheelerFactory();
        Client fourWheelerClient = new Client(fourWheelerFactory);
        Vehicle fourWheeler = fourWheelerClient.getVehicle();
        fourWheeler.printVehicle();
    }
}
```
- **Abstrakte Fabrikmuster**
	- Das Abstract Factory Pattern ist eine Möglichkeit, die Art und Weise zu organisieren, wie Sie Gruppen von Dingen erstellen, die miteinander in Beziehung stehen. Es enthält eine Reihe von Regeln oder Anweisungen, mit denen Sie verschiedene Arten von Dingen erstellen können, ohne genau zu wissen, um welche Dinge es sich handelt.
	- Abstrakte Fabrikmuster basieren auf einer Superfabrik, die andere Fabriken schafft.
	- **Vorteile**:
		- Isolierung konkreter Klassen.
		- Produktfamilien einfach austauschen: 
			- Die Klasse einer konkreten Fabrik kommt nur einmal in einer Anwendung vor, also dort, wo sie instanziiert wird.
			- Dies macht es einfach, die konkrete Fabrik zu ändern, die eine Anwendung verwendet.
			- Es können verschiedene Produktkonfigurationen verwendet werden, indem einfach die Betonfabrik gewechselt wird.
	- **Nachteile**:
		- Komplexität
		- Erhöhte Anzahl an Klassen
	- **Komponenten**:
		- **Abstrakte Fabrik**: Abstract Factory dient als übergeordneter Entwurf, der eine Reihe von Regeln zum Erstellen von Familien verwandter Objekte definiert, ohne deren konkrete Klassen anzugeben. Es deklariert eine Reihe von Methoden, von denen jede für die Erstellung eines bestimmten Objekttyps verantwortlich ist, und stellt sicher, dass konkrete Fabriken einer gemeinsamen Schnittstelle folgen, wodurch eine konsistente Möglichkeit zur Erstellung verwandter Objektsätze bereitgestellt wird.
		- **Concrete Factory**:Konkrete Fabriken implementieren die von der abstrakten Fabrik festgelegten Regeln. Es enthält die Logik zum Erstellen bestimmter Instanzen von Objekten innerhalb einer Familie. Es können auch mehrere Betonfabriken existieren, die jeweils darauf zugeschnitten sind, eine bestimmte Familie verwandter Objekte herzustellen.
		- **Abstrakte Produkte**:Abstrakte Produkte stellen eine Familie verwandter Objekte dar, indem sie eine Reihe gemeinsamer Methoden oder Eigenschaften definieren.
		- **Concrete Product**:Sie sind die tatsächlichen Instanzen von Objekten, die von Betonfabriken hergestellt wurden. Sie implementieren die in den abstrakten Produkten deklarierten Methoden, stellen die Konsistenz innerhalb einer Familie sicher und gehören zu einer bestimmten Kategorie oder Familie verwandter Objekte.
	- Stellen Sie sich vor, Sie leiten ein globales Automobilunternehmen. Sie möchten ein System entwerfen, um Autos mit spezifischen Konfigurationen für verschiedene Regionen wie Nordamerika und Europa zu erstellen. Jede Region hat möglicherweise eigene Anforderungen und Vorschriften, und Sie möchten sicherstellen, dass die für jede Region hergestellten Autos diese Standards erfüllen.
	- ![[Pasted image 20240511124112.png]]
```java
public interface Car{
	void display();
}
public interface CarSpecification{
	void specification();
}
public class NorthAmericaSpec implements CarSpecification{
	public void specification(){
		System.out.println("North america spec");
	}
}
public class EuropaSpec implements CarSpecification{
	public void specification(){
		System.out.println("Europa spec");
	}
}
public class Sedan implements Car{
	public void display(){
		System.out.println("Sedan");
	}
}
public class Hatchback implements Car{
	public void display(){
		System.out.println("Hatchback");
	}
}

public interface CarFactory{
	Car createCar();
	CarSpecification createSpecification();
}

public class EuropaCarFactory implements CarFactory{
	public Car createCar(){
		return new Hatchback();
	}
	public CarSpecification createSpecification(){
		return new EuropaSpec();
	}
}

public class NorthAmericaCarFactory implements CarFactory{
	public Car createCar(){
		return new Sedan();
	}
	public CarSpecification createSpecification(){
		return new NorthAmericaSpec();
	}
}

public class CarFactoryClient{
	public static void main(String argv){
		CarFactory europaCarFactory = new EuropaCarFactory();
		Car europaCar1 = europaCarFactory.createCar();
		CarSpecification europaCarSpec1 = europaCarFactory.createSpecification(); 
		europaCar1.display();
		europaCarSpec1.specification();
	}

}
```
- **Verhaltensmuster**
	- **Observer**:
		- mehrere Objekte sind am Zustand eines anderen Objektes interessiert
		- Das Beobachter-Entwurfsmuster ist ein Verhaltensentwurfsmuster, das eine Eins-zu-viele-Abhängigkeit zwischen Objekten definiert, sodass alle abhängigen Objekte (Observer) automatisch benachrichtigt und aktualisiert werden, wenn ein Objekt (das Subjekt) seinen Zustand ändert.
		- Es befasst sich hauptsächlich mit der Interaktion und Kommunikation zwischen Objekten und konzentriert sich insbesondere darauf, wie sich Objekte als Reaktion auf Änderungen im Zustand anderer Objekte verhalten.
		- **Komponenten**:
			- **Subject**:Das Subjekt führt eine Liste von Observer. Es stellt Methoden zum dynamischen Registrieren und Aufheben der Registrierung von Observer bereit und definiert eine Methode,um Observer über Zustandsänderungen zu benachrichtigen.
			- **Observer**:Observer definiert eine Schnittstelle mit einer Aktualisierungsmethode, die konkrete Beobachter implementieren müssen, und stellt eine gemeinsame oder konsistente Möglichkeit sicher, dass konkrete Beobachter Aktualisierungen vom Subjekt erhalten. Konkrete Beobachter implementieren diese Schnittstelle und können so auf Veränderungen im Zustand des Subjekts reagieren.
			- **KonkretesSubjekt** : ConcreteSubjects sind spezifische Implementierungen des Subjekts. Sie enthalten den tatsächlichen Zustand oder Daten, die Beobachter verfolgen möchten. Wenn sich dieser Zustand ändert, benachrichtigen konkrete Subjekte ihre Beobachter. Wenn es sich beispielsweise um eine Wetterstation handelt, wären bestimmte Wetterstationen an verschiedenen Standorten konkrete Themen.
			- **ConcreteObserver**:Concrete Observer implementiert die Observer-Schnittstelle. Sie registrieren sich bei einem konkreten Thema und reagieren, wenn ihnen eine Zustandsänderung mitgeteilt wird. Wenn sich der Zustand des Subjekts ändert, wird die Methode des konkreten Beobachters `update()`aufgerufen, die es ihm ermöglicht, entsprechende Maßnahmen zu ergreifen. In einem praktischen Beispiel ist eine Wetter-App auf Ihrem Smartphone ein konkreter Beobachter, der auf Änderungen einer Wetterstation reagiert.
![[Pasted image 20240511143406.png]]![[Pasted image 20240511143417.png]]
![[Pasted image 20240511143428.png]]
![[Pasted image 20240511143439.png]]
![[Pasted image 20240511143524.png]]

- **Model View Controller Design Pattern**
	- Das ****Model View Controller**** (MVC)-Entwurfsmuster gibt an, dass eine Anwendung aus einem Datenmodell, Präsentationsinformationen und Steuerinformationen besteht. Das Muster erfordert, dass jedes davon in verschiedene Objekte unterteilt wird.
	- - Das MVC-Muster unterteilt die Belange einer Anwendung in drei verschiedene Komponenten, von denen jede für einen bestimmten Aspekt der Funktionalität der Anwendung verantwortlich ist.
	- - Diese Trennung von Belangen erleichtert die Wartung und Erweiterung der Anwendung, da Änderungen an einer Komponente keine Änderungen an den anderen Komponenten erfordern.
	- **Vorteile**:
		- - ***Modularität:** Jede Komponente (Modell, Ansicht, Controller) kann separat entwickelt und getestet werden, was die Wiederverwendbarkeit und Skalierbarkeit des Codes fördert.
		- - ***Flexibilität:** Da die Komponenten unabhängig sind, wirken sich Änderungen an einer Komponente nicht auf die anderen aus, was einfachere Aktualisierungen und Änderungen ermöglicht.
		- 
	- ![[Pasted image 20240511144413.png]]
	- **Komponenten**
		- **Model**: Die Modellkomponente im MVC-Entwurfsmuster (Model-View-Controller) repräsentiert die Daten und Geschäftslogik einer Anwendung. Es ist für die Verwaltung der Anwendungsdaten, die Verarbeitung von Geschäftsregeln und die Reaktion auf Informationsanfragen von anderen Komponenten wie der Ansicht und dem Controller verantwortlich.
		- **View**: Zeigt dem Benutzer die Daten vom Modell an und sendet Benutzereingaben an den Controller.
		- **Controller**: Der Controller fungiert als Vermittler zwischen dem Modell und der Ansicht. Es verarbeitet Benutzereingaben und aktualisiert das Modell entsprechend und aktualisiert die Ansicht, um Änderungen im Modell widerzuspiegeln. Es enthält Anwendungslogik, wie z. B. Eingabevalidierung und Datentransformation.
		- ![[Pasted image 20240511145249.png]]
		- ![[Pasted image 20240511145306.png]]
		- ![[Pasted image 20240511145318.png]]
		- ![[Pasted image 20240511145330.png]]
	- **Template Method**
		- Das Template-Methodemuster ist ein Verhaltensentwurfsmuster,das das Grundgerüst eines Algorithmus oder von Operationen in einer (häufig abstrakten) Oberklasse definiert und die Implementierung der Details durch die untergeordneten Klassen überlässt. Es ermöglicht Unterklassen, bestimmte Teile des Algorithmus anzupassen, ohne seine Gesamtstruktur zu ändern. 
		- **Komponenten**:
			- **Abstrakte Klasse (oder Schnittstelle)**:Dies ist die Oberklasse, die die Vorlagenmethode definiert. Es stellt ein Grundgerüst für den Algorithmus bereit, in dem bestimmte Schritte definiert werden, andere jedoch abstrakt bleiben oder als Hooks definiert werden, die von Unterklassen überschrieben werden können. Es kann auch konkrete Methoden enthalten, die allen Unterklassen gemeinsam sind und innerhalb der Vorlagenmethode verwendet werden.
			- **Vorlagenmethode**:Dies ist die Methode innerhalb der abstrakten Klasse, die die gesamte Algorithmusstruktur definiert, indem sie verschiedene Schritte in einer bestimmten Reihenfolge aufruft. Sie wird oft als final deklariert, um zu verhindern, dass Unterklassen die Struktur des Algorithmus ändern.
			- **Abstrakte (oder Hook-)Methoden**: Dies sind Methoden, die innerhalb der abstrakten Klasse deklariert, aber nicht implementiert sind. Sie dienen als Platzhalter für Schritte im Algorithmus, die von Unterklassen implementiert werden sollen. Unterklassen müssen konkrete Implementierungen für diese Methoden bereitstellen, um den Algorithmus zu vervollständigen.
			- **Konkrete Unterklassen**:Dies sind die Unterklassen, die die abstrakte Klasse erweitern und konkrete Implementierungen für die in der Oberklasse definierten abstrakten Methoden bereitstellen. Jede Unterklasse kann bestimmte Schritte des Algorithmus überschreiben, um das Verhalten anzupassen, ohne die Gesamtstruktur zu ändern.
			- ![[Pasted image 20240511151302.png]]
			- ![[Pasted image 20240511151320.png]]
			- ![[Pasted image 20240511151330.png]]![[Pasted image 20240511151336.png]]
			- ![[Pasted image 20240511151350.png]]