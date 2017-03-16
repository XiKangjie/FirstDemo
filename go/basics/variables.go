package main

import "fmt"

func main() {
	var a string = "initial"
	fmt.Println(a)
	fmt.Printf("type of a : %T\n", a)

	// multiple
	var b, c int = 1, 2
	fmt.Println(b, c)

	// infer the type
	var d = true
	fmt.Println(d)

	// zero-valued
	var e int
	fmt.Println(e)

	// shorthand
	f := "short"
	fmt.Println(f)
}
