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
	var maxN int
	a := make([]int, n)
	for i := range a {
		a[i] = NumStdin()
		if maxN < a[i] {
			maxN = a[i]
		}
	}
	
	var g int
	for i := 1; i < n; i++ {
		g = gcd(g, abs(a[i]-a[i-1]))
	}
	if g == 1 {
		fmt.Println(2)
	} else {
		fmt.Println(1)
	}

	// cnt := n
	// for i := 2; i <= maxN; i++ {
	// 	seen := make(map[int]bool)
	// 	for _, num := range a {
	// 		seen[num%i] = true
	// 	}
	// 	if cnt > len(seen) {
	// 		fmt.Println(i, len(seen))
	// 		cnt = len(seen)
	// 	}
	// }
	// fmt.Println(cnt)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
