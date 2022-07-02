package main

import "log"

func main() {

	var vbool bool
	vbool = false
	name := "Test"

	if vbool && name == "Shashank" {
		log.Println("Both are True")
	} else if vbool && name != "Shashank" {
		log.Println("Second Condition, name not matching")
	} else if !vbool && name == "Shashank" {
		log.Println("Second Condition, name not matching")
	} else {
		log.Println("Both Conditions not matching")
	}

	// Or is |

	log.Println("Moving to Switch case Statement")

	rem := 23 % 2

	switch rem {
	case 1:
		log.Println("Not Divisible by 2")
	case 0:
		log.Println("Divisible by 2")
	default:
		log.Println("Probably not Divisible by 2")

	}
}
