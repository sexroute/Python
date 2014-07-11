package main

import (
	"fmt"
	"time"
)

func say(s string, interval int) {
	for i := 0; i < 5; i++ {
		time.Sleep(time.Duration(interval) * time.Millisecond)
		fmt.Println(s)
	}
}

func main() {
	go say("world", 500)
	go say("hello", 500)
	time.Sleep(1000 * time.Millisecond)
	fmt.Println("Over")
}