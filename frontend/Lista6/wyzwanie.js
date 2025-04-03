// WYZWANIE 1
// Hoisting to mechanizm w js, w którym deklaracje zmiennych i funkcji są przenoszone na górę swojego zakresu jeszcze przed wykonaniem kodu
// funkcja przypisana do zmiennej nie jest hoistowana, ale funkcje deklarowane są hoistowane
// var jest hoistowany, ale nie jest inicjalizowany, więc jego wartość to undefined
// let i const są hoistowane, ale nie mogą być używane przed ich deklaracją (ReferenceError)

//console.log(capitalize("alice"));
// const capitalize = (str) => {
//   return str.charAt(0).toUpperCase() + str.slice(1);
// };

console.log(capitalize("alice"));
function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

//------------------------------------------------------------------

// WYZWANIE 2

function capitalizeSentence(sentence) {
  const words = sentence.split(" ");
  const capitalizedWords = words.map((word) => {
    return capitalize(word);
  });
  return capitalizedWords.join(" ");
}

console.log(capitalizeSentence("alice"));
console.log(capitalizeSentence("alice in wonderland"));

//------------------------------------------------------------------

// WYZWANIE 3

// kod z wykladu
const ids = [];

const generateId = () => {
  let id = 0;

  do {
    id++;
  } while (ids.includes(id));

  ids.push(id);
  return id;
};

console.time("generateId");

for (let i = 0; i < 3000; i++) {
  generateId();
}

console.timeEnd("generateId");

// alternatywa 1: uzycie seta

const idsSet = new Set();
const generateIdSet = () => {
  let id = 0;

  do {
    id++;
  } while (idsSet.has(id));

  idsSet.add(id);
  return id;
};

console.time("generateIdSet");
for (let i = 0; i < 3000; i++) {
  generateIdSet();
}
console.timeEnd("generateIdSet");

// alternatywa 2: uzycie generatora -> najszybsza opcja, ale zmieniamy sposob generowania id

function* generateIdGenerator() {
  let id = 0;
  while (true) {
    id++;
    yield id;
  }
}

const idGenerator = generateIdGenerator();
console.time("idGenerator");
for (let i = 0; i < 3000; i++) {
  idGenerator.next();
}
console.timeEnd("idGenerator");

//------------------------------------------------------------------

// WYZWANIE 4

function compareObjects(a, b) {
  var aKeys = Object.keys(a); // zapisuje klucze obiektu a jako tablice
  var bKeys = Object.keys(b);

  if (aKeys.length !== bKeys.length) return false;

  for (var prop of aKeys) {
    if (!b.hasOwnProperty(prop)) return false; // sprawdza czy obiekt b ma dany klucz

    if (typeof a[prop] === "object" && a[prop] !== null && b[prop] !== null) { 
      if (!compareObjects(a[prop], b[prop])) return false;
    } else {
      if (a[prop] !== b[prop]) return false;
    }
  }
  return true;
}

const obj1 = {
  name: "Alice",
  age: 25,
  address: {
    city: "Wonderland",
    country: "Fantasy",
  },
};

const obj2 = {
  name: "Alice",
  age: 25,
  address: {
    city: "Wonderland",
    country: "Fantasy",
  },
};

const obj3 = {
  age: 25,
  address: {
    city: "Wonderland",
    country: "Fantasy",
  },
  name: "Alice",
};

const obj4 = {
  name: "Alice",
  age: 25,
  address: {
    city: "Not Wonderland",
    country: "Fantasy",
  },
};

const obj5 = {
  name: "Alice",
};

console.log("Should be True:", compareObjects(obj1, obj2));
console.log("Should be True:", compareObjects(obj1, obj3));
console.log("Should be False:", compareObjects(obj1, obj4));
console.log("Should be True:", compareObjects(obj2, obj3));
console.log("Should be False:", compareObjects(obj2, obj4));
console.log("Should be False:", compareObjects(obj3, obj4));
console.log("Should be False:", compareObjects(obj1, obj5));
console.log("Should be False:", compareObjects(obj5, obj1));

// ------------------------------------------------------------------

// WYZWANIE 5

let library = [];

const addBookToLibrary = (title, author, pages, isAvailable, ratings) => {
  if (typeof title !== "string" || title.trim() === "") {
    throw new Error("Title must be a non-empty string");
  }
  if (typeof author !== "string" || author.trim() === "") {
    throw new Error("Title must be a non-empty string");
  }
  if (typeof pages !== "number" || pages <= 0 || !Number.isInteger(pages)) {
    throw new Error("Pages must be a positive integer number");
  }
  if (typeof isAvailable !== "boolean") {
    throw new Error("isAvailable must be a boolean value");
  }
  if (!Array.isArray(ratings) || !ratings.every(r => typeof r === "number" && r >= 0 && r <= 5)) {
    throw new Error("Ratings must be an array of numbers between 0 and 5");
  }
  library.push({
    title,
    author,
    pages,
    available: isAvailable,
    ratings,
  });
};

addBookToLibrary("Harry Potter", "J.K. Rowling", 500, true, []); // poprawny rekord (tablica ratingow moze byc pusta)
//addBookToLibrary("  ", "J.K. Rowling", 500, true, []);
//addBookToLibrary(5, "J.K. Rowling", 500, true, []);
//addBookToLibrary("Harry Potter", "  ", 500, true, []);
//addBookToLibrary("Harry Potter", 5, 500, true, []);
//addBookToLibrary("Harry Potter", "J.K. Rowling", -5, true, []);
//addBookToLibrary("Harry Potter", "J.K. Rowling", 5.6, true, []);
//addBookToLibrary("Harry Potter", "J.K. Rowling", "five", true, [1, 2, 3]);
//addBookToLibrary("Harry Potter", "J.K. Rowling", 500, "true", []);
//addBookToLibrary("Harry Potter", "J.K. Rowling", 500, true, [1, 2, 3, 6]);
//addBookToLibrary("Harry Potter", "J.K. Rowling", 500, true, [1, 2, 3, "six"]);
