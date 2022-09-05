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
	var centralLen int
	for i := range a {
		a[i] = NumStdin()
		centralLen += a[i]
	}

	centralLen /= 2
	var leftLen, rightLen int
	i, j := 0, n-1
	for j - i > 0 {
		if leftLen + a[i] <= centralLen {
			leftLen += a[i]
			i++
		}
		if rightLen + a[j] <= centralLen {
			rightLen += a[j]
			j--
		}
	}

	var ans int
	if i == j {
		ans = min((abs(leftLen+a[i]) - rightLen), abs(leftLen - (rightLen+a[j])))
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

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
