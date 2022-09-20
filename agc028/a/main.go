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
	m := NumStdin()
	s := StrStdin()
	t := StrStdin()

	l := n * m / gcd(n, m)

	seen := make(map[int]string, n)
	for i, chr := range s {
		idx := i * (l/n) + 1
		seen[idx] = string(chr)
	}

	for i, chr := range t {
		idx := i * (l/m) + 1
		if si, ok := seen[idx]; ok && string(chr) != si {
			fmt.Println(-1)
			return
		}
	}

	fmt.Println(l)
}

func StrStdin() string {
	scan.Scan()
	return scan.Text()
}

func NumStdin() int {
	num, err := strconv.Atoi(StrStdin())
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
