package main

import "fmt"

func main() {
	var a [5]int
	fmt.Println("emp:", a)

	a[4] = 100
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])
	//fmt.Println("get:", a[5])

	fmt.Println("len:", len(a))
	fmt.Println("cap:", cap(a))

	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	c := a
	fmt.Println("c:", c)
	c[4] = 200
	fmt.Println("c:", c)
	fmt.Println("a:", a)

	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d:", twoD)
}
