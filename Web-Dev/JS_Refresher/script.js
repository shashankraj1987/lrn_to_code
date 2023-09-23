const data = [
  {
    id: 1,
    title: "The Lord of the Rings",
    publicationDate: "1954-07-29",
    author: "J. R. R. Tolkien",
    genres: [
      "fantasy",
      "high-fantasy",
      "adventure",
      "fiction",
      "novels",
      "literature",
    ],
    hasMovieAdaptation: true,
    pages: 1216,
    translations: {
      spanish: "El señor de los anillos",
      chinese: "魔戒",
      french: "Le Seigneur des anneaux",
    },
    reviews: {
      goodreads: {
        rating: 4.52,
        ratingsCount: 630994,
        reviewsCount: 13417,
      },
      librarything: {
        rating: 4.53,
        ratingsCount: 47166,
        reviewsCount: 452,
      },
    },
  },
  {
    id: 2,
    title: "The Cyberiad",
    publicationDate: "1965-01-01",
    author: "Stanislaw Lem",
    genres: [
      "science fiction",
      "humor",
      "speculative fiction",
      "short stories",
      "fantasy",
    ],
    hasMovieAdaptation: false,
    pages: 295,
    translations: {},
    reviews: {
      goodreads: {
        rating: 4.16,
        ratingsCount: 11663,
        reviewsCount: 812,
      },
      librarything: {
        rating: 4.13,
        ratingsCount: 2434,
        reviewsCount: 0,
      },
    },
  },
  {
    id: 3,
    title: "Dune",
    publicationDate: "1965-01-01",
    author: "Frank Herbert",
    genres: ["science fiction", "novel", "adventure"],
    hasMovieAdaptation: true,
    pages: 658,
    translations: {
      spanish: "",
    },
    reviews: {
      goodreads: {
        rating: 4.25,
        ratingsCount: 1142893,
        reviewsCount: 49701,
      },
    },
  },
  {
    id: 4,
    title: "Harry Potter and the Philosopher's Stone",
    publicationDate: "1997-06-26",
    author: "J. K. Rowling",
    genres: ["fantasy", "adventure"],
    hasMovieAdaptation: true,
    pages: 223,
    translations: {
      spanish: "Harry Potter y la piedra filosofal",
      korean: "해리 포터와 마법사의 돌",
      bengali: "হ্যারি পটার এন্ড দ্য ফিলোসফার্স স্টোন",
      portuguese: "Harry Potter e a Pedra Filosofal",
    },
    reviews: {
      goodreads: {
        rating: 4.47,
        ratingsCount: 8910059,
        reviewsCount: 140625,
      },
      librarything: {
        rating: 4.29,
        ratingsCount: 120941,
        reviewsCount: 1960,
      },
    },
  },
  {
    id: 5,
    title: "A Game of Thrones",
    publicationDate: "1996-08-01",
    author: "George R. R. Martin",
    genres: ["fantasy", "high-fantasy", "novel", "fantasy fiction"],
    hasMovieAdaptation: true,
    pages: 835,
    translations: {
      korean: "왕좌의 게임",
      polish: "Gra o tron",
      portuguese: "A Guerra dos Tronos",
      spanish: "Juego de tronos",
    },
    reviews: {
      goodreads: {
        rating: 4.44,
        ratingsCount: 2295233,
        reviewsCount: 59058,
      },
      librarything: {
        rating: 4.36,
        ratingsCount: 38358,
        reviewsCount: 1095,
      },
    },
  },
];

function getBooks() {
  return data;
}

function getBook(id) {
  return data.find((d) => d.id === id);
}

// TOPIC 1 -- Destructuring
// ======================

const books = getBook(3);
// books;

// const title = books.title;
// title;
// console.log(books.author);

const { title, author, pages, genres, publicationDate } = books;

// There are the actual object names of books and not random values.
console.log(title, author, genres);

// TOPIC 2 -- Rest and Spread Operators.
// ============================================

// Defining a List
const [p_genres, s_genres, ...rest] = genres;

// ...rest is called a rest operator. It gets the rest of the values.

console.log(p_genres, s_genres);
console.log(rest);

// If we want to create a new array, which wold include all the values of the existing array, along with some new values
// We can do the following.

const new_genres = [...genres, "epic fantasy"];
console.log(new_genres);

// This basically takes all the values of 'genres' array and puts it in the new array, one by one.
// This '...genres' here is called the Spread Operator, which is different from the '...rest' at the top.

// To Add a new property to the book object, we can do the following.
const updatedBook = { ...books, mov_rls_dt: "2001-12-20", pages: 1200 };
console.log(updatedBook);
// In the above example, we have also overriden a Property called Pages.

// TOPIC 3 -- Template Literals
// =============================

//  Similar to f-string in Python.
const summary = ` ${title} is a book written by  ${author}`;
summary;

// TOPIC 4 -- Ternary Operator
// ==========================

console.log(
  ` This book has ${
    updatedBook.pages > 1000 ? "over a thousand" : "less than a thousand"
  } Pages`
);

// Combining Ternary Operator with String Literal.

// TOPIC 4 -- Arrow Functions.
// ============================

// Old Function
function getyr(str) {
  return str.split("-")[0];
}

console.log(getyr(publicationDate));

// Arrow Functions. Only for one liners.
// Syntax : Return Value => Function Argument.

const get_yr = (str) => str.split("-")[0];
console.log(get_yr(publicationDate));

// TOPIC 5 -- Short Circuiting Logical Operators.
// ==============================================

// Short circuiting Logical Operators.
console.log(2 > 4 && 10 != 20);
console.log(2 < 4 && 10 == 10);
console.log(2 < 4 && 10 > 20);

// Falsy values : 0, null, '', undefined
console.log("anything" && undefined);
console.log(null && "whatever");

console.log(null || "whatever");

console.log(books.translations.spanish || "Not Translated to Spanish");
// This can cause problems, when the value for the first operand is 0.

console.log(0 || "Blank");

// Here 0 is a value and not blank but the Or operator is showing it as blank. In order to counter that, we have the following:
console.log(0 ?? "Blank");
console.log(" " ?? "Blank");

// This works for 0 and Empty Strings.

// TOPIC 6 -- Optional Chaining
// ===============================

console.log(books.reviews.goodreads.reviewsCount);
console.log(books.reviews.librarything?.reviewsCount);

// The book in question doesn't have a Libraanything review. So it is returning undefined.

console.log(
  books.reviews.goodreads?.reviewsCount +
    books.reviews.librarything?.reviewsCount
);

// Adding a number to undefined is returning a NaN. We can do the following to solve this.

console.log(
  (books.reviews?.goodreads?.reviewsCount ?? 0) +
    (books.reviews?.librarything?.reviewsCount ?? 0)
);

// TOPIC 7 -- Map Method.
// ======================
