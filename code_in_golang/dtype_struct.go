package main

import (
	"log"
	"time"
)

type User struct {
	FirstName string
	LastName  string
	Age       int
	BirthDate time.Time
}

//  If struct is like a class, then we can define the functions for a class.

func (m *User) printName() string {
	return "User Name is " + m.FirstName + " " + m.LastName
}

func (m *User) printAge() int {
	return m.Age
}

func main() {
	usr1 := User{
		FirstName: "Shashank",
		LastName:  "Raj",
		Age:       35,
	}
	// usr1 ends with , even after the last field.

	log.Println(usr1.printName())
	log.Println(usr1.printAge())
}

func Add(a int, b int) int {
	//  Names starting with Capital Letters would be visible
	//  outside the main package.
	return a + b

}
