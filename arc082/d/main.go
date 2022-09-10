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
	same := make([]bool, n)
	for i := range same {
		p := NumStdin()
		same[i] = (i + 1) == p
	}

	var cnt, i int
	for i < n-1 {
		if same[i] {
			cnt++
			same[i], same[i+1] = false, false
		}
		i++
	}
	if same[n-1] {
		cnt++
	}

	fmt.Println(cnt)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
