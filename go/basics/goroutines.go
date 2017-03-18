package main

import "fmt"

func f(from string) {
	for i := 0; i < 100; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {
	f("direct")

	// invoke the function in a goroutine, this new goroutine will
	// execute concurrently with the calling one.
	go f("goroutine")

	go func(msg string) {
		fmt.Println(msg)
	}("going")

	// When we run this program, we see the output of the blocking call first,
	// then the interleaved output of the two gouroutines. This interleaving
	// reflects the goroutines being run concurrently by the Go runtime.

	var input string
	fmt.Scanln(&input)
	fmt.Println("done")
}
