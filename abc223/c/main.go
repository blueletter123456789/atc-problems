package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var scan = bufio.NewScanner(os.Stdin)

const (
	initBufSize = 10000
	maxBufSize = 10000000
)

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	n := NumStdin()
	a := make([]float64, n)
	b := make([]float64, n)

	var centralTime float64
	for i := range a {
		a[i], b[i] = float64(NumStdin()), float64(NumStdin())
		centralTime += a[i] / b[i]
	}

	centralTime /= 2

	var dist float64
	var i int
	for centralTime > 0 {
		partTime := a[i]/b[i]
		if centralTime - partTime > 0 {
			dist += a[i]
		} else {
			dist += b[i]*centralTime
			break
		}

		centralTime -= partTime
		i++
	}

	fmt.Printf("%.15f\n", dist)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
