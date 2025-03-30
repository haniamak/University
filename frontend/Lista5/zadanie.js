// od 9 niezrobione

/**
 * @typedef {Object} Product
 * @property {number} id - Id produktu
 * @property {string} name - Nazwa produktu
 * @property {number} quantity - Liczba sztuk do zakupienia
 * @property {Date} purchaseBy - Data, do której produkt powinien być zakupiony
 * @property {boolean} isPurchased - Status informujący, czy produkt został zakupiony
 * @property {number} [pricePerUnit] - Opcjonalna cena za sztukę (tylko dla zakupionych produktów)
 */

/** @type {Product[]} */
const products = [];

/**
 * Funkcja generatora dla unikalnych id produktów.
 */
function* idGenerator() {
  let id = 1;
  while (true) {
    yield id++;
  }
}
const idGen = idGenerator();

/**
 * Dodaje produkt do listy zakupów.
 * @param {string} name - Nazwa produktu
 * @param {number} quantity - Liczba sztuk do zakupienia
 * @param {string} purchaseBy - Data, do której produkt powinien być zakupiony (format: YYYY-MM-DD)
 * @param {boolean} isPurchased - Status informujący, czy produkt został zakupiony
 * @param {number} [pricePerUnit] - Opcjonalna cena za sztukę (tylko dla zakupionych produktów)
 * @return {Product} Dodany produkt
 */
function addProduct(name, quantity, purchaseBy, isPurchased, pricePerUnit) {
    let product = {
      id: idGen.next().value,
      name,
      quantity,
      purchaseBy: new Date(purchaseBy),
      isPurchased: isPurchased
  };
    if (isPurchased) {
      product.pricePerUnit = pricePerUnit;
    }
    products.push(product);
    return product;
}

/**
 * Usuwa produkt z listy zakupów.
 * @param {number} id - Id produktu do usunięcia
 * @return {boolean} true, jeśli produkt został usunięty, false w przeciwnym wypadku
 */
function deleteProduct(id) {
  const index = products.findIndex(product => product.id === id);
  if (index !== -1) {
    products.splice(index, 1);
    return true;
  }
  return false;
}

/**
 * Edytuje nazwę produktu.
 * @param {number} id - Id produktu do edytowania
 * @param {string} newName - Nowa nazwa produktu
 * @return {boolean} true, jeśli nazwa została zmieniona, false w przeciwnym wypadku
 */
function editName(id, newName) {
  const product = products.find(product => product.id === id);
  if (product) {
    product.name = newName;
    return true;
  }
  return false;
}

/**
 * Edytuje status zakupu produktu.
 * @param {number} id - Id produktu do edytowania
 * @param {boolean} isPurchased - Nowy status zakupu
 * @return {boolean} true, jeśli status został zmieniony, false w przeciwnym wypadku
 */
function editIsPurchased(id, isPurchased) {
  const product = products.find(product => product.id === id);
  if (product) {
    product.isPurchased = isPurchased;
    return true;
  }
  return false;
}

/**
 * Edytuje ilość produktu.
 * @param {number} id - Id produktu do edytowania
 * @param {number} newQuantity - Nowa ilość produktu
 * @returns {boolean} true, jeśli ilość została zmieniona, false w przeciwnym wypadku
 */
function editQuantity(id, newQuantity) {  
  const product = products.find(product => product.id === id);
  if (product) {
    product.quantity = newQuantity;
    return true;
  }
  return false;
}

/**
 * Edytuje datę zakupu produktu.
 * @param {number} id - Id produktu do edytowania
 * @param {string} newDate - Nowa data zakupu (format: YYYY-MM-DD)
 * @returns {boolean} true, jeśli data została zmieniona, false w przeciwnym wypadku
 */
function editDate(id, newDate) {
  const product = products.find(product => product.id === id);
  if (product) {
    product.purchaseBy = new Date(newDate);
    return true;
  }
  return false;
}

/**
 * Funkcja przesuwająca produkt na początek listy i ustawiajaca produkt z poczatku na miejsce przesuwanego.
 * @param {number} id - Id produktu do przesunięcia na początek listy
 * @returns {Product[]|null} Zaktualizowana lista produktów lub null, jeśli produkt nie został znaleziony
 */
function listUp(id) {
  const product = products.find(product => product.id === id);
  if (product) {
    [products[0], products[id]] = [products[id], products[0]];
    return products;
  }
  return null;
}

/**
 * Zwraca wszystkie produkty z listy zakupów do kupienia dzis.
 * @returns {Product[]} Lista produktów
 */
function buyToday() {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const todayTime = today.getTime();

  const productsToBuy = products.filter(product => {
    const productDate = new Date(product.purchaseBy);
    productDate.setHours(0, 0, 0, 0);
    return productDate.getTime() === todayTime && !product.isPurchased;
  });

  return productsToBuy;
}


addProduct("Mleko", 2, "2025-03-31", false);
addProduct("Chleb", 1, "2025-03-31", false);
addProduct("Masło", 1, "2025-03-31", true, 12.99);
addProduct("Ser", 1, "2025-03-30", false, 12.99);
//console.log(products);
//console.log(deleteProduct(1));
//console.log(products);
// console.log(editName(1, "Jogurt"));
// console.log(products);
// console.log(editIsPurchased(1, true));
// console.log(products);
// console.log(editQuantity(1, 3));
// console.log(products);
// console.log(editDate(1, "2025-03-25"));
// console.log(products);
//console.log(listUp(2));
// console.log(buyToday());
//console.log(products);
