package main

import "sort"
import "fmt"

type ByLength []string

// We implement sort.Interface - Len, Less, and Swap - on our type so we can
// use the sort package's generic Sort fuction.
func (s ByLength) Len() int {
	return len(s)
}

func (s ByLength) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s ByLength) Less(i, j int) bool {
	return len(s[i]) < len(s[j])
}

func main() {
	fruits := []string{"peach", "banana", "kiwi"}
	// casting the original fruits slice to ByLength
	sort.Sort(ByLength(fruits))
	fmt.Println(fruits)
}
