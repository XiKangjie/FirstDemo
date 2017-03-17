package main

import "fmt"

/*
 *
 *Functions that take a value argument must take a value of that specific type:
 *
 *var v Vertex
 *fmt.Println(AbsFunc(v))  // OK
 *fmt.Println(AbsFunc(&v)) // Compile error!
 *
 *while methods with value receivers take either a value or a pointer as the receiver when they are called:
 *
 *var v Vertex
 *fmt.Println(v.Abs()) // OK
 *p := &v
 *fmt.Println(p.Abs()) // OK
 */

type rect struct {
	width, height int
}

func (r *rect) area() int {
	fmt.Printf("type r: %T\n", r)
	return r.width * r.height
}

func (r rect) perim() int {
	fmt.Printf("type r: %T\n", r)
	return 2 * (r.width + r.height)
}

func (r *rect) mutate() {
	r.width += 10
	r.height += 10
}

func main() {
	// Go automatically handles conversion between values and pointers for method calls.
	r := rect{width: 10, height: 5}

	fmt.Println("area:", r.area())
	fmt.Println("perim:", r.perim())

	rp := &r
	fmt.Println("area:", rp.area())
	fmt.Println("perim:", rp.perim())

	fmt.Printf("before, width: %d, height: %d\n", r.width, r.height)
	r.mutate()
	fmt.Printf("after, width: %d, height: %d\n", r.width, r.height)
}
