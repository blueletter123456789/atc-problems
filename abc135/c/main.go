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
	a := make([]int, n+1)
	for i := range a {
		a[i] = NumStdin()
	}

	b := make([]int, n)
	for i := range b {
		b[i] = NumStdin()
	}

	var ans int
	for i := range b {
		if b[i] < a[i] {
			ans += b[i]
		} else {
			ans += a[i]
			b[i] -= a[i]
			if a[i+1] > b[i] {
				ans += b[i]
				a[i+1] -= b[i]
			} else {
				ans += a[i+1]
				a[i+1] = 0
			}
		}
	}

	fmt.Println(ans)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
