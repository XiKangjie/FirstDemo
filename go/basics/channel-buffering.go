package main

import "fmt"
import "time"

func main() {
	messages := make(chan string, 2)

	// Because this channel is bufferd, we can send these values
	// into the channel without a corresponding concurrent receive.
	messages <- "buffered"
	messages <- "channel"
	//messages <- "more"	// error: all goroutines are asleep - deadlock!

	go func() {
		for {
			messages <- "more"
			time.Sleep(time.Second * 1)
		}
	}()

	fmt.Println(<-messages)
	fmt.Println(<-messages)

	for {
		fmt.Println(<-messages)
	}
}
