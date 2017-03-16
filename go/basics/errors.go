package main

import "errors"
import "fmt"

// By convention, errors are the last return value and have
// type error, a built-in interface.

// The error type is an interface type. An error variable represents
// any value that can describe itself as a string.

//Here is the interface's declaration:
/*
 *type error interface {
 *    Error() string
 *}
 */

func f1(arg int) (int, error) {
	if arg == 42 {
		// errors.New constructs a basic error value with the
		// given error message
		return -1, errors.New("can't work with 42")
	}
	return arg + 3, nil
}

// It's possible to use custom types as errors by
// implementing the Error() method on them.
type argError struct {
	arg  int
	prob string
}

func (e *argError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.prob)
}

func f2(arg int) (int, error) {
	if arg == 42 {
		return -1, &argError{arg, "can't work with it"}
	}
	return arg + 3, nil
}

func main() {
	for _, i := range []int{7, 42} {
		if r, e := f1(i); e != nil {
			fmt.Println("f1 failed:", e)
		} else {
			fmt.Println("f1 worked:", r)
		}
	}

	for _, i := range []int{7, 42} {
		if r, e := f2(i); e != nil {
			fmt.Println("f2 failed:", e)
		} else {
			fmt.Println("f2 worked:", r)
		}
	}

	// use the data in a custom error
	_, e := f2(42)
	// get the error as an instance of the custom error type
	// via type assertion
	if ae, ok := e.(*argError); ok {
		fmt.Println(ae.arg)
		fmt.Println(ae.prob)
	}
}
