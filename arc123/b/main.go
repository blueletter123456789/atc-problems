package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var scan = bufio.NewScanner(os.Stdin)

const (
	initBufSize = 10000
	maxBufSize = 1000000000000
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

	b := make([]int, n)
	for i := range b {
		b[i] = NumStdin()
	}

	c := make([]int, n)
	for i := range c {
		c[i] = NumStdin()
	}

	sort.Slice(a, func(i, j int) bool { return a[i] < a[j] })
	sort.Slice(b, func(i, j int) bool { return b[i] < b[j] })
	sort.Slice(c, func(i, j int) bool { return c[i] < c[j] })

	var ans int
	for _, num := range a {
		idxB := upperBound(b, num)
		if idxB >= len(b) {
			break
		}
		
		idxC := upperBound(c, b[idxB])
		if idxC >= len(c) {
			break
		}

		b = b[idxB+1:]
		c = c[idxC+1:]
		ans++
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

func upperBound(a []int, x int) int {
	return sort.Search(len(a), func(i int) bool { return a[i] > x })
}
