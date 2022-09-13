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
	a := make([]int, n)
	for i := range a {
		a[i] = NumStdin()
	}

	stock, deposit := 0, 1000
	for i := 0; i < n; i++ {
		deposit += stock * a[i]
		stock = 0
		// Buy if the stock price rises the next day
		if i+1 < n && a[i] < a[i+1] {
			stock = deposit / a[i]
			deposit -= stock * a[i]
		}
	}

	fmt.Println(deposit)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
