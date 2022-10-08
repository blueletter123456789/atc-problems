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
	M = 1_000_000_007
)

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	n := NumStdin()
	m := NumStdin()

	if abs(n-m) > 1 {
		fmt.Println(0)
		return
	}

	numN := 1
	for i := 1; i <= n; i++ {
		numN *= i
		numN %= M
	}

	numM := 1
	for i := 1; i <= m; i++ {
		numM *= i
		numM %= M
	}

	ans := (numN * numM) % M

	if n == m {
		ans = (ans * 2) % M
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

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
