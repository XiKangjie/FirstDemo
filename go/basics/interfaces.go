package main

import "fmt"
import "math"

type geometry interface {
	area() float64
	perim() float64
}

type rect struct {
	width, height float64
}

type circle struct {
	radius float64
}

// To implement an interface in Go, we just need to
// implement all the methods in the interface.

// rect implements geometry
func (r rect) area() float64 {
	return r.width * r.height
}

func (r rect) perim() float64 {
	return 2 * (r.width + r.height)
}

// *circle implements geometry, but circle DOES NOT implement geometry
func (c *circle) area() float64 {
	return math.Pi * c.radius * c.radius
}

func (c *circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	rp := &rect{width: 3, height: 4}
	c := circle{radius: 5}
	cp := &circle{radius: 5}

	measure(r)
	measure(rp)
	//measure(c) // error, because circle is not geometry, but *circle is.
	fmt.Printf("c area: %f, perim: %f\n", c.area(), c.perim())
	measure(cp)
}
