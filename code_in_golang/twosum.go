package main

import (
	"fmt"
)

func TwoNumSum(arr []int, trgt int) []int {
	final := []int{}
	for i, num := range arr {
		for j := len(arr) - 1; j > i; j-- {
			if (trgt-num) == arr[j] && i != j {
				final = append(final, num)
				final = append(final, arr[j])
			}
		}
	}
	return final
}

func main() {
	trgt := 10
	arr := []int{3, 5, -4, 8, 11, 1, -1, 6}
	fmt.Println(TwoNumSum(arr, trgt))
}
