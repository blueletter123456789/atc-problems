package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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
	r := make([]int, n)
	for i := range r {
		r[i] = NumStdin()
	}
	c := make([]int, n)
	for i := range c {
		c[i] = NumStdin()
	}

	q := NumStdin()
	ans := make([]string, q)
	for i := 0; i < q; i++ {
		rq, cq := NumStdin()-1, NumStdin()-1
		rc := r[rq] + c[cq]
		if rc > n {
			ans = append(ans, "#")
		} else {
			ans = append(ans, ".")
		}
	}

	fmt.Println(strings.Join(ans, ""))
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
