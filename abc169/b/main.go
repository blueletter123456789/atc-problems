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
	const m = 1_000_000_000_000_000_000
	n := NumStdin()
	a := make([]int, n)
	for i := range a {
		a[i] = NumStdin()
		if a[i] == 0 {
			fmt.Println(0)
			return
		}
	}

	var num int = 1
	for _, i := range a{
		
		if m/num < i || num*i > m{
			num = -1
			break
		}
		num *= i
	}

	fmt.Println(num)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
