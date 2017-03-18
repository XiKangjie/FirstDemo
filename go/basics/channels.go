package main

import "fmt"

// Channels are the pipes that connect concurrent goroutines.
// You can send values into channels from one goroutine and receive those values into another goroutine.

func main() {
	// By defalut sends and receives block until both the sender and receiver are ready.
	messages := make(chan string)

	// send:	channel <-
	go func() { messages <- "ping" }()

	// receive:	<-channel
	msg := <-messages
	fmt.Println(msg)
}
