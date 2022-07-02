package main

import (
	"log"
)

func main() {

	// Create a Basic Dictionary of type string
	// Maps are immutable, unsorted

	strMap := make(map[string]string)

	// The First string at the top, indicates the key type
	// The Second string at the top, indicates the Value type

	strMap["Name"] = "Shashank"
	strMap["id"] = "3265"

	log.Println(strMap)

	// Creating a Map of Mixed Datatype

	mixMap := make(map[string]int)

	mixMap["Age"] = 23
	log.Println(mixMap)

	// Maps can also store structs
	type User struct {
		Fname string
		Lname string
		Age   int
	}

	usrMap := make(map[string]User)

	usr1 := User{
		Fname: "Shashank",
		Lname: "Raj",
		Age:   35,
	}

	usrMap["Me"] = usr1

	log.Println(usrMap)

	advMap := make(map[string]interface{})
	advMap["Name"] = "ABC"
	advMap["Nbr "] = 32
	// interface means that we are not sure what Datatype we would be storing.

	log.Println(advMap)

	// Slices/Arrays in Go
	// Slices preservs the order

	var alphs []string

	alphs = append(alphs, "def")
	alphs = append(alphs, "abc")

	log.Println(alphs)

	// Slice Operations on Ints
	arr := []int{1, 3, 4, 5, 6, 9, 3, 6, 7}

	log.Println(arr[1:5])
	// fmt.Println will always be printed out after all the Logs

	// Upto but not including the index after :, which is 5
	// Negative index is not supported.

	// Array of Mixed Datatype
	var advSlice []interface{}
	advSlice = append(advSlice, "ABc")
	advSlice = append(advSlice, 123)
	log.Println(advSlice)

}
