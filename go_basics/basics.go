package main

import (
	"fmt"
	"log"
	"time"
)

var PI = 3.414
var now time.Time

func main() {
	var txt string = "Hello"
	fmt.Println(txt)
	tst := test_out()
	// := is used to assign the variable type to func's return type.
	// So we do not have to explicitly declare them.
	log.Println(tst)
	pointr_str(&tst)

	//  Pointer to a String is passed using &string
	log.Println(tst)
	log.Println(pass_2_params(tst))
	log.Println("The Value of the Global Variable is ", PI)
	PI = 5566
	log.Println("The Value of the Local Variable is ", PI)

	// Arithmetic Operators

	log.Println(23 / 2) // Reruens the quotient
	log.Println(23 % 2) // Returns the Remainder

}

func test_out() string {
	return "JMD"
}

func pointr_str(s *string) {
	//  Here we are declaring that s is a pointer of type string.
	*s = "Red"
}

func pass_2_params(s string) (string, string) {
	return s, "Second Argument"
}
