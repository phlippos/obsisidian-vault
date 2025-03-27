C++’ta `std::vector`, dinamik bir dizi yapısıdır ve C++ Standard Library’nin bir parçasıdır. `std::vector`, bir dizi gibi sıralı bir veri kümesi tutar, ancak boyutu dinamik olarak değiştirilebilir.
- **Tanım**: `std::vector`, bir tür nesne koleksiyonu tutmak için kullanılır. Belirli bir türdeki nesneleri dinamik olarak saklar ve gerektiğinde boyutunu otomatik olarak ayarlayabilir.
    
- **Kapsam**: `#include <vector>
- 
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers; // Boş bir vector oluşturma
    std::vector<int> numbersWithSize(5); // 5 elemanlı bir vector oluşturma (default değerler ile)
    std::vector<int> initializedNumbers = {1, 2, 3, 4, 5}; // Başlangıç değerleri ile
	numbers.push_back(10); // Sonuna 10 ekler
	numbers.push_back(20); // Sonuna 20 ekler
	numbers.pop_back(); // Son elemanı siler
	int first = numbers[0]; // İlk elemana erişim
	int second = numbers.at(1); // İkinci elemana erişim (hata kontrolü var)
	std::cout << "Size: " << numbers.size() << std::endl; // Eleman sayısını verir
	std::cout << "Capacity: " << numbers.capacity() << std::endl; // Tahsis edilen hafıza boyutunu verir
	for (auto it = numbers.begin(); it != numbers.end(); ++it) {
	    std::cout << *it << " "; // Her elemanı yazdırır
	}
	

}


```
### 10. **Performans**

- `std::vector`, ardışık bellek alanları kullanır, bu da hızlı erişim sağlar.
- Ancak, çok fazla ekleme veya silme işlemi yapıldığında, bellek tahsisi ve kopyalama maliyetleri olabilir. Bu nedenle, `reserve()` fonksiyonunu kullanarak kapasite önceden belirlenebilir.
### 11. **Kısıtlamalar**

- `std::vector`, yalnızca elemanları ardışık bellekte tutar, bu nedenle ekleme ve silme işlemleri bazen yavaşlayabilir.
- Elemanlar, belirli bir türde olmalıdır (yani, tüm elemanlar aynı türde olmalıdır).