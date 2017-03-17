package main

import "fmt"

func plus(a int, b int) int {
	return a + b
}

func plusPlus(a, b, c int) int {
	return a + b + c
}

func swap(a, b *int) {
	t := *a
	*a = *b
	*b = t
}

func main() {
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)

	a, b := 1, 2
	fmt.Printf("before swap, a: %d, b: %d\n", a, b)
	swap(&a, &b)
	//swap(a, b)	// error
	fmt.Printf("after swap, a: %d, b: %d\n", a, b)
}
