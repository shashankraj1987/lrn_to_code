package main

import "fmt"

func main() {
	arr := []int{1, 4, 2, 7, 2, 9}

	for i := 0; i < len(arr); i++ {
		fmt.Println("I is ", arr[i])
	}

	fmt.Println("  ")

	animals := []string{"cat", "dog", "elephant", "rabbit"}

	for _, animal := range animals {
		fmt.Println(animal)
	}

	// Simlar to Python without the "in" keyword

	// Looping over maps

	animals2 := make(map[string]string)

	animals2["fish"] = "dolphin"
	animals2["reptile"] = "snake"
	animals2["bird"] = "hawk"

	for key, value := range animals2 {
		fmt.Println(value, " is a ", key)
	}

	// we can range over strings as well.
	// strings are immutable
	// While looping over strings, it prints out the ascii of the string rather than the string.
}
